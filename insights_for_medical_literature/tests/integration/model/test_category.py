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

def test_category():
    types = []
    types.append('test')

    category = wh.Category(name='test', types=types, category='test', only_negated_concepts=False)
    category_diff = wh.Category(name='test', types=types, category='test', only_negated_concepts=True)
    category_same = wh.Category(name='test', types=types, category='test', only_negated_concepts=False)

    category_obj = {}
    category_obj['name'] = 'test'
    category_obj['types'] = types
    category_obj['category'] = 'test'
    category_obj['onlyNegatedConcepts'] = False
    category_dict = category._from_dict(category_obj)
    assert category_dict is not None

    assert category.__str__() is not None
    assert category.__eq__(category_same)
    assert category.__ne__(category_diff)
