#  Copyright 2022 Deep Learning on Flink Authors
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pyflink.stream.functions.source import JavaSourceFunction
from pyflink.util.type_util import TypesUtil


class TFRSourceFunc(JavaSourceFunction):
    def __init__(self, paths, epochs, out_row_type, converters):
        src_func_clz_name = 'org.flinkextended.flink.tensorflow.hadoop.io.TFRToRowSourceFunc'
        src_func_clz = TypesUtil.class_for_name(src_func_clz_name)
        j_paths = TypesUtil._convert_py_list_to_java_array('java.lang.String', paths)
        j_converters = []
        for converter in converters:
            j_converters.append(converter.java_converter())
        j_converters = TypesUtil._convert_py_list_to_java_array(
            'org.flinkextended.flink.tensorflow.hadoop.io.TFRExtractRowHelper$ScalarConverter', j_converters)
        j_row_type = TypesUtil.to_java_sql_type(out_row_type)
        super(TFRSourceFunc, self).__init__(src_func_clz(j_paths, epochs, j_row_type, j_converters))
