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

def test_documents_model():
    metadata = {}
    sort_entries = []
    order = wh.Order('DESC')
    sort = wh.SortEntry('publishDate', order)
    sort_entries.append(sort)
    model = wh.Documents(5, 0, metadata)
    model_diff = wh.Documents(5, 1, metadata)
    model_same = wh.Documents(5, 0, metadata)

    document_obj = {}
    document_obj['limit'] = 5
    document_obj['offset'] = 0
    document_obj['metadata'] = {}
    document_obj['sortEntry'] = sort_entries
    document = model._from_dict(document_obj)
    assert model.__eq__(document)

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
