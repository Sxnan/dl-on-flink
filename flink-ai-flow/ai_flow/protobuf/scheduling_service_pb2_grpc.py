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

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import scheduling_service_pb2 as scheduling__service__pb2


class SchedulingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.submitWorkflow = channel.unary_unary(
                '/ai_flow.SchedulingService/submitWorkflow',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowInfoResponse.FromString,
                )
        self.deleteWorkflow = channel.unary_unary(
                '/ai_flow.SchedulingService/deleteWorkflow',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowInfoResponse.FromString,
                )
        self.pauseWorkflowScheduling = channel.unary_unary(
                '/ai_flow.SchedulingService/pauseWorkflowScheduling',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowInfoResponse.FromString,
                )
        self.resumeWorkflowScheduling = channel.unary_unary(
                '/ai_flow.SchedulingService/resumeWorkflowScheduling',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowInfoResponse.FromString,
                )
        self.getWorkflow = channel.unary_unary(
                '/ai_flow.SchedulingService/getWorkflow',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowInfoResponse.FromString,
                )
        self.listWorkflows = channel.unary_unary(
                '/ai_flow.SchedulingService/listWorkflows',
                request_serializer=scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ListWorkflowInfoResponse.FromString,
                )
        self.startNewWorkflowExecution = channel.unary_unary(
                '/ai_flow.SchedulingService/startNewWorkflowExecution',
                request_serializer=scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowExecutionResponse.FromString,
                )
        self.killAllWorkflowExecutions = channel.unary_unary(
                '/ai_flow.SchedulingService/killAllWorkflowExecutions',
                request_serializer=scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ListWorkflowExecutionResponse.FromString,
                )
        self.killWorkflowExecution = channel.unary_unary(
                '/ai_flow.SchedulingService/killWorkflowExecution',
                request_serializer=scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowExecutionResponse.FromString,
                )
        self.getWorkflowExecution = channel.unary_unary(
                '/ai_flow.SchedulingService/getWorkflowExecution',
                request_serializer=scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.WorkflowExecutionResponse.FromString,
                )
        self.listWorkflowExecutions = channel.unary_unary(
                '/ai_flow.SchedulingService/listWorkflowExecutions',
                request_serializer=scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ListWorkflowExecutionResponse.FromString,
                )
        self.startJob = channel.unary_unary(
                '/ai_flow.SchedulingService/startJob',
                request_serializer=scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.JobInfoResponse.FromString,
                )
        self.stopJob = channel.unary_unary(
                '/ai_flow.SchedulingService/stopJob',
                request_serializer=scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.JobInfoResponse.FromString,
                )
        self.restartJob = channel.unary_unary(
                '/ai_flow.SchedulingService/restartJob',
                request_serializer=scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.JobInfoResponse.FromString,
                )
        self.getJob = channel.unary_unary(
                '/ai_flow.SchedulingService/getJob',
                request_serializer=scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.JobInfoResponse.FromString,
                )
        self.listJobs = channel.unary_unary(
                '/ai_flow.SchedulingService/listJobs',
                request_serializer=scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ListJobInfoResponse.FromString,
                )
        self.getExecutionLabel = channel.unary_unary(
                '/ai_flow.SchedulingService/getExecutionLabel',
                request_serializer=scheduling__service__pb2.SchedulingNameRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ExecutionLabelResponse.FromString,
                )
        self.upsertExecutionLabel = channel.unary_unary(
                '/ai_flow.SchedulingService/upsertExecutionLabel',
                request_serializer=scheduling__service__pb2.ExecutionLabelRequest.SerializeToString,
                response_deserializer=scheduling__service__pb2.ExecutionLabelResponse.FromString,
                )


class SchedulingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def submitWorkflow(self, request, context):
        """workflow api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pauseWorkflowScheduling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resumeWorkflowScheduling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listWorkflows(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def startNewWorkflowExecution(self, request, context):
        """workflow execution api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def killAllWorkflowExecutions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def killWorkflowExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWorkflowExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listWorkflowExecutions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def startJob(self, request, context):
        """job api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def restartJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getExecutionLabel(self, request, context):
        """Execution label api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upsertExecutionLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchedulingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'submitWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.submitWorkflow,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowInfoResponse.SerializeToString,
            ),
            'deleteWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteWorkflow,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowInfoResponse.SerializeToString,
            ),
            'pauseWorkflowScheduling': grpc.unary_unary_rpc_method_handler(
                    servicer.pauseWorkflowScheduling,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowInfoResponse.SerializeToString,
            ),
            'resumeWorkflowScheduling': grpc.unary_unary_rpc_method_handler(
                    servicer.resumeWorkflowScheduling,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowInfoResponse.SerializeToString,
            ),
            'getWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.getWorkflow,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowInfoResponse.SerializeToString,
            ),
            'listWorkflows': grpc.unary_unary_rpc_method_handler(
                    servicer.listWorkflows,
                    request_deserializer=scheduling__service__pb2.ScheduleWorkflowRequest.FromString,
                    response_serializer=scheduling__service__pb2.ListWorkflowInfoResponse.SerializeToString,
            ),
            'startNewWorkflowExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.startNewWorkflowExecution,
                    request_deserializer=scheduling__service__pb2.WorkflowExecutionRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowExecutionResponse.SerializeToString,
            ),
            'killAllWorkflowExecutions': grpc.unary_unary_rpc_method_handler(
                    servicer.killAllWorkflowExecutions,
                    request_deserializer=scheduling__service__pb2.WorkflowExecutionRequest.FromString,
                    response_serializer=scheduling__service__pb2.ListWorkflowExecutionResponse.SerializeToString,
            ),
            'killWorkflowExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.killWorkflowExecution,
                    request_deserializer=scheduling__service__pb2.WorkflowExecutionRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowExecutionResponse.SerializeToString,
            ),
            'getWorkflowExecution': grpc.unary_unary_rpc_method_handler(
                    servicer.getWorkflowExecution,
                    request_deserializer=scheduling__service__pb2.WorkflowExecutionRequest.FromString,
                    response_serializer=scheduling__service__pb2.WorkflowExecutionResponse.SerializeToString,
            ),
            'listWorkflowExecutions': grpc.unary_unary_rpc_method_handler(
                    servicer.listWorkflowExecutions,
                    request_deserializer=scheduling__service__pb2.WorkflowExecutionRequest.FromString,
                    response_serializer=scheduling__service__pb2.ListWorkflowExecutionResponse.SerializeToString,
            ),
            'startJob': grpc.unary_unary_rpc_method_handler(
                    servicer.startJob,
                    request_deserializer=scheduling__service__pb2.ScheduleJobRequest.FromString,
                    response_serializer=scheduling__service__pb2.JobInfoResponse.SerializeToString,
            ),
            'stopJob': grpc.unary_unary_rpc_method_handler(
                    servicer.stopJob,
                    request_deserializer=scheduling__service__pb2.ScheduleJobRequest.FromString,
                    response_serializer=scheduling__service__pb2.JobInfoResponse.SerializeToString,
            ),
            'restartJob': grpc.unary_unary_rpc_method_handler(
                    servicer.restartJob,
                    request_deserializer=scheduling__service__pb2.ScheduleJobRequest.FromString,
                    response_serializer=scheduling__service__pb2.JobInfoResponse.SerializeToString,
            ),
            'getJob': grpc.unary_unary_rpc_method_handler(
                    servicer.getJob,
                    request_deserializer=scheduling__service__pb2.ScheduleJobRequest.FromString,
                    response_serializer=scheduling__service__pb2.JobInfoResponse.SerializeToString,
            ),
            'listJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.listJobs,
                    request_deserializer=scheduling__service__pb2.ScheduleJobRequest.FromString,
                    response_serializer=scheduling__service__pb2.ListJobInfoResponse.SerializeToString,
            ),
            'getExecutionLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.getExecutionLabel,
                    request_deserializer=scheduling__service__pb2.SchedulingNameRequest.FromString,
                    response_serializer=scheduling__service__pb2.ExecutionLabelResponse.SerializeToString,
            ),
            'upsertExecutionLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.upsertExecutionLabel,
                    request_deserializer=scheduling__service__pb2.ExecutionLabelRequest.FromString,
                    response_serializer=scheduling__service__pb2.ExecutionLabelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai_flow.SchedulingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SchedulingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def submitWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/submitWorkflow',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.WorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/deleteWorkflow',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.WorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pauseWorkflowScheduling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/pauseWorkflowScheduling',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.WorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resumeWorkflowScheduling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/resumeWorkflowScheduling',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.WorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/getWorkflow',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.WorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listWorkflows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/listWorkflows',
            scheduling__service__pb2.ScheduleWorkflowRequest.SerializeToString,
            scheduling__service__pb2.ListWorkflowInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def startNewWorkflowExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/startNewWorkflowExecution',
            scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
            scheduling__service__pb2.WorkflowExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def killAllWorkflowExecutions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/killAllWorkflowExecutions',
            scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
            scheduling__service__pb2.ListWorkflowExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def killWorkflowExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/killWorkflowExecution',
            scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
            scheduling__service__pb2.WorkflowExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getWorkflowExecution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/getWorkflowExecution',
            scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
            scheduling__service__pb2.WorkflowExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listWorkflowExecutions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/listWorkflowExecutions',
            scheduling__service__pb2.WorkflowExecutionRequest.SerializeToString,
            scheduling__service__pb2.ListWorkflowExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def startJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/startJob',
            scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
            scheduling__service__pb2.JobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/stopJob',
            scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
            scheduling__service__pb2.JobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def restartJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/restartJob',
            scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
            scheduling__service__pb2.JobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/getJob',
            scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
            scheduling__service__pb2.JobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/listJobs',
            scheduling__service__pb2.ScheduleJobRequest.SerializeToString,
            scheduling__service__pb2.ListJobInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getExecutionLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/getExecutionLabel',
            scheduling__service__pb2.SchedulingNameRequest.SerializeToString,
            scheduling__service__pb2.ExecutionLabelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upsertExecutionLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai_flow.SchedulingService/upsertExecutionLabel',
            scheduling__service__pb2.ExecutionLabelRequest.SerializeToString,
            scheduling__service__pb2.ExecutionLabelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)