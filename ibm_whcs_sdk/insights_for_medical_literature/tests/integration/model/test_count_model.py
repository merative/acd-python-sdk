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

def test_count_model():
    model = wh.Count(50, 30)
    model_diff = wh.Count(50, 20)

    count_obj = {}
    count_obj['count'] = 50
    count_obj['hits'] = 30
    count = model._from_dict(count_obj)

    assert model.__str__()
    assert model.__eq__(count)
    assert model.__ne__(model_diff)
