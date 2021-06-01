##
## Licensed to the Apache Software Foundation (ASF) under one
## or more contributor license agreements.  See the NOTICE file
## distributed with this work for additional information
## regarding copyright ownership.  The ASF licenses this file
## to you under the Apache License, Version 2.0 (the
## "License"); you may not use this file except in compliance
## with the License.  You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing,
## software distributed under the License is distributed on an
## "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
## KIND, either express or implied.  See the License for the
## specific language governing permissions and limitations
## under the License.
##

# DESCRIPTION: Basic Flink AI Flow image\

FROM python:3.7-slim-buster
LABEL maintainer="jiangxin369@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV PYTHONFAULTHANDLER=1

# Airflow
ARG AIRFLOW_USER_HOME=/usr/local/airflow
ARG AIRFLOW_DEPS=""
ARG PYTHON_DEPS=""
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}
ENV AIRFLOW_DEPLOY_PATH=${AIRFLOW_HOME}/airflow_deploy

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

RUN set -ex \
    && buildDeps=' \
        freetds-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
    ' \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        freetds-bin \
        build-essential \
        default-libmysqlclient-dev \
        apt-utils \
        curl \
        rsync \
        netcat \
        locales \
        unzip \
        wget \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && useradd -ms /bin/bash -d ${AIRFLOW_USER_HOME} airflow \
    && pip install -U pip setuptools wheel \
    && pip install pytz \
    && pip install pyOpenSSL \
    && pip install ndg-httpsclient \
    && pip install pyasn1 \
    && pip install mysqlclient \
    && pip install 'redis==3.2' \
    && if [ -n "${PYTHON_DEPS}" ]; then pip install ${PYTHON_DEPS}; fi \
    && apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y default-mysql-client
RUN apt-get install -y procps
RUN apt-get install -y vim
RUN apt-get install -y less
RUN apt-get install -y --no-install-recommends nodejs npm bzip2
RUN npm install --global yarn

# For locally dev, it's better to pre-install master version of Flink AI Flow dependencies so that
# we do not have to always reinstall it from the scratch.
# WORKDIR /tmp
# RUN git clone https://github.com/alibaba/flink-ai-extended.git
# RUN pip install flink-ai-extended/flink-ai-flow/lib/notification_service
# RUN pip install flink-ai-extended/flink-ai-flow/lib/airflow
# RUN pip install flink-ai-extended/flink-ai-flow
# RUN pip uninstall -y typing

ARG FLINK_AI_FLOW_SOURCES=/opt/flink-ai-flow
ENV FLINK_AI_FLOW_SOURCES=${FLINK_AI_FLOW_SOURCES}

WORKDIR ${FLINK_AI_FLOW_SOURCES}
COPY . ${FLINK_AI_FLOW_SOURCES}/

RUN bash lib/airflow/airflow/www/compile_assets.sh
RUN pip install lib/notification_service
RUN pip install lib/airflow
RUN pip install .

RUN wget https://archive.apache.org/dist/flink/flink-1.11.3/flink-1.11.3-bin-scala_2.11.tgz \
    && tar -xvzf flink-1.11.3-bin-scala_2.11.tgz \
    && mv flink-1.11.3 /flink \
    && rm -f flink-1.11.3-bin-scala_2.11.tgz

ARG flink_ml_jar=https://ai-flow-packages.oss-cn-hangzhou.aliyuncs.com/flink-ai-extended/flink-ml-dist-0.3.0.jar
RUN wget -q $flink_ml_jar -O /flink/lib/flink-ml-dist-0.2.2.jar

RUN python -m pip install --no-cache-dir \
        https://ai-flow-packages.oss-cn-hangzhou.aliyuncs.com/flink-ai-extended/0.2.2/flink_ml_framework-0.2.2-cp37-cp37m-linux_x86_64.whl \
        https://ai-flow-packages.oss-cn-hangzhou.aliyuncs.com/flink-ai-extended/0.2.2/flink_ml_tensorflow-0.2.2-cp37-cp37m-linux_x86_64.whl

RUN wget https://ai-flow-packages.oss-cn-hangzhou.aliyuncs.com/hadoop-2.7.7.tar.gz \
         && tar -zxvf hadoop-2.7.7.tar.gz \
         && mv hadoop-2.7.7 /hadoop \
         && rm -f hadoop-2.7.7.tar.gz

ENV HADOOP_HDFS_HOME=/hadoop
ENV HADOOP_HOME=/hadoop
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${JAVA_HOME}/jre/lib/amd64/server:${HADOOP_HDFS_HOME}/lib/native


RUN mkdir -p /usr/share/man/man1 && \
    apt-get install -y default-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=/flink/bin:$PATH

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

RUN echo "airflow_deploy_path: ${AIRFLOW_DEPLOY_PATH}" >> ${FLINK_AI_FLOW_SOURCES}/examples/quickstart_example/project.yaml

EXPOSE 8080 50051 50052

USER root
WORKDIR ${AIRFLOW_USER_HOME}

ENTRYPOINT ["/entrypoint.sh"]
CMD [ ]