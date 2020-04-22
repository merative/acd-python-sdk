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
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')
CUI = CONFIG.get('search', 'search_cui')
SEMTYPE = CONFIG.get('search', 'search_sem_type')
ONTOLOGY = CONFIG.get('search', 'umls')
BOOL_PHRASE = CONFIG.get('search', 'boolean_phrase')
RANGE_FIELD = CONFIG.get('search', 'range_field')
RANGE_BEGIN = CONFIG.get('search', 'range_begin')
RANGE_END = CONFIG.get('search', 'range_end')
BOOLEAN_REGEX = CONFIG.get('search', 'boolean_regex')
REGEX_FIELD = CONFIG.get('search', 'field_regex_name')
REGEX = CONFIG.get('search', 'field_regex')
TERM_FIELD = CONFIG.get('search', 'term_field_name')
TERM_VALUE = CONFIG.get('search', 'term_field_value')
SORT_FIELD = CONFIG.get('search', 'sort_field')
ATTRIBUTE = CONFIG.get('search', 'attribute')
SECOND_CUI = CONFIG.get('search', 'second_cui')
SECOND_SEMTYPE = CONFIG.get('search', 'second_sem_type')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)
VALID_LIMIT = 10

def test_search_single_concept():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(concepts=concepts)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

#def test_search_scrolling():
#    concepts = []
#    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
#                                          semanticType=SEMTYPE)
#    concepts.append(search_concept)
#    query = wh.Query(concepts=concepts)
#
#   returns = wh.ReturnsModel(documents)
#    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
#    search_model = wh.SearchModel._from_dict(response.get_result())
#    cursor_id = search_model.cursor_id
#    assert cursor_id is not None
#    query = wh.Query(concepts=concepts, cursorId=cursor_id)
#    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
#    search_model = wh.SearchModel._from_dict(response.get_result())
#    result_documents = search_model.documents
#    for ranked_doc in result_documents:
#        assert ranked_doc.document_id is not None
#        assert ranked_doc.links is not None
#        doc_links = ranked_doc.links
#        assert doc_links.href_search_matches is not None
#        assert doc_links.href_categories is not None

def test_search_ranked_search():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(concepts=concepts, rankedSearch=True)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_multiple_concepts():
    concepts = []
    search_concept1 = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                           semanticType=SEMTYPE)
    concepts.append(search_concept1)
    search_concept2 = wh.SearchableConcept(cui=SECOND_CUI, ontology=ONTOLOGY, rank='10',
                                           semanticType=SECOND_SEMTYPE)
    concepts.append(search_concept2)
    query = wh.Query(concepts=concepts)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_boolean_phrase():
    concepts = []
    phrase = BOOL_PHRASE
    query = wh.Query(boolExpression=phrase, concepts=concepts)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_keyword():
    phrase = 'COPD AND (smoker OR smoking)'
    operands = []
    copd_operand = {}
    copd_operand['ontology'] = 'text'
    copd_operand['boolOperand'] = 'COPD'
    copd_operand['text'] = 'COPD'
    operands.append(copd_operand)
    smoker_operand = {}
    smoker_operand['ontology'] = 'text'
    smoker_operand['boolOperand'] = 'smoker'
    smoker_operand['text'] = 'smoker'
    operands.append(smoker_operand)
    smoking_operand = {}
    smoking_operand['ontology'] = 'text'
    smoking_operand['boolOperand'] = 'smoking'
    smoking_operand['text'] = 'smoking'
    operands.append(smoking_operand)
    query = wh.Query(boolExpression=phrase, concepts=operands)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_date_range():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    date_range = wh.Range(begin=RANGE_BEGIN, end=RANGE_END)
    range_map = {}
    range_map[RANGE_FIELD] = date_range
    query = wh.Query(concepts=concepts, date_range=range_map)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_bool_regexp():
    bool_regexp = {}
    bool_regexp['title'] = BOOLEAN_REGEX
    query = wh.Query(boolRegexp=bool_regexp)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_regexp():
    regexps = []
    regexp = {}
    regexp[REGEX_FIELD] = REGEX
    regexps.append(regexp)
    query = wh.Query(regexp=regexps)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_bool_term():
    concepts = []
    bool_term = {}
    bool_term[TERM_FIELD] = TERM_VALUE
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    date_range = wh.Range(begin=RANGE_BEGIN, end=RANGE_END)
    range_map = {}
    range_map[RANGE_FIELD] = date_range
    query = wh.Query(concepts=concepts, date_range=range_map, boolTerm=bool_term)
    documents = wh.Documents("10", "0")
    returns = wh.ReturnsModel(documents)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None

def test_search_sorted_results():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(concepts=concepts)
    metadata = []
    metadata.append("abstract")
    metadata.append(SORT_FIELD)
    sort_entries = []
    order = wh.Order('ASC')
    sort = wh.SortEntry(SORT_FIELD, order)
    sort_entries.append(sort)
    documents = wh.Documents("10", "0", metadata, None, sort=sort_entries)
    returns = wh.ReturnsModel(documents)
#    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
#    search_model = wh.SearchModel._from_dict(response.get_result())
#    result_documents = search_model.documents
#    for ranked_doc in result_documents:
#        assert ranked_doc.document_id is not None
#        assert ranked_doc.metadata is not None
#        for key in ranked_doc.metadata:
#            assert key is not None
#            assert ranked_doc.metadata[key] is not None
#        assert ranked_doc.corpus == CORPUS
#        assert ranked_doc.links is not None
#        doc_links = ranked_doc.links
#        assert doc_links.href_search_matches is not None
#        assert doc_links.href_categories is not None

def test_search_returns_concepts():
    title = wh.Title(0)
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(title=title, concepts=concepts)
    cooccurring_concepts = wh.Concepts(ONTOLOGY, 20)
    returns = wh.ReturnsModel(None, cooccurring_concepts)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_concepts = search_model.concepts
    for concept in result_concepts:
        assert concept.cui is not None

def test_returns_date_histogram():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(concepts=concepts)
    date_histogram = wh.DateHistograms(interval='1y')
    metadata = []
    metadata.append("abstract")
    metadata.append(RANGE_FIELD)
    histogram_map = {}
    histogram_map[RANGE_FIELD] = date_histogram
    documents = wh.Documents(limit="10", offset="0", metadata=metadata)
    returns = wh.ReturnsModel(documents, None, None, None, None, None, None, None, histogram_map)
    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_documents = search_model.documents
    for ranked_doc in result_documents:
        assert ranked_doc.document_id is not None
        assert ranked_doc.metadata is not None
        for key in ranked_doc.metadata:
            assert key is not None
            assert ranked_doc.metadata[key] is not None
        assert ranked_doc.corpus == CORPUS
        assert ranked_doc.links is not None
        doc_links = ranked_doc.links
        assert doc_links.href_search_matches is not None
        assert doc_links.href_categories is not None
    result_histograms = search_model.date_histograms
    for histogram_key in result_histograms:
        years_and_hits = result_histograms[histogram_key]
        for year in years_and_hits:
            year_date = wh.YearAndHits()
            year_and_hits = year_date._from_dict(year)
            assert year_and_hits.date is not None
            assert year_and_hits.hits > -1

def test_search_returns_typeahead():
    type_list = []
    type_list.append(SEMTYPE)
    typeahead = wh.Typeahead(ONTOLOGY, "hear", type_list, 5, True)
    returns = wh.ReturnsModel(typeahead=typeahead)
    response = IML_TEST.search(CORPUS, returns, query=None)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_typehead = search_model.typeahead
    for concept in result_typehead:
        assert concept.cui is not None

def test_search_returns_attributes():
    attributes = wh.Attributes()
    returns = wh.ReturnsModel(None, None, None, attributes)
    response = IML_TEST.search(CORPUS, returns, query=None)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_attributes = search_model.attributes
    for attribute in result_attributes:
        assert attribute.attribute_id is not None
        assert attribute.count > 0

def test_returns_attribute_values():
    values = wh.Values(ATTRIBUTE, scope='corpus')
    returns = wh.ReturnsModel(None, None, None, None, values)
    response = IML_TEST.search(CORPUS, returns, query=None)
    search_model = wh.SearchModel._from_dict(response.get_result())
    result_values = search_model.values
    for value in result_values:
        assert value.preferred_name is not None

def test_returns_aggregations():
    agg_map = {}
    aggregations = wh.Aggregations(limit=VALID_LIMIT)
    authors = {}
    authors['limit'] = 20
    agg_map['authors'] = aggregations
    returns = wh.ReturnsModel(aggregations=agg_map)
    response = IML_TEST.search(CORPUS, returns, query=None)
    search_model = wh.SearchModel._from_dict(response.get_result())
    results_aggregations = search_model.aggregations
    for key in results_aggregations:
        aggregations = results_aggregations[key]
        for aggregation in aggregations:
            agg = wh.AggregationModel._from_dict(aggregation)
            assert agg.name is not None
            assert agg.document_count > 0

def test_search_returns_passages():
    concepts = []
    search_concept = wh.SearchableConcept(cui=CUI, ontology=ONTOLOGY, rank='10',
                                          semanticType=SEMTYPE)
    concepts.append(search_concept)
    query = wh.Query(concepts=concepts)
    documents = wh.Documents("10", "0")
    matches = [search_concept]
    passages = wh.Passages(concepts_to_highlight=matches, limit=3, search_tag_begin='&lt;search_span&gt;',
                           search_tag_end='&lt;/search_span&gt;', related_tag_begin='&lt;related_span&gt;',
                           related_tag_end='&lt;/related_tag_end&gt;', min_score='0.1')
    returns = wh.ReturnsModel(documents, passages=passages)
#    response = IML_TEST.search(corpus=CORPUS, query=query, returns=returns)
#    search_model = wh.SearchModel._from_dict(response.get_result())
#    result_documents = search_model.documents
#    for ranked_doc in result_documents:
#        assert ranked_doc.document_id is not None
#        assert ranked_doc.metadata is not None
#        for key in ranked_doc.metadata:
#            assert key is not None
#            assert ranked_doc.metadata[key] is not None
#        assert ranked_doc.corpus == CORPUS
#        assert ranked_doc.links is not None
#        doc_links = ranked_doc.links
#        assert doc_links.href_search_matches is not None
#        assert doc_links.href_categories is not None
#        doc_passages = ranked_doc.passages
#        for passage in doc_passages:
#            assert passage.text is not None
#            assert passage.document_section is not None
#            assert passage.timestamp > -1
#        doc_annotations = ranked_doc.annotations
#        for annotation_name in doc_annotations:
#            annotation = doc_annotations[annotation_name]
#            assert annotation.cui is not None

def test_search_returns_ranges():
    range_map = {}
    ranges = wh.Ranges(ATTRIBUTE)
    range_map[ATTRIBUTE] = ranges
    returns = wh.ReturnsModel(ranges=ranges)
    response = IML_TEST.search(CORPUS, returns, query=None)
    search_model = wh.SearchModel._from_dict(response.get_result())
    ranges_model = search_model.ranges
    for key in ranges_model:
        value_range = ranges_model[key]
        assert value_range is None

def test_search_no_corpus():
    try:
        returns = wh.ReturnsModel()
        IML_TEST.search(None, returns)
    except ValueError as exp:
        assert exp is not None

def test_search_no_returns():
    try:
        IML_TEST.search(CORPUS, None)
    except ValueError as exp:
        assert exp is not None
