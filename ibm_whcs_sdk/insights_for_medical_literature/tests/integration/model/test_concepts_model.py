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

def test_concepts_model():
    types = []

    concepts = wh.Concepts(ontology='test', limit=5, scope='test', types=types, mode='test')
    concepts_diff = wh.Concepts(ontology='test', limit=5, scope='exam', types=types, mode='test')
    concepts_same = wh.Concepts(ontology='test', limit=5, scope='test', types=types, mode='test')

    conncepts_obj = {}
    conncepts_obj['ontology'] = 'test'
    conncepts_obj['limit'] = 5
    conncepts_obj['scope'] = 'test'
    conncepts_obj['types'] = types
    conncepts_obj['mode'] = 'test'

    concepts_dict = concepts._from_dict(conncepts_obj)
    assert concepts_dict is not None

    assert concepts.__str__() is not None
    assert concepts.__eq__(concepts_same)
    assert concepts.__ne__(concepts_diff)
