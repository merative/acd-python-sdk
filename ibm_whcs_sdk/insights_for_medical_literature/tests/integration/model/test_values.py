# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ibm_whcs_sdk.insights_for_medical_literature as wh

def test_values():
    values = {}
    values['attributeId'] = 'test'
    values['unit'] = 'test'
    values['scope'] = 'test'
    values_obj = wh.Values()
    values1 = {}
    values1['attributeId'] = 'test'
    values1['unit'] = 'tester'
    values1['scope'] = 'test'
    values1_obj = wh.Values()
    model = values_obj._from_dict(values)
    model_diff = values1_obj._from_dict(values1)
    model_same = values_obj._from_dict(values)

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
