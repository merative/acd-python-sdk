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
SEMTYPE = CONFIG.get('document', 'sem_type')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_categories_default():
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_title is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_custom_tags():
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, highlight_tag_begin='<i>',
                                                highlight_tag_end='</i>')
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_title is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_types_filter():
    types = []
    types.append(SEMTYPE)
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, types=types)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_abstract is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_category_filter():
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, category='disorders')
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_title is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_negation_only():
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, only_negated_concepts=True)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_fields_filter():
    fields = []
    fields.append('annotations')
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, fields=fields)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_title is None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_categories_limit_filter():
    response = IML_TEST.get_document_categories(corpus=CORPUS, document_id=DOC, limit=5)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None
    assert categories.highlighted_title is not None
    assert categories.passages is not None
    assert categories.annotations is not None

def test_get_categories_no_corpus():
    try:
        IML_TEST.get_document_categories(None, document_id=DOC, limit=5)
    except ValueError as exp:
        assert exp is not None

def test_get_categories_no_id():
    try:
        IML_TEST.get_document_categories(CORPUS, document_id=None, limit=5)
    except ValueError as exp:
        assert exp is not None
