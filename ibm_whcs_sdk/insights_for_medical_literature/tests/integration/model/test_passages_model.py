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

def test_passages():
    concepts = []
    passages_obj = {}
    passages_obj['conceptsToHighlight'] = concepts
    passages_obj['searchTagBegin'] = 'test'
    passages_obj['searchTagEnd'] = 'test'
    passages_obj['relatedTagBegin'] = 'test'
    passages_obj['relatedTagEnd'] = 'test'
    passages_obj['limit'] = 10
    passages_obj['minScore'] = 0.6

    passages = wh.Passages(concepts, 'test', 'test', 'test', 'test', 10, 0.6)
    passages_same = wh.Passages(concepts, 'test', 'test', 'test', 'test', 10, 0.6)
    passages_diff = wh.Passages(concepts, 'test', 'test', 'test', 'test', 10, 0.7)
    passages_dict = passages._from_dict(passages_obj)

    assert passages_dict.__str__()
    assert passages.__eq__(passages_dict)
    assert passages.__ne__(passages_diff)
