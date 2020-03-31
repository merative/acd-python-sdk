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


def test_passage():
    passage = wh.Passage(document_section='test', text='test', timestamp=0)
    passage_diff = wh.Passage(document_section='test', text='test', timestamp=1)
    passage_same = wh.Passage(document_section='test', text='test', timestamp=0)

    assert passage.__str__()
    assert passage.__eq__(passage_same)
    assert passage.__ne__(passage_diff)
