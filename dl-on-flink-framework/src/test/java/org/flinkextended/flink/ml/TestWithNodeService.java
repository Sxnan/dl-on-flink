/*
 * Copyright 2022 Deep Learning on Flink Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.flinkextended.flink.ml;

import org.flinkextended.flink.ml.cluster.node.MLContext;
import org.flinkextended.flink.ml.cluster.rpc.NodeServer;
import org.flinkextended.flink.ml.util.ContextService;
import org.flinkextended.flink.ml.util.IpHostUtil;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import org.junit.AfterClass;
import org.junit.BeforeClass;

import java.io.IOException;

/** Abstract unit test that start node service before testing. */
public abstract class TestWithNodeService {

    private static Server server;
    private static ContextService service;

    @BeforeClass
    public static void startServer() throws IOException {
        service = new ContextService();
        server = ServerBuilder.forPort(0).addService(service).build();
        server.start();
    }

    @AfterClass
    public static void stopServer() {
        server.shutdown();
    }

    protected void configureContext(MLContext context) throws Exception {
        context.setNodeServerIP(IpHostUtil.getIpAddress());
        context.setNodeServerPort(server.getPort());
        NodeServer.prepareStartupScript(context);
        service.setMlContext(context);
    }
}
