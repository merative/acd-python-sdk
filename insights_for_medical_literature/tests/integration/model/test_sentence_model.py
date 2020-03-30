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

def test_sentence_model():
    sm_model = wh.SentenceModel(document_section='test', text='test', begin=0, end=5, timestamp=0)
    sm_diff = wh.SentenceModel(document_section='test', text='test', begin=1, end=5, timestamp=0)
    sm_same = wh.SentenceModel(document_section='test', text='test', begin=0, end=5, timestamp=0)

    assert sm_model.__str__() is not None
    assert sm_model.__eq__(sm_same)
    assert sm_model.__ne__(sm_diff)
