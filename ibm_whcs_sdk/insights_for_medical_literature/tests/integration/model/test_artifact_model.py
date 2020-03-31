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


def test_artifact_model():
    synonyms = []
    synonyms.append('test')

    model = wh.ArtifactModel(
        cui='test',
        ontology='test',
        preferred_name='test',
        alternative_name='test',
        type='test',
        rank=10,
        hit_count=10,
        score=0.9,
        surface_forms=synonyms
    )

    model_diff = wh.ArtifactModel(
        cui='test',
        ontology='test',
        preferred_name='test',
        alternative_name='test',
        type='test',
        rank=10,
        hit_count=10,
        score=0.9,
        surface_forms=None
    )

    model_same = wh.ArtifactModel(
        cui='test',
        ontology='test',
        preferred_name='test',
        alternative_name='test',
        type='test',
        rank=10,
        hit_count=10,
        score=0.9,
        surface_forms=synonyms
    )

    model_obj = {}
    model_obj['cui'] = 'test'
    model_obj['ontology'] = 'test'
    model_obj['preferredName'] = ' test'
    model_obj['alternativeName'] = 'test'
    model_obj['type'] = 'test'
    model_obj['rank'] = 10
    model_obj['hit_count'] = 10
    model_obj['score'] = 0.9
    model_obj['surfaceForms'] = synonyms
    model_dict = model._from_dict(model_obj)
    assert model_dict is not None

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
