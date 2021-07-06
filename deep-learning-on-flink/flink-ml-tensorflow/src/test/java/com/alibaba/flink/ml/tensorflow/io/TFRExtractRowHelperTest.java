package com.alibaba.flink.ml.tensorflow.io;

import com.alibaba.flink.ml.tensorflow.io.TFRExtractRowHelper.ScalarConverter;
import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.api.java.typeutils.RowTypeInfo;
import org.apache.flink.types.Row;
import org.junit.Test;
import org.tensorflow.example.BytesList;
import org.tensorflow.example.Example;
import org.tensorflow.example.Feature;
import org.tensorflow.example.Features;
import org.tensorflow.example.FloatList;
import org.tensorflow.example.Int64List;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class TFRExtractRowHelperTest {

	@Test
	public void testExtract() throws InvalidProtocolBufferException {

		final RowTypeInfo info = new RowTypeInfo(Types.STRING,
				Types.INT,
				Types.FLOAT,
				Types.PRIMITIVE_ARRAY(Types.INT),
				Types.PRIMITIVE_ARRAY(Types.SHORT),
				Types.PRIMITIVE_ARRAY(Types.LONG),
				Types.PRIMITIVE_ARRAY(Types.BYTE),
				Types.INT,
				Types.INT);
		ScalarConverter[] converter = new ScalarConverter[]{ ScalarConverter.FIRST,
				ScalarConverter.ONE_HOT,
				ScalarConverter.LAST,
				ScalarConverter.FIRST,
				ScalarConverter.FIRST,
				ScalarConverter.FIRST,
				ScalarConverter.LAST,
				ScalarConverter.MIN,
				ScalarConverter.MAX};
		final TFRExtractRowHelper helper = new TFRExtractRowHelper(info, converter);
		final Feature stringFeature = Feature.newBuilder().setBytesList(BytesList.newBuilder()
				.addValue(ByteString.copyFromUtf8("hello1"))
				.addValue(ByteString.copyFromUtf8("hello2")).build())
				.build();
		final Feature intListFeature = Feature.newBuilder().setInt64List(Int64List.newBuilder().addValue(0).addValue(0).addValue(1).build()).build();
		final Feature floatListFeature = Feature.newBuilder().setFloatList(FloatList.newBuilder().addValue(0.1f).addValue(0.2f).build()).build();
		final Features features = Features.newBuilder()
				.putFeature("f0", stringFeature)
				.putFeature("f1", intListFeature)
				.putFeature("f2", floatListFeature)
				.putFeature("f3", intListFeature)
				.putFeature("f4", intListFeature)
				.putFeature("f5", intListFeature)
				.putFeature("f6", stringFeature)
				.putFeature("f7", intListFeature)
				.putFeature("f8", intListFeature)
				.build();
		final Example example = Example.newBuilder().setFeatures(features).build();
		final Row row = helper.extract(example.toByteArray());
		assertEquals("hello1", row.getField(0));
		assertEquals(2, row.getField(1));
		assertEquals(0.2f, row.getField(2));
		assertArrayEquals(new int[]{0, 0, 1}, (int[]) row.getField(3));
		assertArrayEquals(new short[]{0, 0, 1}, (short[]) row.getField(4));
		assertArrayEquals(new long[]{0, 0, 1}, (long[]) row.getField(5));
		assertArrayEquals(new byte[][]{ByteString.copyFromUtf8("hello1").toByteArray(), ByteString.copyFromUtf8("hello2").toByteArray()},
				(byte[][]) row.getField(6));
		assertEquals(0L, row.getField(7));
		assertEquals(1L, row.getField(8));
	}
}