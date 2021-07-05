package com.alibaba.flink.ml.tensorflow.io;

import com.alibaba.flink.ml.util.FileUtil;
import org.apache.flink.api.common.io.statistics.BaseStatistics;
import org.apache.flink.core.io.InputSplit;
import org.apache.flink.core.io.InputSplitAssigner;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mockito;

import java.io.IOException;
import java.net.URL;
import java.util.Collections;

import static org.junit.Assert.*;

public class TFRecordInputFormatTest {

	private String[] paths;
	private TFRecordInputFormat inputFormat;

	@Before
	public void setUp() throws Exception {
		final URL record0 = FileUtil.class.getClassLoader().getResource("tfrecords/0.tfrecords");
		final URL record1 = FileUtil.class.getClassLoader().getResource("tfrecords/1.tfrecords");
		assertNotNull(record0);
		assertNotNull(record1);
		paths = new String[]{record0.toString(), record1.toString()};
		inputFormat = new TFRecordInputFormat(paths, 1);
	}

	@Test
	public void testCreateInputSplits() throws IOException {
		final TFRecordInputSplit[] inputSplits = inputFormat.createInputSplits(2);
		assertEquals(2, inputSplits.length);
	}

	@Test
	public void testOpen() throws IOException {
		final TFRecordInputSplit[] inputSplits = inputFormat.createInputSplits(2);
		inputFormat.open(inputSplits[0]);
		assertNotNull(inputFormat.getTfRecordReader());
	}

	@Test
	public void testGetStatics() throws IOException {
		assertNull(inputFormat.getStatistics(Mockito.mock(BaseStatistics.class)));
	}

	@Test
	public void testGetInputSplitAssigner() throws IOException {
		final TFRecordInputSplit[] inputSplits = inputFormat.createInputSplits(2);
		final InputSplitAssigner splitAssigner = inputFormat.getInputSplitAssigner(inputSplits);
		assertThat(splitAssigner, org.hamcrest.CoreMatchers.instanceOf(InputSplitAssigner.class));
		final InputSplit split0 = splitAssigner.getNextInputSplit("host1", 0);
		final InputSplit split1 = splitAssigner.getNextInputSplit("host1", 0);
		assertEquals(0, split0.getSplitNumber());
		assertEquals(1, split1.getSplitNumber());
		assertNull(splitAssigner.getNextInputSplit("host1", 0));
		splitAssigner.returnInputSplit(Collections.singletonList(split0), 0);
		assertEquals(split0, splitAssigner.getNextInputSplit("host1", 0));
	}

	@Test
	public void testNextRecord() throws IOException {
		final TFRecordInputSplit[] inputSplits = inputFormat.createInputSplits(2);
		inputFormat.open(inputSplits[0]);
		assertNotNull(inputFormat.getTfRecordReader());
		int recordsCnt = 0;
		while(true) {
			final byte[] record = inputFormat.nextRecord(new byte[0]);
			if (record == null) {
				break;
			}
			recordsCnt++;
		}
		inputFormat.close();
		assertTrue(inputFormat.reachedEnd());
		assertEquals(5000, recordsCnt);
	}
}