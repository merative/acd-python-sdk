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
IAMURL = CONFIG.get('settings', 'iam_url')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')
DOC = CONFIG.get('document', 'doc_id')
SEMTYPE = CONFIG.get('document', 'sem_type')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

INPUT_CATEGORIES = []
CATEGORY_TYPES = []
CATEGORY_TYPES.append(SEMTYPE)
CATEGORY = wh.Category(name=SEMTYPE, types=CATEGORY_TYPES)
INPUT_CATEGORIES.append(CATEGORY)

def test_multiple_categories():
    response = IML_TEST.get_doc_multiple_categories(corpus=CORPUS, document_id=DOC, categories=INPUT_CATEGORIES)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None

def test_multiple_categories_tags():
    response = IML_TEST.get_doc_multiple_categories(corpus=CORPUS, document_id=DOC, categories=INPUT_CATEGORIES,
                                                    highlight_tag_begin='<i>', highlight_tag_end='</i>')
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None

def test_multiple_categories_fields():
    fields = []
    fields.append('annotations')
    response = IML_TEST.get_doc_multiple_categories(corpus=CORPUS, document_id=DOC,
                                                    categories=INPUT_CATEGORIES, fields=fields)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None

def test_multiple_categories_limit():
    response = IML_TEST.get_doc_multiple_categories(corpus=CORPUS, document_id=DOC,
                                                    categories=INPUT_CATEGORIES, limit=5)
    categories = wh.CategoriesModel._from_dict(response.get_result())
    assert categories is not None

def test_mult_categories_no_corpus():
    try:
        IML_TEST.get_doc_multiple_categories(None, document_id=DOC, categories=INPUT_CATEGORIES, limit=5)
    except ValueError as exp:
        assert exp is not None

def test_multiple_categories_no_id():
    try:
        IML_TEST.get_doc_multiple_categories(CORPUS, document_id=None, categories=INPUT_CATEGORIES, limit=5)
    except ValueError as exp:
        assert exp is not None
