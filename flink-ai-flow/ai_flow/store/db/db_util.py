#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import logging
import os
import re
import urllib.parse
from contextlib import contextmanager

import sqlalchemy
from ai_flow.store.sqlalchemy_store import SqlAlchemyStore

from ai_flow.store.mongo_store import MongoStore

from notification_service.util.db import DBType

from ai_flow.protobuf.message_pb2 import INTERNAL_ERROR
from ai_flow.endpoint.server.exception import AIFlowException
from ai_flow.store import AIFLOW_SQLALCHEMYSTORE_MAX_OVERFLOW, AIFLOW_SQLALCHEMYSTORE_POOL_SIZE
from ai_flow.store.db.db_engine import DATABASE_ENGINES

_logger = logging.getLogger(__name__)


def extract_db_engine_from_uri(db_uri):
    """
    Parse specified database URI to extract database type. Confirm extracted database engine is
    supported. If database driver is specified, confirm driver passes a plausible regex.
    """
    scheme = urllib.parse.urlparse(db_uri).scheme
    scheme_plus_count = scheme.count('+')

    """validates scheme parsed from DB URI is supported"""
    if scheme_plus_count == 0:
        db_engine = scheme
    elif scheme_plus_count == 1:
        db_engine, _ = scheme.split('+')
    else:
        error_msg = "Invalid database URI: '%s'." % db_uri
        raise AIFlowException(error_msg)

    """validates db_engine parsed from DB URI is supported"""
    if db_engine not in DATABASE_ENGINES:
        error_msg = "Invalid database engine: '%s'." % db_engine
        raise AIFlowException(error_msg)

    return db_engine


def _get_managed_session_maker(SessionMaker):
    """
    Creates session factory for generating exception-safe SQLAlchemy sessions that are available for
    using session context manager. Session generated by session factory is automatically committed
    if no exceptions are encountered within its associated context. If an exception is
    encountered, this session could be rolled back. Session generated by session factory is
    automatically closed when the session's associated context is exited.
    """

    @contextmanager
    def make_managed_session():
        """Provide transactional scope around series of session operations."""
        session = SessionMaker()
        try:
            yield session
            session.commit()
        except AIFlowException:
            session.rollback()
            raise
        except Exception as e:
            session.rollback()
            raise AIFlowException(error_msg=e, error_code=INTERNAL_ERROR)
        finally:
            session.close()

    return make_managed_session


def create_sqlalchemy_engine(db_uri):
    """
    Create SQLAlchemy engine with specified database URI to support AIFlow entities backend storage.
    """
    pool_size = os.environ.get(AIFLOW_SQLALCHEMYSTORE_POOL_SIZE)
    pool_max_overflow = os.environ.get(AIFLOW_SQLALCHEMYSTORE_MAX_OVERFLOW)
    pool_kwargs = {}
    if pool_size:
        pool_kwargs['pool_size'] = int(pool_size)
    if pool_max_overflow:
        pool_kwargs['max_overflow'] = int(pool_max_overflow)
    if pool_kwargs:
        _logger.info("Create SQLAlchemy engine with pool options %s", pool_kwargs)
    return sqlalchemy.create_engine(db_uri, pool_pre_ping=True, **pool_kwargs)


def parse_mongo_uri(db_uri):
    """
    Parse MongoDB URI-style string to split up and return credentials

    Args:
        db_uri (string): MongoDB URI-style string
    Return:

    """
    regex_str = r'^(?P<schema>(mongodb:(?:\/{2})?))((?P<user>\w+?):(?P<pwd>(\w+?))@|:@?)(?P<host>(\S+?)):(?P<port>(\d+))(\/(?P<db>(\S+?)))$'
    pattern = re.compile(regex_str)
    m = pattern.match(db_uri)
    if m is None:
        raise Exception('The URI of MongoDB is invalid')
    return m.group('user'), m.group('pwd'), m.group('host'), m.group('port'), m.group('db')


def create_db_store(db_uri):
    db_engine = extract_db_engine_from_uri(db_uri)
    if DBType.value_of(db_engine) == DBType.MONGODB:
        username, password, host, port, db = parse_mongo_uri(db_uri)
        store = MongoStore(host=host,
                           port=int(port),
                           username=username,
                           password=password,
                           db=db)
    else:
        store = SqlAlchemyStore(db_uri)
    return store
