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

package org.flinkextended.flink.ml.tensorflow.util;

import org.flinkextended.flink.ml.operator.util.DataTypes;
import org.flinkextended.flink.ml.tensorflow.client.TFConfigBase;
import org.flinkextended.flink.ml.tensorflow.coding.ExampleCoding;
import org.flinkextended.flink.ml.tensorflow.coding.ExampleCodingConfig;
import org.flinkextended.flink.ml.util.MLConstants;

import org.apache.flink.api.common.typeinfo.BasicArrayTypeInfo;
import org.apache.flink.api.common.typeinfo.BasicTypeInfo;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.table.api.TableSchema;
import org.apache.flink.types.Row;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Arrays;

/**
 * Util class which provide methods to configure example coding and methods to convert DataTypes and
 * TypeInformation.
 *
 * <p>Configuration example as below:
 *
 * <pre>{@code
 * ExampleCodingConfigUtil.configureExampleCoding(
 *      tfConfig, inputSchema, outputSchema);
 *
 * }</pre>
 */
public class ExampleCodingConfigUtil {
    private static final Logger LOG = LoggerFactory.getLogger(ExampleCodingConfigUtil.class);

    /**
     * Convert DataTypes list to TypeInformation list.
     *
     * @throws RuntimeException when meet unsupported type of DataTypes
     */
    public static TypeInformation[] dataTypesListToTypeInformation(DataTypes[] dataTypes) {
        return Arrays.stream(dataTypes)
                .map(ExampleCodingConfigUtil::dataTypesToTypeInformation)
                .toArray(TypeInformation[]::new);
    }

    /**
     * Map DataTypes class to TypeInformation.
     *
     * @throws RuntimeException when meet unsupported type of DataTypes
     */
    public static TypeInformation dataTypesToTypeInformation(DataTypes dataTypes) {
        if (dataTypes == null) {
            return null;
        } else if (dataTypes == DataTypes.STRING) {
            return BasicTypeInfo.STRING_TYPE_INFO;
        } else if (dataTypes == DataTypes.BOOL) {
            return BasicTypeInfo.BOOLEAN_TYPE_INFO;
        } else if (dataTypes == DataTypes.INT_8) {
            return BasicTypeInfo.BYTE_TYPE_INFO;
        } else if (dataTypes == DataTypes.INT_16) {
            return BasicTypeInfo.SHORT_TYPE_INFO;
        } else if (dataTypes == DataTypes.INT_32) {
            return BasicTypeInfo.INT_TYPE_INFO;
        } else if (dataTypes == DataTypes.INT_64) {
            return BasicTypeInfo.LONG_TYPE_INFO;
        } else if (dataTypes == DataTypes.FLOAT_32) {
            return BasicTypeInfo.FLOAT_TYPE_INFO;
        } else if (dataTypes == DataTypes.FLOAT_64) {
            return BasicTypeInfo.DOUBLE_TYPE_INFO;
        } else if (dataTypes == DataTypes.UINT_16) {
            return BasicTypeInfo.CHAR_TYPE_INFO;
        } else if (dataTypes == DataTypes.FLOAT_32_ARRAY) {
            return BasicArrayTypeInfo.FLOAT_ARRAY_TYPE_INFO;
        } else {
            throw new RuntimeException("Unsupported data type of " + dataTypes.toString());
        }
    }

    /**
     * Convert TypeInformation list to DataTypes list.
     *
     * @throws RuntimeException when meet unsupported type of TypeInformation
     */
    public static DataTypes[] typeInormationListToDataTypes(TypeInformation[] typeInformation) {
        return Arrays.stream(typeInformation)
                .map(ExampleCodingConfigUtil::typeInformationToDataTypes)
                .toArray(DataTypes[]::new);
    }

    /**
     * Map TypeInformation class to DataTypes.
     *
     * @throws RuntimeException when meet unsupported type of TypeInformation
     */
    public static DataTypes typeInformationToDataTypes(TypeInformation typeInformation) {
        if (typeInformation == null) {
            return null;
        } else if (typeInformation == BasicTypeInfo.STRING_TYPE_INFO) {
            return DataTypes.STRING;
        } else if (typeInformation == BasicTypeInfo.BOOLEAN_TYPE_INFO) {
            return DataTypes.BOOL;
        } else if (typeInformation == BasicTypeInfo.BYTE_TYPE_INFO) {
            return DataTypes.INT_8;
        } else if (typeInformation == BasicTypeInfo.SHORT_TYPE_INFO) {
            return DataTypes.INT_16;
        } else if (typeInformation == BasicTypeInfo.INT_TYPE_INFO) {
            return DataTypes.INT_32;
        } else if (typeInformation == BasicTypeInfo.LONG_TYPE_INFO) {
            return DataTypes.INT_64;
        } else if (typeInformation == BasicTypeInfo.FLOAT_TYPE_INFO) {
            return DataTypes.FLOAT_32;
        } else if (typeInformation == BasicTypeInfo.DOUBLE_TYPE_INFO) {
            return DataTypes.FLOAT_64;
        } else if (typeInformation == BasicTypeInfo.CHAR_TYPE_INFO) {
            return DataTypes.UINT_16;
        } else if (typeInformation == BasicArrayTypeInfo.FLOAT_ARRAY_TYPE_INFO) {
            return DataTypes.FLOAT_32_ARRAY;
        } else {
            throw new RuntimeException("Unsupported data type of " + typeInformation.toString());
        }
    }

    /**
     * Configuration for example encoding via encodeNames and encodeTypes.
     *
     * @param config the config instance to configuration
     * @param encodeNames field names
     * @param encodeTypes field types
     * @param entryType ObjectType for each entry
     * @param entryClass java object class for each entry
     */
    public static void configureEncodeExampleCoding(
            TFConfigBase config,
            String[] encodeNames,
            DataTypes[] encodeTypes,
            ExampleCodingConfig.ObjectType entryType,
            Class entryClass) {
        String strInput =
                ExampleCodingConfig.createExampleConfigStr(
                        encodeNames, encodeTypes, entryType, entryClass);
        LOG.info("input tf example config: " + strInput);
        config.getProperties().put(TFConstants.INPUT_TF_EXAMPLE_CONFIG, strInput);
        config.getProperties()
                .put(MLConstants.ENCODING_CLASS, ExampleCoding.class.getCanonicalName());
    }

    /**
     * Configuration for example decoding via decodeNames and decodeTypes.
     *
     * @param config the config instance to configuration
     * @param decodeNames field names
     * @param decodeTypes field types
     * @param entryType ObjectType for each entry
     * @param entryClass java object class for each entry
     */
    public static void configureDecodeExampleCoding(
            TFConfigBase config,
            String[] decodeNames,
            DataTypes[] decodeTypes,
            ExampleCodingConfig.ObjectType entryType,
            Class entryClass) {
        String strOutput =
                ExampleCodingConfig.createExampleConfigStr(
                        decodeNames, decodeTypes, entryType, entryClass);
        LOG.info("output tf example config: " + strOutput);
        config.getProperties().put(TFConstants.OUTPUT_TF_EXAMPLE_CONFIG, strOutput);
        config.getProperties()
                .put(MLConstants.DECODING_CLASS, ExampleCoding.class.getCanonicalName());
    }

    /**
     * Configuration for example encoding via encodeNames and encodeTypes.
     *
     * @param config the config instance to configuration
     * @param encodeNames field names
     * @param encodeTypes field types
     * @param entryType ObjectType for each entry
     * @param entryClass java object class for each entry
     */
    public static void configureEncodeExampleCoding(
            TFConfigBase config,
            String[] encodeNames,
            TypeInformation[] encodeTypes,
            ExampleCodingConfig.ObjectType entryType,
            Class entryClass) {
        DataTypes[] encodeDataTypes =
                Arrays.stream(encodeTypes)
                        .map(ExampleCodingConfigUtil::typeInformationToDataTypes)
                        .toArray(DataTypes[]::new);
        configureEncodeExampleCoding(config, encodeNames, encodeDataTypes, entryType, entryClass);
    }

    /**
     * Configuration for example decoding via decodeNames and decodeTypes.
     *
     * @param config the config instance to configuration
     * @param decodeNames field names
     * @param decodeTypes field types
     * @param entryType ObjectType for each entry
     * @param entryClass java object class for each entry
     */
    public static void configureDecodeExampleCoding(
            TFConfigBase config,
            String[] decodeNames,
            TypeInformation[] decodeTypes,
            ExampleCodingConfig.ObjectType entryType,
            Class entryClass) {
        DataTypes[] decodeDataTypes =
                Arrays.stream(decodeTypes)
                        .map(ExampleCodingConfigUtil::typeInformationToDataTypes)
                        .toArray(DataTypes[]::new);
        configureDecodeExampleCoding(config, decodeNames, decodeDataTypes, entryType, entryClass);
    }

    /**
     * Automatic configuration for example coding via encodeSchema and decodeSchema, one of them can
     * be null.
     *
     * @param config the config instance to configuration
     * @param encodeSchema the schema of input table whose fields need to be encoded to python
     * @param decodeSchema the schema of output table whose fields need to be decoded from python
     * @param entryType ObjectType for each entry
     * @param entryClass java object class for each entry
     */
    public static void configureExampleCoding(
            TFConfigBase config,
            TableSchema encodeSchema,
            TableSchema decodeSchema,
            ExampleCodingConfig.ObjectType entryType,
            Class entryClass) {
        if (encodeSchema != null) {
            configureEncodeExampleCoding(
                    config,
                    encodeSchema.getFieldNames(),
                    encodeSchema.getFieldTypes(),
                    entryType,
                    entryClass);
        }
        if (decodeSchema != null) {
            configureDecodeExampleCoding(
                    config,
                    decodeSchema.getFieldNames(),
                    decodeSchema.getFieldTypes(),
                    entryType,
                    entryClass);
        }
    }

    /**
     * Automatic configuration for example coding via encodeSchema and decodeSchema, one of them can
     * be null.
     *
     * @param config the config instance to configuration
     * @param encodeSchema the schema of input table whose fields need to be encoded to python
     * @param decodeSchema the schema of output table whose fields need to be decoded from python
     */
    public static void configureExampleCoding(
            TFConfigBase config, TableSchema encodeSchema, TableSchema decodeSchema) {
        configureExampleCoding(
                config, encodeSchema, decodeSchema, ExampleCodingConfig.ObjectType.ROW, Row.class);
    }
}
