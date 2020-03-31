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

def test_returns_model():
    documents = wh.Documents()
    concepts = wh.Concepts()
    passages = wh.Passages()
    attributes = wh.Attributes()
    values = wh.Values()
    ranges = wh.Ranges()
    types = wh.TypesModel()
    typeahead = wh.Typeahead()
    histograms = {}
    aggs = {}
    model = wh.ReturnsModel(documents, concepts, passages, attributes, values, ranges, types,
                            typeahead, histograms, aggs)
    model_diff = wh.ReturnsModel(documents, concepts, passages, attributes, values, ranges, types,
                                 None, histograms, aggs)

    returns_obj = {}
    returns_obj['documents'] = {}
    returns_obj['concepts'] = {}
    returns_obj['passages'] = {}
    returns_obj['attributes'] = {}
    returns_obj['values'] = {}
    returns_obj['ranges'] = {}
    returns_obj['types'] = {}
    returns_obj['typeahead'] = {}
    returns_obj['dateHistograms'] = histograms
    returns_obj['aggregations'] = aggs
    returns = model._from_dict(returns_obj)

    assert model.__str__() is not None
    assert model.__eq__(returns)
    assert model.__ne__(model_diff)
