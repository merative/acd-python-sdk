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

def test_search_model():
    concepts = []
    types = []
    attributes = []
    values = []
    ranges = {}
    typeahead = []
    aggregations = {}
    date_histograms = {}
    qualifiers = []
    concepts_exist = {}
    vocabs = []
    docs = []
    sub_queries = []

    model = wh.SearchModel(
        href='test',
        page_number=1,
        get_limit=10,
        total_document_count=100,
        concepts=concepts,
        types=types,
        attributes=attributes,
        values=values,
        ranges=ranges,
        typeahead=typeahead,
        aggregations=aggregations,
        date_histograms=date_histograms,
        qualifiers=qualifiers,
        expanded_query={},
        concepts_exist=concepts_exist,
        bool_concepts=wh.BooleanConcepts(),
        cursor_id='test',
        vocabs=vocabs,
        documents=docs,
        sub_queries=sub_queries
    )

    model_diff = wh.SearchModel(
        href='test',
        page_number=1,
        get_limit=10,
        total_document_count=100,
        concepts=concepts,
        types=types,
        attributes=attributes,
        values=values,
        ranges=ranges,
        typeahead=typeahead,
        aggregations=aggregations,
        date_histograms=date_histograms,
        qualifiers=qualifiers,
        expanded_query={},
        concepts_exist=concepts_exist,
        bool_concepts=wh.BooleanConcepts(),
        cursor_id='exam',
        vocabs=vocabs,
        documents=docs,
        sub_queries=sub_queries
    )

    model_same = wh.SearchModel(
        href='test',
        page_number=1,
        get_limit=10,
        total_document_count=100,
        concepts=concepts,
        types=types,
        attributes=attributes,
        values=values,
        ranges=ranges,
        typeahead=typeahead,
        aggregations=aggregations,
        date_histograms=date_histograms,
        qualifiers=qualifiers,
        expanded_query={},
        concepts_exist=concepts_exist,
        bool_concepts=wh.BooleanConcepts(),
        cursor_id='test',
        vocabs=vocabs,
        documents=docs,
        sub_queries=sub_queries
    )

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
