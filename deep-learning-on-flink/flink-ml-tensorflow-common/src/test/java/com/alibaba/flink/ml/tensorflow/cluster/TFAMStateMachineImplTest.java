package com.alibaba.flink.ml.tensorflow.cluster;

import com.alibaba.flink.ml.cluster.BaseEventReporter;
import com.alibaba.flink.ml.cluster.master.AMEvent;
import com.alibaba.flink.ml.cluster.master.AMEventType;
import com.alibaba.flink.ml.cluster.master.meta.AMMeta;
import com.alibaba.flink.ml.cluster.node.MLContext;
import com.alibaba.flink.ml.cluster.rpc.AppMasterServer;
import com.alibaba.flink.ml.cluster.statemachine.StateMachine;
import com.alibaba.flink.ml.proto.AMStatus;
import com.alibaba.flink.ml.util.DummyContext;
import org.junit.Test;
import org.mockito.Mockito;

import static org.junit.Assert.*;

public class TFAMStateMachineImplTest {

	@Test
	public void testBuildStateMachine() {
		final MLContext mlContext = DummyContext.createDummyMLContext();
		final AMMeta amMeta = Mockito.mock(AMMeta.class);
		final TFAMStateMachineImpl stateMachine = new TFAMStateMachineImpl(Mockito.mock(AppMasterServer.AppMasterServiceImpl.class),
				amMeta, mlContext, Mockito.mock(BaseEventReporter.class));
		final StateMachine<AMStatus, AMEventType, AMEvent> machine =
				stateMachine.buildStateMachine(mlContext, amMeta);
		assertEquals(AMStatus.AM_UNKNOW, machine.getCurrentState());
	}
}