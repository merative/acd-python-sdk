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

def test_range():
    date_range = wh.Range(begin='2008', end='2020')
    date_range_diff = wh.Range(begin='2008', end='2021')

    range_obj = {}
    range_obj['begin'] = '2008'
    range_obj['end'] = '2020'
    range_dict = date_range._from_dict(range_obj)

    assert date_range.__str__() is not None
    assert date_range.__eq__(range_dict)
    assert date_range.__ne__(date_range_diff)
