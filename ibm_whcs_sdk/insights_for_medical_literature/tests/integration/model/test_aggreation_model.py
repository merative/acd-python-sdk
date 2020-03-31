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

def test_aggregation_model():
    aggregation1 = wh.AggregationModel(name='gizmos', document_count=10)
    aggregation2 = wh.AggregationModel(name='gadgets', document_count=15)
    aggregation3 = wh.AggregationModel(name='gizmos', document_count=10)

    assert aggregation1._to_dict() is not None
    assert aggregation1.__str__() is not None
    assert aggregation1.__ne__(aggregation2)
    assert aggregation1.__eq__(aggregation3)
