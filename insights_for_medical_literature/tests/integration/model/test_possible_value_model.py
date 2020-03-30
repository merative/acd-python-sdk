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

import watson_health_cognitive_services.insights_for_medical_literature as wh

def test_possible_values():
    poss_value = {}
    poss_value['value'] = 'test'
    poss_value['displayValue'] = 'test'

    possible_value = wh.PossibleValues('test', 'test')
    possible_value_diff = wh.PossibleValues('test', 'exam')
    poss_value_dict = possible_value._from_dict(poss_value)

    assert possible_value.__str__()
    assert possible_value.__eq__(poss_value_dict)
    assert possible_value.__ne__(possible_value_diff)
