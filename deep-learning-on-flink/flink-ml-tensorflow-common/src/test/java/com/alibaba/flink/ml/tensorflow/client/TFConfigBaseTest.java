package com.alibaba.flink.ml.tensorflow.client;

import com.alibaba.flink.ml.cluster.MLConfig;
import com.alibaba.flink.ml.tensorflow.util.TFConstants;
import org.junit.Before;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.*;

public class TFConfigBaseTest {

	private TestTFConfig tfConfig;
	private Map<String, String> properties;
	private String envPath;
	private String func;
	private String pythonFile;
	private int psNum;
	private int workerNum;

	@Before
	public void setUp() throws Exception {
		properties = new HashMap<>();
		properties.put("key", "value");
		envPath = "/tmp/env";
		func = "func";
		pythonFile = "/tmp/test.py";
		psNum = 2;
		workerNum = 1;
		tfConfig = new TestTFConfig(workerNum, psNum, properties,
				pythonFile, func, envPath);
	}

	@Test
	public void testGetEnvPath() {
		assertEquals(envPath, tfConfig.getEnvPath());
	}

	@Test
	public void testPythonFiles() {
		String[] pythonFiles = tfConfig.getPythonFiles();
		assertEquals(1, pythonFiles.length);
		assertEquals(pythonFile, pythonFiles[0]);

		pythonFiles = new String[]{"1.py", "2.py"};
		tfConfig.setPythonFiles(pythonFiles);
		assertArrayEquals(pythonFiles, tfConfig.getPythonFiles());
	}

	@Test
	public void testGetWorkerNum() {
		assertEquals(workerNum, tfConfig.getWorkerNum());
		tfConfig.setWorkerNum(2);
		assertEquals(2, tfConfig.getWorkerNum());
	}

	@Test
	public void testGetPsNum() {
		assertEquals(psNum, tfConfig.getPsNum());
		tfConfig.setPsNum(3);
		assertEquals(3, tfConfig.getPsNum());
	}

	@Test
	public void testGetProperties() {
		assertEquals(properties, tfConfig.getProperties());
	}

	@Test
	public void testGetFuncName() {
		assertEquals(func, tfConfig.getFuncName());
	}

	@Test
	public void testAddProperties() {
		tfConfig.addProperty("k1", "v1");
		assertEquals("v1", tfConfig.getProperty("k1"));
	}

	@Test
	public void testGetProperty() {
		tfConfig.addProperty("k1", "v1");
		assertEquals("v1", tfConfig.getProperty("k1", "default"));
		assertEquals("default", tfConfig.getProperty("invalid", "default"));
	}

	@Test
	public void testIsWorkerZeroAlone() {
		assertFalse(tfConfig.isWorkerZeroAlone());
		tfConfig.getProperties().put(TFConstants.TF_IS_CHIEF_ALONE, "true");
		assertTrue(tfConfig.isWorkerZeroAlone());
	}


	@Test
	public void testIsChiefRole() {
		assertFalse(tfConfig.isChiefRole());
		tfConfig.getProperties().put(TFConstants.TF_IS_CHIEF_ROLE, "true");
		assertTrue(tfConfig.isChiefRole());
	}

	@Test
	public void testGetMlConfig() {
		final MLConfig mlConfig = tfConfig.getMlConfig();
		System.out.println(mlConfig);
		assertEquals(envPath, mlConfig.getEnvPath());
		assertEquals(func, mlConfig.getFuncName());
		assertEquals(1, mlConfig.getPythonFiles().length);
		assertEquals(pythonFile, mlConfig.getPythonFiles()[0]);
		assertEquals(properties, mlConfig.getProperties());
	}

}