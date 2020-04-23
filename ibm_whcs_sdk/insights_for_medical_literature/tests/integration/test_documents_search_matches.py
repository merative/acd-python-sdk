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
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/insights_for_medical_literature/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')
DOC = CONFIG.get('document', 'doc_id')
CUI = CONFIG.get('document', 'cui')
SEMTYPE = CONFIG.get('document', 'sem_type')
ATTR = CONFIG.get('document', 'attribute_id')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_get_search_matches():
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5')
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_earch_matches_cuis():
    cuis = []
    cuis.append(CUI)
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           cuis=cuis)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.negated is None
        assert model.hypothetical is None
        assert model.nlu_source_type is None
        assert model.nlu_relation is None
        assert model.nlu_target_type is None
        assert model.nlu_entity_index is None
        assert model.nlu_mention_index is None
        assert model.nlu_relation_id is None
        assert model.nlu_side is None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_search_matches_text():
    keywords = []
    keywords.append('organisms')
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5', text=keywords)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is None
        assert model.type is None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_search_matches_types():
    types_filter = []
    types_filter.append(SEMTYPE)
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           types=types_filter)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_search_matches_attrs():
    attributes = []
    attributes.append(ATTR)
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           attributes=attributes)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.attribute_id is not None
        assert model.min_value is not None
        assert model.max_value is not None
        assert model.operator is None
        assert model.unit is None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_search_matches_values():
    values = []
    values.append('age_group:child')
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           values=values)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_search_matches_limit():
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5', limit=5)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > -1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_matches_search_tags():
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           search_tag_begin='<u>', search_tag_end='</u>')
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > 1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_matches_related_tags():
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5',
                                           related_tag_begin='<p>', related_tag_end='</p>')
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > 1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get__matches_fields_filter():
    fields = []
    fields.append('highlightedTitle')
    response = IML_TEST.get_search_matches(corpus=CORPUS, document_id=DOC, min_score='0.5', fields=fields)
    search_match = wh.SearchMatchesModel._from_dict(response.get_result())
    assert search_match.document_id == DOC
    assert search_match.title is not None
    assert search_match.passages is not None
    passages_map = search_match.passages
    for key in passages_map:
        passage_map = passages_map[key]
        for passage_key in passage_map:
            entry_model = wh.EntryModel()
            model = entry_model._from_dict(passage_map[passage_key])
            sentences = model.sentences
            for sentence in sentences:
                assert sentence.begin > 1
                assert sentence.end > sentence.begin
                assert sentence.document_section is not None
                assert sentence.text is not None
                assert sentence.timestamp == 0
    assert search_match.annotations is not None
    annotations_map = search_match.annotations
    for key in annotations_map:
        model = annotations_map[key]
        assert model.unique_id is not None
        assert model.sticky_ids is not None
        assert model.ontology is not None
        assert model.section is not None
        assert model.preferred_name is not None
        assert model.cui is not None
        assert model.type is not None
        assert model.begin > -1
        assert model.end > model.begin
        assert model.timestamp == 0
        assert model.hits > -1

def test_get_matches_no_corpus():
    try:
        IML_TEST.get_search_matches(None, document_id=DOC, min_score='0.5')
    except ValueError as exp:
        assert exp is not None

def test_get_search_matches_no_id():
    try:
        IML_TEST.get_search_matches(CORPUS, document_id=None, min_score='0.5')
    except ValueError as exp:
        assert exp is not None

def test_get_matches_no_score():
    try:
        IML_TEST.get_search_matches(CORPUS, document_id=DOC, min_score=None)
    except ValueError as exp:
        assert exp is not None
