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
import configparser
import ibm_whcs_sdk.insights_for_medical_literature as wh

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/insights_for_medical_literature/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')
CUI = CONFIG.get('search', 'search_cui')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_related_children():
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children')
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    assert related_concepts is not None

def test_get_related_attr_filter():
    rel_attrs = []
    rel_attrs.append('part_of')
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children',
                                             relationship_attributes=rel_attrs)
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    related_concept_list = related_concepts.concepts
    assert related_concept_list is not None

def test_get_related_vocab_filter():
    vocabs = []
    vocabs.append('AIR')
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children',
                                             sources=vocabs)
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    related_concept_list = related_concepts.concepts
    assert related_concept_list is not None

def test_get_related_recursive():
    vocabs = []
    vocabs.append('AIR')
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children',
                                             sources=vocabs, recursive=True)
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    related_concept_list = related_concepts.concepts
    assert related_concept_list is not None

def test_get_related_no_tree_layout():
    vocabs = []
    vocabs.append('AIR')
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children',
                                             sources=vocabs, tree_layout=True)
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    related_concept_list = related_concepts.concepts
    assert related_concept_list is not None

def test_get_related_limited_depth():
    vocabs = []
    vocabs.append('AIR')
    response = IML_TEST.get_related_concepts(CORPUS, name_or_id='C0243026', relationship='children',
                                             sources=vocabs, max_depth=2)
    related_concepts = wh.RelatedConceptsModel._from_dict(response.get_result())
    related_concept_list = related_concepts.concepts
    assert related_concept_list is not None

def test_get_related_no_corpus():
    try:
        IML_TEST.get_related_concepts(None, CUI, relationship='children')
    except ValueError as exp:
        assert exp is not None

def test_get_related_no_concept():
    try:
        IML_TEST.get_related_concepts(CORPUS, None, relationship='children')
    except ValueError as exp:
        assert exp is not None

def test_get_related_no_relation():
    try:
        IML_TEST.get_related_concepts(CORPUS, CUI, relationship=None)
    except ValueError as exp:
        assert exp is not None
