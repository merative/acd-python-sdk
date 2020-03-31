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
ONTOLOGY = CONFIG.get('search', 'umls')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_similar_umls():
    response = IML_TEST.get_similar_concepts(CORPUS, name_or_id=CUI, return_ontologies=ONTOLOGY)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_similar_umls_limit():
    response = IML_TEST.get_similar_concepts(CORPUS, name_or_id=CUI, ontology=ONTOLOGY,
                                             return_ontologies=ONTOLOGY, limit=2)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_similar_mesh():
    ontologies = []
    ontologies.append('mesh')
    response = IML_TEST.get_similar_concepts(CORPUS, name_or_id=CUI, ontology=ONTOLOGY,
                                             return_ontologies=ontologies)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology == ontologies[0]
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_similar_no_corpus():
    try:
        IML_TEST.get_similar_concepts(None, CUI)
    except ValueError as exp:
        assert exp is not None

def test_get_similar_no_concept():
    try:
        IML_TEST.get_similar_concepts(CORPUS, None)
    except ValueError as exp:
        assert exp is not None
