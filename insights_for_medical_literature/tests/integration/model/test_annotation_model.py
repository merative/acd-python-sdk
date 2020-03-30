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

def test_annotation_model():
    sticky_ids = []
    sticky_ids.append(99)
    qualifiers = []
    qualifiers.append('test')
    features = {}
    features['f1'] = 'test'

    model = wh.AnnotationModel(
        unique_id=1,
        sticky_ids=sticky_ids,
        ontology='test',
        section='test',
        preferred_name='test',
        cui='test',
        attribute_id='test',
        qualifiers=qualifiers,
        type='test',
        negated=False,
        hypothetical=True,
        unit='test',
        min_value='test',
        max_value='test',
        operator='test',
        nlu_source_type='test',
        nlu_relation='test',
        nlu_target_type='test',
        nlu_entity_index='test',
        nlu_mention_index='test',
        nlu_relation_id='test',
        nlu_side='test',
        begin=0,
        end=3,
        score=0.5,
        timestamp=0,
        features=features,
        hits=5
    )

    model_diff = wh.AnnotationModel(
        unique_id=1,
        sticky_ids=sticky_ids,
        ontology='test',
        section='test',
        preferred_name='test',
        cui='test',
        hits=5
    )

    model_same = wh.AnnotationModel(
        unique_id=1,
        sticky_ids=sticky_ids,
        ontology='test',
        section='test',
        preferred_name='test',
        cui='test',
        hits=5
    )

    assert model._to_dict is not None
    assert model.__str__() is not None
    assert model_diff.__eq__(model_same)
    assert model.__ne__(model_diff)
