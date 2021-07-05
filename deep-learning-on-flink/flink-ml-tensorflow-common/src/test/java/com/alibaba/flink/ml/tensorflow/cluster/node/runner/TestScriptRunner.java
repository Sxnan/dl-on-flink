package com.alibaba.flink.ml.tensorflow.cluster.node.runner;

import com.alibaba.flink.ml.cluster.node.MLContext;
import com.alibaba.flink.ml.cluster.node.runner.AbstractScriptRunner;

import java.io.IOException;

public class TestScriptRunner extends AbstractScriptRunner {

	public TestScriptRunner(MLContext mlContext) {
		super(mlContext);
	}

	@Override
	public void runScript() throws IOException {

	}

	@Override
	public void notifyKillSignal() {

	}

	@Override
	public void close() throws IOException {

	}
}
