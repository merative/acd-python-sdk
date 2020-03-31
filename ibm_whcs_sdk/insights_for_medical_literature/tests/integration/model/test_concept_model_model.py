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

def test_concept_model():
    cm_model = wh.ConceptModel(cui='test', ontology='test', corpora={}, preferred_name='test',
                               alternative_name='test', semantic_type='test', rank=10, hit_count=5,
                               surface_forms=[])
    cm_model_diff = wh.ConceptModel(cui='test', ontology='test', corpora={}, preferred_name='test',
                                    alternative_name='test', semantic_type='test', rank=10, hit_count=15,
                                    surface_forms=[])
    cm_model_same = wh.ConceptModel(cui='test', ontology='test', corpora={}, preferred_name='test',
                                    alternative_name='test', semantic_type='test', rank=10, hit_count=5,
                                    surface_forms=[])
    assert cm_model.__str__()
    assert cm_model.__eq__(cm_model_same)
    assert cm_model.__ne__(cm_model_diff)
