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

def test_boolean_concepts():
    concepts = []

    boolean_concepts = wh.BooleanConcepts('test', concepts)
    boolean_concepts_diff = wh.BooleanConcepts('diff', concepts)
    boolean_concepts_same = wh.BooleanConcepts('test', concepts)

    bc_obj = {}
    bc_obj['bool_phrase'] = 'test'
    bc_obj['concepts'] = concepts
    bc_dict = boolean_concepts._from_dict(bc_obj)
    assert bc_dict is not None

    assert boolean_concepts.__str__() is not None
    assert boolean_concepts.__eq__(boolean_concepts_same)
    assert boolean_concepts.__ne__(boolean_concepts_diff)
