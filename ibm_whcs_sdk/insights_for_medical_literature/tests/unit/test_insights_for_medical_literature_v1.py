# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from ibm_whcs_sdk.insights_for_medical_literature import *

version = 'testString'

service = InsightsForMedicalLiteratureServiceV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

base_url = 'https://us-south.wh-iml.cloud.ibm.com/wh-iml/api'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Documents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_documents
#-----------------------------------------------------------------------------
class TestGetDocuments():

    #--------------------------------------------------------
    # get_documents()
    #--------------------------------------------------------
    @responses.activate
    def test_get_documents_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents'
        mock_response = '{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Invoke method
        response = service.get_documents(
            corpus,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_documents_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_documents_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents'
        mock_response = '{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_documents(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for add_corpus_document
#-----------------------------------------------------------------------------
class TestAddCorpusDocument():

    #--------------------------------------------------------
    # add_corpus_document()
    #--------------------------------------------------------
    @responses.activate
    def test_add_corpus_document_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document = {}
        acd_url = 'testString'
        api_key = 'testString'
        flow_id = 'testString'
        access_token = 'testString'
        other_annotators = [{ 'foo': 'bar' }]

        # Invoke method
        response = service.add_corpus_document(
            corpus,
            document=document,
            acd_url=acd_url,
            api_key=api_key,
            flow_id=flow_id,
            access_token=access_token,
            other_annotators=other_annotators,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['document'] == {}
        assert req_body['acdUrl'] == 'testString'
        assert req_body['apiKey'] == 'testString'
        assert req_body['flowId'] == 'testString'
        assert req_body['accessToken'] == 'testString'
        assert req_body['otherAnnotators'] == [{ 'foo': 'bar' }]


    #--------------------------------------------------------
    # test_add_corpus_document_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_add_corpus_document_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document = {}
        acd_url = 'testString'
        api_key = 'testString'
        flow_id = 'testString'
        access_token = 'testString'
        other_annotators = [{ 'foo': 'bar' }]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_corpus_document(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_document_info
#-----------------------------------------------------------------------------
class TestGetDocumentInfo():

    #--------------------------------------------------------
    # get_document_info()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_info_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString'
        mock_response = '{}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        verbose = True

        # Invoke method
        response = service.get_document_info(
            corpus,
            document_id,
            verbose=verbose,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string


    #--------------------------------------------------------
    # test_get_document_info_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_info_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString'
        mock_response = '{}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'

        # Invoke method
        response = service.get_document_info(
            corpus,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_document_info_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_info_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString'
        mock_response = '{}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_info(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_document_annotations
#-----------------------------------------------------------------------------
class TestGetDocumentAnnotations():

    #--------------------------------------------------------
    # get_document_annotations()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_annotations_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/annotations'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        document_section = 'testString'
        cuis = ['testString']
        include_text = True

        # Invoke method
        response = service.get_document_annotations(
            corpus,
            document_id,
            document_section,
            cuis=cuis,
            include_text=include_text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'document_section={}'.format(document_section) in query_string
        assert 'cuis={}'.format(','.join(cuis)) in query_string
        assert 'include_text={}'.format('true' if include_text else 'false') in query_string


    #--------------------------------------------------------
    # test_get_document_annotations_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_annotations_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/annotations'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        document_section = 'testString'

        # Invoke method
        response = service.get_document_annotations(
            corpus,
            document_id,
            document_section,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'document_section={}'.format(document_section) in query_string


    #--------------------------------------------------------
    # test_get_document_annotations_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_annotations_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/annotations'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        document_section = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "document_id": document_id,
            "document_section": document_section,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_annotations(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_document_categories
#-----------------------------------------------------------------------------
class TestGetDocumentCategories():

    #--------------------------------------------------------
    # get_document_categories()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_categories_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        highlight_tag_begin = 'testString'
        highlight_tag_end = 'testString'
        types = ['testString']
        category = 'disorders'
        only_negated_concepts = True
        fields = 'testString'
        limit = 38

        # Invoke method
        response = service.get_document_categories(
            corpus,
            document_id,
            highlight_tag_begin=highlight_tag_begin,
            highlight_tag_end=highlight_tag_end,
            types=types,
            category=category,
            only_negated_concepts=only_negated_concepts,
            fields=fields,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'highlight_tag_begin={}'.format(highlight_tag_begin) in query_string
        assert 'highlight_tag_end={}'.format(highlight_tag_end) in query_string
        assert 'types={}'.format(','.join(types)) in query_string
        assert 'category={}'.format(category) in query_string
        assert 'only_negated_concepts={}'.format('true' if only_negated_concepts else 'false') in query_string
        assert '_fields={}'.format(fields) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_document_categories_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_categories_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'

        # Invoke method
        response = service.get_document_categories(
            corpus,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_document_categories_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_categories_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_categories(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_document_multiple_categories
#-----------------------------------------------------------------------------
class TestGetDocumentMultipleCategories():

    #--------------------------------------------------------
    # get_document_multiple_categories()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_multiple_categories_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a StringBuilder model
        string_builder_model = {}

        # Construct a dict representation of a AnnotationModel model
        annotation_model_model = {}
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        model_license = 'testString'
        highlight_tag_begin = 'testString'
        highlight_tag_end = 'testString'
        fields = 'testString'
        limit = 38
        categories = []
        # Invoke method
        response = service.get_doc_multiple_categories(
            corpus,
            document_id,
            categories,
            highlight_tag_begin=highlight_tag_begin,
            highlight_tag_end=highlight_tag_end,
            fields=fields,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'highlight_tag_begin={}'.format(highlight_tag_begin) in query_string
        assert 'highlight_tag_end={}'.format(highlight_tag_end) in query_string
        assert '_fields={}'.format(fields) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_document_multiple_categories_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_multiple_categories_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a StringBuilder model
        string_builder_model = {}

        # Construct a dict representation of a AnnotationModel model
        annotation_model_model = {}
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        model_license = 'testString'
        highlighted_title = string_builder_model
        highlighted_abstract = string_builder_model
        highlighted_body = string_builder_model
        highlighted_sections = {}
        passages = {}
        annotations = {}
        categories = []

        # Invoke method
        response = service.get_doc_multiple_categories(
            corpus,
            document_id,
            categories,
            headers={},
            fields={'modelLicense, passages, annotations, highlightedTitle, highlightedAbstract, highlightedBody, highlightedSections'}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_document_multiple_categories_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_multiple_categories_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/categories'
        mock_response = '{"modelLicense": "model_license", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"id": "id", "negated": false, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}]}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a StringBuilder model
        string_builder_model = {}

        # Construct a dict representation of a AnnotationModel model
        annotation_model_model = {}
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        model_license = 'testString'
        highlighted_title = string_builder_model
        highlighted_abstract = string_builder_model
        highlighted_body = string_builder_model
        highlighted_sections = {}
        passages = {}
        annotations = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_doc_multiple_categories(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_search_matches
#-----------------------------------------------------------------------------
class TestGetSearchMatches():

    #--------------------------------------------------------
    # get_search_matches()
    #--------------------------------------------------------
    @responses.activate
    def test_get_search_matches_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/search_matches'
        mock_response = '{"externalId": "external_id", "documentId": "document_id", "parentDocumentId": "parent_document_id", "publicationName": "publication_name", "publicationDate": "publication_date", "publicationURL": "publication_url", "authors": ["authors"], "title": "title", "medlineLicense": "medline_license", "hrefPubMed": "href_pub_med", "hrefPmc": "href_pmc", "hrefDoi": "href_doi", "pdfUrl": "pdf_url", "referenceUrl": "reference_url", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"negated": false, "score": 5, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}], "id": "id"}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        min_score = 36.0
        cuis = ['testString']
        text = ['testString']
        types = ['testString']
        attributes = ['testString']
        values = ['testString']
        nlu_relations = ['testString']
        limit = 38
        search_tag_begin = 'testString'
        search_tag_end = 'testString'
        related_tag_begin = 'testString'
        related_tag_end = 'testString'
        fields = 'testString'

        # Invoke method
        response = service.get_search_matches(
            corpus,
            document_id,
            min_score,
            cuis=cuis,
            text=text,
            types=types,
            attributes=attributes,
            values=values,
            nlu_relations=nlu_relations,
            limit=limit,
            search_tag_begin=search_tag_begin,
            search_tag_end=search_tag_end,
            related_tag_begin=related_tag_begin,
            related_tag_end=related_tag_end,
            fields=fields,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'min_score={}'.format(min_score) in query_string
        assert 'cuis={}'.format(','.join(cuis)) in query_string
        assert 'text={}'.format(','.join(text)) in query_string
        assert 'types={}'.format(','.join(types)) in query_string
        assert 'attributes={}'.format(','.join(attributes)) in query_string
        assert 'values={}'.format(','.join(values)) in query_string
        assert 'nlu_relations={}'.format(','.join(nlu_relations)) in query_string
        assert '_limit={}'.format(limit) in query_string
        assert 'search_tag_begin={}'.format(search_tag_begin) in query_string
        assert 'search_tag_end={}'.format(search_tag_end) in query_string
        assert 'related_tag_begin={}'.format(related_tag_begin) in query_string
        assert 'related_tag_end={}'.format(related_tag_end) in query_string
        assert '_fields={}'.format(fields) in query_string


    #--------------------------------------------------------
    # test_get_search_matches_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_search_matches_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/search_matches'
        mock_response = '{"externalId": "external_id", "documentId": "document_id", "parentDocumentId": "parent_document_id", "publicationName": "publication_name", "publicationDate": "publication_date", "publicationURL": "publication_url", "authors": ["authors"], "title": "title", "medlineLicense": "medline_license", "hrefPubMed": "href_pub_med", "hrefPmc": "href_pmc", "hrefDoi": "href_doi", "pdfUrl": "pdf_url", "referenceUrl": "reference_url", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"negated": false, "score": 5, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}], "id": "id"}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        min_score = 36.0

        # Invoke method
        response = service.get_search_matches(
            corpus,
            document_id,
            min_score,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'min_score={}'.format(min_score) in query_string


    #--------------------------------------------------------
    # test_get_search_matches_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_search_matches_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/documents/testString/search_matches'
        mock_response = '{"externalId": "external_id", "documentId": "document_id", "parentDocumentId": "parent_document_id", "publicationName": "publication_name", "publicationDate": "publication_date", "publicationURL": "publication_url", "authors": ["authors"], "title": "title", "medlineLicense": "medline_license", "hrefPubMed": "href_pub_med", "hrefPmc": "href_pmc", "hrefDoi": "href_doi", "pdfUrl": "pdf_url", "referenceUrl": "reference_url", "highlightedTitle": {}, "highlightedAbstract": {}, "highlightedBody": {}, "highlightedSections": {"mapKey": {}}, "passages": {"mapKey": {"mapKey": {"negated": false, "score": 5, "sentences": [{"documentSection": "document_section", "text": {}, "begin": 5, "end": 3, "timestamp": 9}], "id": "id"}}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        document_id = 'testString'
        min_score = 36.0

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "document_id": document_id,
            "min_score": min_score,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_search_matches(**req_copy)



# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: Corpora
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_corpora_config
#-----------------------------------------------------------------------------
class TestGetCorporaConfig():

    #--------------------------------------------------------
    # get_corpora_config()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpora_config_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        verbose = True

        # Invoke method
        response = service.get_corpora_config(
            verbose=verbose,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string


    #--------------------------------------------------------
    # test_get_corpora_config_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpora_config_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_corpora_config()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_corpora_config_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpora_config_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_corpora_config(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for set_corpus_schema
#-----------------------------------------------------------------------------
class TestSetCorpusSchema():

    #--------------------------------------------------------
    # set_corpus_schema()
    #--------------------------------------------------------
    @responses.activate
    def test_set_corpus_schema_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enrichment_targets = [{ 'foo': 'bar' }]
        metadata_fields = [{ 'foo': 'bar' }]
        corpus_name = 'testString'
        references = {}

        # Invoke method
        response = service.set_corpus_schema(
            enrichment_targets=enrichment_targets,
            metadata_fields=metadata_fields,
            corpus_name=corpus_name,
            references=references,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enrichmentTargets'] == [{ 'foo': 'bar' }]
        assert req_body['metadataFields'] == [{ 'foo': 'bar' }]
        assert req_body['corpusName'] == 'testString'
        assert req_body['references'] == {}


    #--------------------------------------------------------
    # test_set_corpus_schema_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_set_corpus_schema_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enrichment_targets = [{ 'foo': 'bar' }]
        metadata_fields = [{ 'foo': 'bar' }]
        corpus_name = 'testString'
        references = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_corpus_schema(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_corpus_schema
#-----------------------------------------------------------------------------
class TestDeleteCorpusSchema():

    #--------------------------------------------------------
    # delete_corpus_schema()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_corpus_schema_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance = 'testString'

        # Invoke method
        response = service.delete_corpus_schema(
            instance,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'instance={}'.format(instance) in query_string


    #--------------------------------------------------------
    # test_delete_corpus_schema_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_corpus_schema_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance": instance,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_corpus_schema(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for set_corpus_config
#-----------------------------------------------------------------------------
class TestSetCorpusConfig():

    #--------------------------------------------------------
    # set_corpus_config()
    #--------------------------------------------------------
    @responses.activate
    def test_set_corpus_config_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/configure'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        user_name = 'testString'
        password = 'testString'
        corpus_uri = 'testString'

        # Invoke method
        response = service.set_corpus_config(
            user_name=user_name,
            password=password,
            corpus_uri=corpus_uri,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['userName'] == 'testString'
        assert req_body['password'] == 'testString'
        assert req_body['corpusURI'] == 'testString'


    #--------------------------------------------------------
    # test_set_corpus_config_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_set_corpus_config_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/configure'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        user_name = 'testString'
        password = 'testString'
        corpus_uri = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_corpus_config(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for monitor_corpus
#-----------------------------------------------------------------------------
class TestMonitorCorpus():

    #--------------------------------------------------------
    # monitor_corpus()
    #--------------------------------------------------------
    @responses.activate
    def test_monitor_corpus_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/monitor'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        apikey = 'testString'

        # Invoke method
        response = service.monitor_corpus(
            apikey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'apikey={}'.format(apikey) in query_string


    #--------------------------------------------------------
    # test_monitor_corpus_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_monitor_corpus_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/monitor'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        apikey = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "apikey": apikey,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.monitor_corpus(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for enable_corpus_search_tracking
#-----------------------------------------------------------------------------
class TestEnableCorpusSearchTracking():

    #--------------------------------------------------------
    # enable_corpus_search_tracking()
    #--------------------------------------------------------
    @responses.activate
    def test_enable_corpus_search_tracking_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/tracking'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        enable_tracking = True

        # Invoke method
        response = service.enable_corpus_search_tracking(
            enable_tracking=enable_tracking,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'enable_tracking={}'.format('true' if enable_tracking else 'false') in query_string


    #--------------------------------------------------------
    # test_enable_corpus_search_tracking_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_enable_corpus_search_tracking_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/tracking'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Invoke method
        response = service.enable_corpus_search_tracking()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_enable_corpus_search_tracking_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_enable_corpus_search_tracking_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/tracking'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.enable_corpus_search_tracking(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_corpus_config
#-----------------------------------------------------------------------------
class TestGetCorpusConfig():

    #--------------------------------------------------------
    # get_corpus_config()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_config_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        verbose = True

        # Invoke method
        response = service.get_corpus_config(
            corpus,
            verbose=verbose,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string


    #--------------------------------------------------------
    # test_get_corpus_config_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_config_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Invoke method
        response = service.get_corpus_config(
            corpus,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_corpus_config_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_config_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString'
        mock_response = '{"corpora": [{"corpusName": "corpus_name", "ontologies": ["ontologies"], "descriptiveName": "descriptive_name", "bvt": false, "elasticsearchIndex": "elasticsearch_index"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_corpus_config(**req_copy)

# endregion
##############################################################################
# End of Service: Corpora
##############################################################################

##############################################################################
# Start of Service: Status
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_health_check_status
#-----------------------------------------------------------------------------
class TestGetHealthCheckStatus():

    #--------------------------------------------------------
    # get_health_check_status()
    #--------------------------------------------------------
    @responses.activate
    def test_get_health_check_status_all_params(self):
        # Set up mock
        url = base_url + '/v1/status/health_check'
        mock_response = '{"version": "version", "upTime": "up_time", "serviceState": "OK", "stateDetails": "state_details", "hostName": "host_name", "requestCount": 13, "maxMemoryMb": 13, "commitedMemoryMb": 18, "inUseMemoryMb": 16, "availableProcessors": 20, "concurrentRequests": 19, "maxConcurrentRequests": 23, "totalRejectedRequests": 23, "totalBlockedRequests": 22}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accept = 'application/json'
        format = 'json'

        # Invoke method
        response = service.get_health_check_status(
            accept=accept,
            format=format,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'format={}'.format(format) in query_string


    #--------------------------------------------------------
    # test_get_health_check_status_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_health_check_status_required_params(self):
        # Set up mock
        url = base_url + '/v1/status/health_check'
        mock_response = '{"version": "version", "upTime": "up_time", "serviceState": "OK", "stateDetails": "state_details", "hostName": "host_name", "requestCount": 13, "maxMemoryMb": 13, "commitedMemoryMb": 18, "inUseMemoryMb": 16, "availableProcessors": 20, "concurrentRequests": 19, "maxConcurrentRequests": 23, "totalRejectedRequests": 23, "totalBlockedRequests": 22}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_health_check_status()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Status
##############################################################################

##############################################################################
# Start of Service: Search
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for search
#-----------------------------------------------------------------------------
class TestSearch():

    #--------------------------------------------------------
    # search()
    #--------------------------------------------------------
    @responses.activate
    def test_search_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search'
        mock_response = '{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation"}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [], "attributeValues": [], "relations": [], "mesh": [], "text": []}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text"}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [], "searchTermToPassages": {"mapKey": []}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": []}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": []}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": []}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "annotations": {"mapKey": null}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [], "types": ["types"], "attributes": [], "values": [], "ranges": {"mapKey": null}, "typeahead": [], "aggregations": {"mapKey": []}, "dateHistograms": {"mapKey": []}, "qualifiers": [], "expandedQuery": {"anyKey": "anyValue"}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": null}, "documents": [], "subQueries": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        body = {}
        returns = {'documents'}
        verbose = True

        # Invoke method
#        response = service.search(
#            corpus,
#            returns,
#            verbose=verbose,
#            headers={}
#        )

        # Check for correct operation
#        assert len(responses.calls) == 1
#        assert response.status_code == 200
        # Validate query params
#        query_string = responses.calls[0].request.url.split('?',1)[1]
#        query_string = requests.utils.unquote(query_string)
#        assert 'verbose={}'.format('true' if verbose else 'false') in query_string
        # Validate body params
#        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
#        assert req_body == body


    #--------------------------------------------------------
    # test_search_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_search_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search'
        mock_response = '{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation"}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [], "attributeValues": [], "relations": [], "mesh": [], "text": []}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text"}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [], "searchTermToPassages": {"mapKey": []}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": []}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": []}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": []}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "annotations": {"mapKey": null}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [], "types": ["types"], "attributes": [], "values": [], "ranges": {"mapKey": null}, "typeahead": [], "aggregations": {"mapKey": []}, "dateHistograms": {"mapKey": []}, "qualifiers": [], "expandedQuery": {"anyKey": "anyValue"}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": null}, "documents": [], "subQueries": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        body = 'testString'
        returns = {'documents'}
        # Invoke method
#        response = service.search(
#            corpus,
#            returns,
#            headers={}
#        )

        # Check for correct operation
#        assert len(responses.calls) == 1
#        assert response.status_code == 200
        # Validate body params
#        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
#        assert req_body == body


    #--------------------------------------------------------
    # test_search_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_search_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search'
        mock_response = '{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation", "source": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}, "target": {"section": "section", "begin": 5, "end": 3, "coveredText": "covered_text", "source": "source", "type": "type"}}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "attributeValues": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "relations": [{"relationId": "relation_id", "relation": "relation"}], "mesh": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}], "text": [{"uniqueId": 9, "stickyIds": [10], "section": "section", "type": "type", "begin": 5, "end": 3, "coveredText": "covered_text", "cui": "cui", "preferredName": "preferred_name", "source": "source", "negated": false, "hypothetical": true, "timestamp": 9, "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "features": {"mapKey": "inner"}, "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "hits": 4}]}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "text": {}, "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text", "data": {"concepts": [], "attributeValues": [], "relations": [], "mesh": [], "text": []}}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}], "searchTermToPassages": {"mapKey": [{"documentSection": "document_section", "timestamp": 9, "preferredName": "preferred_name"}]}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "parents": {"count": 5, "hits": 4}, "children": {"count": 5, "hits": 4}, "siblings": {"count": 5, "hits": 4}, "related": {"count": 5, "hits": 4}, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": [{"messageType": "expanded_request", "url": "url", "request": {"anyKey": "anyValue"}, "headers": ["headers"], "status": 6, "response": {"anyKey": "anyValue"}}]}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": [{"boolOperand": "bool_operand"}]}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": [{"text": "text"}]}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "links": {"hrefSearchMatches": "href_search_matches", "hrefCategories": "href_categories"}, "passages": {"allPassages": [], "searchTermToPassages": {"mapKey": []}}, "annotations": {"mapKey": {"uniqueId": 9, "stickyIds": [10], "ontology": "ontology", "section": "section", "preferredName": "preferred_name", "cui": "cui", "attributeId": "attribute_id", "qualifiers": ["qualifiers"], "type": "type", "negated": false, "hypothetical": true, "unit": "unit", "minValue": "min_value", "maxValue": "max_value", "operator": "operator", "nluSourceType": "nlu_source_type", "nluRelation": "nlu_relation", "nluTargetType": "nlu_target_type", "nluEntityIndex": "nlu_entity_index", "nluMentionIndex": "nlu_mention_index", "nluRelationId": "nlu_relation_id", "nluSide": "nlu_side", "begin": 5, "end": 3, "score": 5, "timestamp": 9, "features": {"mapKey": "inner"}, "hits": 4}}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "types": ["types"], "attributes": [{"attributeId": "attribute_id", "displayName": "display_name", "count": 5}], "values": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "ranges": {"mapKey": {"operator": "operator", "min": "min", "max": "max", "count": 5}}, "typeahead": [{"ontology": "ontology", "cui": "cui", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "count": 5, "hitCount": 9, "score": 5, "documentIds": ["document_ids"], "dataType": "data_type", "unit": "unit", "operator": "operator", "minValue": "min_value", "maxValue": "max_value", "vocab": "vocab", "properties": ["properties"]}], "aggregations": {"mapKey": [{"name": "name", "documentCount": 14}]}, "dateHistograms": {"mapKey": [{"date": "date", "hits": 4}]}, "qualifiers": [{"id": "id", "name": "name"}], "backend": {"messages": []}, "expandedQuery": {"anyKey": "anyValue"}, "parsedBoolExpression": {"boolExpression": "bool_expression", "boolOperands": []}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": {"unstructured": []}}, "metadata": {"corpus": "corpus", "corpusDescription": "corpus_description", "fields": {"mapKey": ["inner"]}}, "documents": [{"documentId": "document_id", "title": "title", "metadata": {"mapKey": ["inner"]}, "sectionName": "section_name", "sectionId": "section_id", "corpus": "corpus", "annotations": {"mapKey": null}}], "subQueries": [{"href": "href", "pageNumber": 11, "get_limit": 9, "totalDocumentCount": 20, "concepts": [], "types": ["types"], "attributes": [], "values": [], "ranges": {"mapKey": null}, "typeahead": [], "aggregations": {"mapKey": []}, "dateHistograms": {"mapKey": []}, "qualifiers": [], "expandedQuery": {"anyKey": "anyValue"}, "conceptsExist": {"mapKey": 5}, "cursorId": "cursor_id", "vocabs": ["vocabs"], "annotations": {"mapKey": null}, "documents": [], "subQueries": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        body = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.search(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_fields
#-----------------------------------------------------------------------------
class TestGetFields():

    #--------------------------------------------------------
    # get_fields()
    #--------------------------------------------------------
    @responses.activate
    def test_get_fields_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search/metadata'
        mock_response = '{"fields": {"mapKey": {"supports": ["supports"]}}, "sectionFieldNames": ["section_field_names"], "attrSectionFieldNames": ["attr_section_field_names"], "qualifierSectionFieldNames": ["qualifier_section_field_names"], "meshSectionFieldNames": ["mesh_section_field_names"], "fieldIndexMap": {"mapKey": "inner"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Invoke method
        response = service.get_fields(
            corpus,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_fields_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_fields_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search/metadata'
        mock_response = '{"fields": {"mapKey": {"supports": ["supports"]}}, "sectionFieldNames": ["section_field_names"], "attrSectionFieldNames": ["attr_section_field_names"], "qualifierSectionFieldNames": ["qualifier_section_field_names"], "meshSectionFieldNames": ["mesh_section_field_names"], "fieldIndexMap": {"mapKey": "inner"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_fields(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for typeahead
#-----------------------------------------------------------------------------
class TestTypeahead():

    #--------------------------------------------------------
    # typeahead()
    #--------------------------------------------------------
    @responses.activate
    def test_typeahead_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search/typeahead'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        query = 'testString'
        ontologies = ['concepts']
        types = ['testString']
        category = 'disorders'
        verbose = True
        limit = 38
        max_hit_count = 38
        no_duplicates = True

        # Invoke method
        response = service.typeahead(
            corpus,
            query,
            ontologies=ontologies,
            types=types,
            category=category,
            verbose=verbose,
            limit=limit,
            max_hit_count=max_hit_count,
            no_duplicates=no_duplicates,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'query={}'.format(query) in query_string
        assert 'ontologies={}'.format(','.join(ontologies)) in query_string
        assert 'types={}'.format(','.join(types)) in query_string
        assert 'category={}'.format(category) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string
        assert '_limit={}'.format(limit) in query_string
        assert 'max_hit_count={}'.format(max_hit_count) in query_string
        assert 'no_duplicates={}'.format('true' if no_duplicates else 'false') in query_string


    #--------------------------------------------------------
    # test_typeahead_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_typeahead_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search/typeahead'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        query = 'testString'

        # Invoke method
        response = service.typeahead(
            corpus,
            query,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'query={}'.format(query) in query_string


    #--------------------------------------------------------
    # test_typeahead_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_typeahead_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/search/typeahead'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        query = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.typeahead(**req_copy)



# endregion
##############################################################################
# End of Service: Search
##############################################################################

##############################################################################
# Start of Service: Concepts
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_concepts
#-----------------------------------------------------------------------------
class TestGetConcepts():

    #--------------------------------------------------------
    # get_concepts()
    #--------------------------------------------------------
    @responses.activate
    def test_get_concepts_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        cuis = ['testString']
        preferred_names = ['testString']
        surface_forms = ['testString']
        attributes = ['testString']
        verbose = True
        sort = 'hitCount'
        limit = 38

        # Invoke method
        response = service.get_concepts(
            corpus,
            cuis=cuis,
            preferred_names=preferred_names,
            surface_forms=surface_forms,
            attributes=attributes,
            verbose=verbose,
            sort=sort,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'cuis={}'.format(','.join(cuis)) in query_string
        assert 'preferred_names={}'.format(','.join(preferred_names)) in query_string
        assert 'surface_forms={}'.format(','.join(surface_forms)) in query_string
        assert 'attributes={}'.format(','.join(attributes)) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string
        assert '_sort={}'.format(sort) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_concepts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_concepts_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Invoke method
        response = service.get_concepts(
            corpus,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_concepts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_concepts_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_concepts(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for add_artifact
#-----------------------------------------------------------------------------
class TestAddArtifact():

    #--------------------------------------------------------
    # add_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_add_artifact_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/definitions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a DictonaryEntry model
        dictonary_entry_model = {}
        dictonary_entry_model['children'] = ['testString']
        dictonary_entry_model['cui'] = 'testString'
        dictonary_entry_model['definition'] = ['testString']
        dictonary_entry_model['parents'] = ['testString']
        dictonary_entry_model['preferredName'] = 'testString'
        dictonary_entry_model['semtypes'] = ['testString']
        dictonary_entry_model['siblings'] = ['testString']
        dictonary_entry_model['surfaceForms'] = ['testString']
        dictonary_entry_model['variants'] = ['testString']
        dictonary_entry_model['vocab'] = 'testString'
        dictonary_entry_model['related'] = ['testString']
        dictonary_entry_model['source'] = 'testString'
        dictonary_entry_model['source_version'] = 'testString'

        # Construct a dict representation of a PossbileValues model
        possbile_values_model = {}
        possbile_values_model['displayValue'] = 'testString'
        possbile_values_model['value'] = 'testString'

        # Construct a dict representation of a AttributeEntry model
        attribute_entry_model = {}
        attribute_entry_model['attr_name'] = 'testString'
        attribute_entry_model['data_type'] = 'testString'
        attribute_entry_model['default_value'] = 'testString'
        attribute_entry_model['description'] = 'testString'
        attribute_entry_model['display_name'] = 'testString'
        attribute_entry_model['doc_id'] = 'testString'
        attribute_entry_model['field_values'] = ['testString']
        attribute_entry_model['maximum_value'] = 'testString'
        attribute_entry_model['minimum_value'] = 'testString'
        attribute_entry_model['multi_value'] = True
        attribute_entry_model['units'] = 'testString'
        attribute_entry_model['valueType'] = 'testString'
        attribute_entry_model['possible_values'] = [possbile_values_model]

        # Set up parameter values
        corpus = 'testString'
        dictionary_entry = dictonary_entry_model
        attribute_entry = attribute_entry_model

        # Invoke method
        response = service.add_artifact(
            corpus,
            dictionary_entry=dictionary_entry,
            attribute_entry=attribute_entry,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['dictionaryEntry'] == dictonary_entry_model
        assert req_body['attributeEntry'] == attribute_entry_model


    #--------------------------------------------------------
    # test_add_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_add_artifact_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/definitions'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a DictonaryEntry model
        dictonary_entry_model = {}
        dictonary_entry_model['children'] = ['testString']
        dictonary_entry_model['cui'] = 'testString'
        dictonary_entry_model['definition'] = ['testString']
        dictonary_entry_model['parents'] = ['testString']
        dictonary_entry_model['preferredName'] = 'testString'
        dictonary_entry_model['semtypes'] = ['testString']
        dictonary_entry_model['siblings'] = ['testString']
        dictonary_entry_model['surfaceForms'] = ['testString']
        dictonary_entry_model['variants'] = ['testString']
        dictonary_entry_model['vocab'] = 'testString'
        dictonary_entry_model['related'] = ['testString']
        dictonary_entry_model['source'] = 'testString'
        dictonary_entry_model['source_version'] = 'testString'

        # Construct a dict representation of a PossbileValues model
        possbile_values_model = {}
        possbile_values_model['displayValue'] = 'testString'
        possbile_values_model['value'] = 'testString'

        # Construct a dict representation of a AttributeEntry model
        attribute_entry_model = {}
        attribute_entry_model['attr_name'] = 'testString'
        attribute_entry_model['data_type'] = 'testString'
        attribute_entry_model['default_value'] = 'testString'
        attribute_entry_model['description'] = 'testString'
        attribute_entry_model['display_name'] = 'testString'
        attribute_entry_model['doc_id'] = 'testString'
        attribute_entry_model['field_values'] = ['testString']
        attribute_entry_model['maximum_value'] = 'testString'
        attribute_entry_model['minimum_value'] = 'testString'
        attribute_entry_model['multi_value'] = True
        attribute_entry_model['units'] = 'testString'
        attribute_entry_model['valueType'] = 'testString'
        attribute_entry_model['possible_values'] = [possbile_values_model]

        # Set up parameter values
        corpus = 'testString'
        dictionary_entry = dictonary_entry_model
        attribute_entry = attribute_entry_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_artifact(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_cui_info
#-----------------------------------------------------------------------------
class TestGetCuiInfo():

    #--------------------------------------------------------
    # get_cui_info()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cui_info_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString'
        mock_response = '{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "semanticTypes": ["semantic_types"], "surfaceForms": ["surface_forms"], "definition": "definition", "hasParents": false, "hasChildren": true, "hasSiblings": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        ontology = 'testString'
        fields = 'testString'
        tree_layout = True

        # Invoke method
        response = service.get_cui_info(
            corpus,
            name_or_id,
            ontology=ontology,
            fields=fields,
            tree_layout=tree_layout,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'ontology={}'.format(ontology) in query_string
        assert '_fields={}'.format(fields) in query_string
        assert 'tree_layout={}'.format('true' if tree_layout else 'false') in query_string


    #--------------------------------------------------------
    # test_get_cui_info_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cui_info_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString'
        mock_response = '{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "semanticTypes": ["semantic_types"], "surfaceForms": ["surface_forms"], "definition": "definition", "hasParents": false, "hasChildren": true, "hasSiblings": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'

        # Invoke method
        response = service.get_cui_info(
            corpus,
            name_or_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_cui_info_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cui_info_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString'
        mock_response = '{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "semanticTypes": ["semantic_types"], "surfaceForms": ["surface_forms"], "definition": "definition", "hasParents": false, "hasChildren": true, "hasSiblings": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "name_or_id": name_or_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_cui_info(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_hit_count
#-----------------------------------------------------------------------------
class TestGetHitCount():

    #--------------------------------------------------------
    # get_hit_count()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hit_count_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/hit_count'
        mock_response = '{"hitCount": 9}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        ontology = 'testString'

        # Invoke method
        response = service.get_hit_count(
            corpus,
            name_or_id,
            ontology=ontology,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'ontology={}'.format(ontology) in query_string


    #--------------------------------------------------------
    # test_get_hit_count_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hit_count_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/hit_count'
        mock_response = '{"hitCount": 9}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'

        # Invoke method
        response = service.get_hit_count(
            corpus,
            name_or_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_hit_count_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_hit_count_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/hit_count'
        mock_response = '{"hitCount": 9}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "name_or_id": name_or_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_hit_count(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_related_concepts
#-----------------------------------------------------------------------------
class TestGetRelatedConcepts():

    #--------------------------------------------------------
    # get_related_concepts()
    #--------------------------------------------------------
    @responses.activate
    def test_get_related_concepts_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/related_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        relationship = 'children'
        ontology = 'testString'
        relationship_attributes = ['testString']
        sources = ['testString']
        recursive = True
        tree_layout = True
        max_depth = 38

        # Invoke method
        response = service.get_related_concepts(
            corpus,
            name_or_id,
            relationship,
            ontology=ontology,
            relationship_attributes=relationship_attributes,
            sources=sources,
            recursive=recursive,
            tree_layout=tree_layout,
            max_depth=max_depth,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'relationship={}'.format(relationship) in query_string
        assert 'ontology={}'.format(ontology) in query_string
        assert 'relationship_attributes={}'.format(','.join(relationship_attributes)) in query_string
        assert 'sources={}'.format(','.join(sources)) in query_string
        assert 'recursive={}'.format('true' if recursive else 'false') in query_string
        assert 'tree_layout={}'.format('true' if tree_layout else 'false') in query_string
        assert 'max_depth={}'.format(max_depth) in query_string


    #--------------------------------------------------------
    # test_get_related_concepts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_related_concepts_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/related_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        relationship = 'children'

        # Invoke method
        response = service.get_related_concepts(
            corpus,
            name_or_id,
            relationship,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'relationship={}'.format(relationship) in query_string


    #--------------------------------------------------------
    # test_get_related_concepts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_related_concepts_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/related_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"], "nextConcepts": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        relationship = 'children'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "name_or_id": name_or_id,
            "relationship": relationship,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_related_concepts(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_similar_concepts
#-----------------------------------------------------------------------------
class TestGetSimilarConcepts():

    #--------------------------------------------------------
    # get_similar_concepts()
    #--------------------------------------------------------
    @responses.activate
    def test_get_similar_concepts_all_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/similar_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        return_ontologies = ['testString']
        ontology = 'testString'
        limit = 38

        # Invoke method
        response = service.get_similar_concepts(
            corpus,
            name_or_id,
            return_ontologies,
            ontology=ontology,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'return_ontologies={}'.format(','.join(return_ontologies)) in query_string
        assert 'ontology={}'.format(ontology) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_similar_concepts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_similar_concepts_required_params(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/similar_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        return_ontologies = ['testString']

        # Invoke method
        response = service.get_similar_concepts(
            corpus,
            name_or_id,
            return_ontologies,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'return_ontologies={}'.format(','.join(return_ontologies)) in query_string


    #--------------------------------------------------------
    # test_get_similar_concepts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_similar_concepts_value_error(self):
        # Set up mock
        url = base_url + '/v1/corpora/testString/concepts/testString/similar_concepts'
        mock_response = '{"concepts": [{"cui": "cui", "ontology": "ontology", "preferredName": "preferred_name", "alternativeName": "alternative_name", "semanticType": "semantic_type", "rank": 4, "hitCount": 9, "score": 5, "surfaceForms": ["surface_forms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        corpus = 'testString'
        name_or_id = 'testString'
        return_ontologies = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "corpus": corpus,
            "name_or_id": name_or_id,
            "return_ontologies": return_ontologies,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_similar_concepts(**req_copy)


# endregion
##############################################################################
# End of Service: Concepts
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for AttributeEntry
#-----------------------------------------------------------------------------
class TestAttributeEntry():

    #--------------------------------------------------------
    # Test serialization/deserialization for AttributeEntry
    #--------------------------------------------------------
    def test_attribute_entry_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        possbile_values_model = {} # PossbileValues
        possbile_values_model['displayValue'] = 'testString'
        possbile_values_model['value'] = 'testString'

        # Construct a json representation of a AttributeEntry model
        attribute_entry_model_json = {}
        attribute_entry_model_json['attr_name'] = 'testString'
        attribute_entry_model_json['data_type'] = 'testString'
        attribute_entry_model_json['default_value'] = 'testString'
        attribute_entry_model_json['description'] = 'testString'
        attribute_entry_model_json['display_name'] = 'testString'
        attribute_entry_model_json['doc_id'] = 'testString'
        attribute_entry_model_json['field_values'] = ['testString']
        attribute_entry_model_json['maximum_value'] = 'testString'
        attribute_entry_model_json['minimum_value'] = 'testString'
        attribute_entry_model_json['multi_value'] = True
        attribute_entry_model_json['units'] = 'testString'
        attribute_entry_model_json['valueType'] = 'testString'
        attribute_entry_model_json['possible_values'] = [possbile_values_model]

        # Construct a model instance of AttributeEntry by calling from_dict on the json representation
        attribute_entry_model = AttributeEntry.from_dict(attribute_entry_model_json)
        assert attribute_entry_model != False

        # Construct a model instance of AttributeEntry by calling from_dict on the json representation
        attribute_entry_model_dict = AttributeEntry.from_dict(attribute_entry_model_json).__dict__
        attribute_entry_model2 = AttributeEntry(**attribute_entry_model_dict)

        # Verify the model instances are equivalent
        assert attribute_entry_model == attribute_entry_model2

        # Convert model instance back to dict and verify no loss of data
        attribute_entry_model_json2 = attribute_entry_model.to_dict()
        assert attribute_entry_model_json2 == attribute_entry_model_json

#-----------------------------------------------------------------------------
# Test Class for BoolOperand
#-----------------------------------------------------------------------------
class TestBoolOperand():

    #--------------------------------------------------------
    # Test serialization/deserialization for BoolOperand
    #--------------------------------------------------------
    def test_bool_operand_serialization(self):

        # Construct a json representation of a BoolOperand model
        bool_operand_model_json = {}
        bool_operand_model_json['boolOperand'] = 'testString'

        # Construct a model instance of BoolOperand by calling from_dict on the json representation
        bool_operand_model = BoolOperand.from_dict(bool_operand_model_json)
        assert bool_operand_model != False

        # Construct a model instance of BoolOperand by calling from_dict on the json representation
        bool_operand_model_dict = BoolOperand.from_dict(bool_operand_model_json).__dict__
        bool_operand_model2 = BoolOperand(**bool_operand_model_dict)

        # Verify the model instances are equivalent
        assert bool_operand_model == bool_operand_model2

        # Convert model instance back to dict and verify no loss of data
        bool_operand_model_json2 = bool_operand_model.to_dict()
        assert bool_operand_model_json2 == bool_operand_model_json

#-----------------------------------------------------------------------------
# Test Class for DictonaryEntry
#-----------------------------------------------------------------------------
class TestDictionaryEntry():

    #--------------------------------------------------------
    # Test serialization/deserialization for DictonaryEntry
    #--------------------------------------------------------
    def test_dictionary_entry_serialization(self):

        # Construct a json representation of a DictonaryEntry model
        dictonary_entry_model_json = {}
        dictonary_entry_model_json['children'] = ['testString']
        dictonary_entry_model_json['cui'] = 'testString'
        dictonary_entry_model_json['definition'] = ['testString']
        dictonary_entry_model_json['parents'] = ['testString']
        dictonary_entry_model_json['preferredName'] = 'testString'
        dictonary_entry_model_json['semtypes'] = ['testString']
        dictonary_entry_model_json['siblings'] = ['testString']
        dictonary_entry_model_json['surfaceForms'] = ['testString']
        dictonary_entry_model_json['variants'] = ['testString']
        dictonary_entry_model_json['vocab'] = 'testString'
        dictonary_entry_model_json['related'] = ['testString']
        dictonary_entry_model_json['source'] = 'testString'
        dictonary_entry_model_json['source_version'] = 'testString'

        # Construct a model instance of DictonaryEntry by calling from_dict on the json representation
        dictonary_entry_model = DictionaryEntry.from_dict(dictonary_entry_model_json)
        assert dictonary_entry_model != False

        # Construct a model instance of DictonaryEntry by calling from_dict on the json representation
        dictonary_entry_model_dict = DictionaryEntry.from_dict(dictonary_entry_model_json).__dict__
        dictonary_entry_model2 = DictionaryEntry(**dictonary_entry_model_dict)

        # Verify the model instances are equivalent
        assert dictonary_entry_model == dictonary_entry_model2

        # Convert model instance back to dict and verify no loss of data
        dictonary_entry_model_json2 = dictonary_entry_model.to_dict()
        assert dictonary_entry_model_json2 == dictonary_entry_model_json

#-----------------------------------------------------------------------------
# Test Class for GetDocumentInfoResponse
#-----------------------------------------------------------------------------
class TestGetDocumentInfoResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for GetDocumentInfoResponse
    #--------------------------------------------------------
    def test_get_document_info_response_serialization(self):

        # Construct a json representation of a GetDocumentInfoResponse model
        get_document_info_response_model_json = {}
        get_document_info_response_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of GetDocumentInfoResponse by calling from_dict on the json representation
        get_document_info_response_model = GetDocumentInfoResponse.from_dict(get_document_info_response_model_json)
        assert get_document_info_response_model != False

        # Construct a model instance of GetDocumentInfoResponse by calling from_dict on the json representation
        get_document_info_response_model_dict = GetDocumentInfoResponse.from_dict(get_document_info_response_model_json).__dict__
        get_document_info_response_model2 = GetDocumentInfoResponse(**get_document_info_response_model_dict)

        # Verify the model instances are equivalent
        assert get_document_info_response_model == get_document_info_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_document_info_response_model_json2 = get_document_info_response_model.to_dict()
        assert get_document_info_response_model_json2 == get_document_info_response_model_json

#-----------------------------------------------------------------------------
# Test Class for Message
#-----------------------------------------------------------------------------
class TestMessage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Message
    #--------------------------------------------------------
    def test_message_serialization(self):

        # Construct a json representation of a Message model
        message_model_json = {}
        message_model_json['messageType'] = 'expanded_request'
        message_model_json['url'] = 'testString'
        message_model_json['request'] = { 'foo': 'bar' }
        message_model_json['headers'] = ['testString']
        message_model_json['status'] = 38
        message_model_json['response'] = { 'foo': 'bar' }

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model = Message.from_dict(message_model_json)
        assert message_model != False

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model_dict = Message.from_dict(message_model_json).__dict__
        message_model2 = Message(**message_model_dict)

        # Verify the model instances are equivalent
        assert message_model == message_model2

        # Convert model instance back to dict and verify no loss of data
        message_model_json2 = message_model.to_dict()
        assert message_model_json2 == message_model_json

#-----------------------------------------------------------------------------
# Test Class for MetadataFields
#-----------------------------------------------------------------------------
class TestMetadataModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for MetadataFields
    #--------------------------------------------------------
    def test_metadata_model_serialization(self):

        # Construct a json representation of a MetadataFields model
        metadata_fields_model_json = {}
        metadata_fields_model_json['corpus'] = 'testString'
        metadata_fields_model_json['corpusDescription'] = 'testString'
        metadata_fields_model_json['fields'] = {}

        # Construct a model instance of MetadataFields by calling from_dict on the json representation
        metadata_fields_model = MetadataModel.from_dict(metadata_fields_model_json)
        assert metadata_fields_model != False

        # Construct a model instance of MetadataFields by calling from_dict on the json representation
        metadata_fields_model_dict = MetadataModel.from_dict(metadata_fields_model_json).__dict__
        metadata_fields_model2 = MetadataModel(**metadata_fields_model_dict)

        # Verify the model instances are equivalent
        assert metadata_fields_model == metadata_fields_model2

        # Convert model instance back to dict and verify no loss of data
        metadata_fields_model_json2 = metadata_fields_model.to_dict()
        assert metadata_fields_model_json2 == metadata_fields_model_json

#-----------------------------------------------------------------------------
# Test Class for PassagesModel
#-----------------------------------------------------------------------------
class TestPassagesModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for PassagesModel
    #--------------------------------------------------------
    def test_passages_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        string_builder_model = {} # StringBuilder

        passage_model = {} # Passage
        passage_model['documentSection'] = 'testString'
        passage_model['text'] = string_builder_model
        passage_model['timestamp'] = 26
        passage_model['preferredName'] = 'testString'

        # Construct a json representation of a PassagesModel model
        passages_model_model_json = {}
        passages_model_model_json['allPassages'] = [passage_model]
        passages_model_model_json['searchTermToPassages'] = {}

        # Construct a model instance of PassagesModel by calling from_dict on the json representation
        passages_model_model = PassagesModel.from_dict(passages_model_model_json)
        assert passages_model_model != False

        # Construct a model instance of PassagesModel by calling from_dict on the json representation
        passages_model_model_dict = PassagesModel.from_dict(passages_model_model_json).__dict__
        passages_model_model2 = PassagesModel(**passages_model_model_dict)

        # Verify the model instances are equivalent
        assert passages_model_model == passages_model_model2

        # Convert model instance back to dict and verify no loss of data
        passages_model_model_json2 = passages_model_model.to_dict()
        assert passages_model_model_json2 == passages_model_model_json

#-----------------------------------------------------------------------------
# Test Class for PossbileValues
#-----------------------------------------------------------------------------
class TestPossibleValues():

    #--------------------------------------------------------
    # Test serialization/deserialization for PossbileValues
    #--------------------------------------------------------
    def test_possbile_values_serialization(self):

        # Construct a json representation of a PossbileValues model
        possbile_values_model_json = {}
        possbile_values_model_json['displayValue'] = 'testString'
        possbile_values_model_json['value'] = 'testString'

        # Construct a model instance of PossbileValues by calling from_dict on the json representation
        possbile_values_model = PossibleValues.from_dict(possbile_values_model_json)
        assert possbile_values_model != False

        # Construct a model instance of PossbileValues by calling from_dict on the json representation
        possbile_values_model_dict = PossibleValues.from_dict(possbile_values_model_json).__dict__
        possbile_values_model2 = PossibleValues(**possbile_values_model_dict)

        # Verify the model instances are equivalent
        assert possbile_values_model == possbile_values_model2

        # Convert model instance back to dict and verify no loss of data
        possbile_values_model_json2 = possbile_values_model.to_dict()
        assert possbile_values_model_json2 == possbile_values_model_json

#-----------------------------------------------------------------------------
# Test Class for RankedDocLinks
#-----------------------------------------------------------------------------
class TestRankedDocLinks():

    #--------------------------------------------------------
    # Test serialization/deserialization for RankedDocLinks
    #--------------------------------------------------------
    def test_ranked_doc_links_serialization(self):

        # Construct a json representation of a RankedDocLinks model
        ranked_doc_links_model_json = {}
        ranked_doc_links_model_json['hrefSearchMatches'] = 'testString'
        ranked_doc_links_model_json['hrefCategories'] = 'testString'

        # Construct a model instance of RankedDocLinks by calling from_dict on the json representation
        ranked_doc_links_model = RankedDocLinks.from_dict(ranked_doc_links_model_json)
        assert ranked_doc_links_model != False

        # Construct a model instance of RankedDocLinks by calling from_dict on the json representation
        ranked_doc_links_model_dict = RankedDocLinks.from_dict(ranked_doc_links_model_json).__dict__
        ranked_doc_links_model2 = RankedDocLinks(**ranked_doc_links_model_dict)

        # Verify the model instances are equivalent
        assert ranked_doc_links_model == ranked_doc_links_model2

        # Convert model instance back to dict and verify no loss of data
        ranked_doc_links_model_json2 = ranked_doc_links_model.to_dict()
        assert ranked_doc_links_model_json2 == ranked_doc_links_model_json

#-----------------------------------------------------------------------------
# Test Class for StringBuilder
#-----------------------------------------------------------------------------
class TestStringBuilder():

    #--------------------------------------------------------
    # Test serialization/deserialization for StringBuilder
    #--------------------------------------------------------
    def test_string_builder_serialization(self):

        # Construct a json representation of a StringBuilder model
        string_builder_model_json = {}

        # Construct a model instance of StringBuilder by calling from_dict on the json representation
        string_builder_model = StringBuilder.from_dict(string_builder_model_json)
        assert string_builder_model != False

        # Construct a model instance of StringBuilder by calling from_dict on the json representation
        string_builder_model_dict = StringBuilder.from_dict(string_builder_model_json).__dict__
        string_builder_model2 = StringBuilder(**string_builder_model_dict)

        # Verify the model instances are equivalent
        assert string_builder_model == string_builder_model2

        # Convert model instance back to dict and verify no loss of data
        string_builder_model_json2 = string_builder_model.to_dict()
        assert string_builder_model_json2 == string_builder_model_json

#-----------------------------------------------------------------------------
# Test Class for AggregationModel
#-----------------------------------------------------------------------------
class TestAggregationModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for AggregationModel
    #--------------------------------------------------------
    def test_aggregation_model_serialization(self):

        # Construct a json representation of a AggregationModel model
        aggregation_model_model_json = {}
        aggregation_model_model_json['name'] = 'testString'
        aggregation_model_model_json['documentCount'] = 38

        # Construct a model instance of AggregationModel by calling from_dict on the json representation
        aggregation_model_model = AggregationModel.from_dict(aggregation_model_model_json)
        assert aggregation_model_model != False

        # Construct a model instance of AggregationModel by calling from_dict on the json representation
        aggregation_model_model_dict = AggregationModel.from_dict(aggregation_model_model_json).__dict__
        aggregation_model_model2 = AggregationModel(**aggregation_model_model_dict)

        # Verify the model instances are equivalent
        assert aggregation_model_model == aggregation_model_model2

        # Convert model instance back to dict and verify no loss of data
        aggregation_model_model_json2 = aggregation_model_model.to_dict()
        assert aggregation_model_model_json2 == aggregation_model_model_json

#-----------------------------------------------------------------------------
# Test Class for AnnotationModel
#-----------------------------------------------------------------------------
class TestAnnotationModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for AnnotationModel
    #--------------------------------------------------------
    def test_annotation_model_serialization(self):

        # Construct a json representation of a AnnotationModel model
        annotation_model_model_json = {}
        annotation_model_model_json['uniqueId'] = 38
        annotation_model_model_json['stickyIds'] = [38]
        annotation_model_model_json['ontology'] = 'testString'
        annotation_model_model_json['section'] = 'testString'
        annotation_model_model_json['preferredName'] = 'testString'
        annotation_model_model_json['cui'] = 'testString'
        annotation_model_model_json['attributeId'] = 'testString'
        annotation_model_model_json['qualifiers'] = ['testString']
        annotation_model_model_json['type'] = 'testString'
        annotation_model_model_json['negated'] = True
        annotation_model_model_json['hypothetical'] = True
        annotation_model_model_json['unit'] = 'testString'
        annotation_model_model_json['minValue'] = 'testString'
        annotation_model_model_json['maxValue'] = 'testString'
        annotation_model_model_json['operator'] = 'testString'
        annotation_model_model_json['nluSourceType'] = 'testString'
        annotation_model_model_json['nluRelation'] = 'testString'
        annotation_model_model_json['nluTargetType'] = 'testString'
        annotation_model_model_json['nluEntityIndex'] = 'testString'
        annotation_model_model_json['nluMentionIndex'] = 'testString'
        annotation_model_model_json['nluRelationId'] = 'testString'
        annotation_model_model_json['nluSide'] = 'testString'
        annotation_model_model_json['begin'] = 38
        annotation_model_model_json['end'] = 38
        annotation_model_model_json['score'] = 36.0
        annotation_model_model_json['timestamp'] = 26
        annotation_model_model_json['features'] = {}
        annotation_model_model_json['hits'] = 38

        # Construct a model instance of AnnotationModel by calling from_dict on the json representation
        annotation_model_model = AnnotationModel.from_dict(annotation_model_model_json)
        assert annotation_model_model != False

        # Construct a model instance of AnnotationModel by calling from_dict on the json representation
        annotation_model_model_dict = AnnotationModel.from_dict(annotation_model_model_json).__dict__
        annotation_model_model2 = AnnotationModel(**annotation_model_model_dict)

        # Verify the model instances are equivalent
        assert annotation_model_model == annotation_model_model2

        # Convert model instance back to dict and verify no loss of data
        annotation_model_model_json2 = annotation_model_model.to_dict()
        assert annotation_model_model_json2 == annotation_model_model_json

#-----------------------------------------------------------------------------
# Test Class for ArtifactModel
#-----------------------------------------------------------------------------
class TestArtifactModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for ArtifactModel
    #--------------------------------------------------------
    def test_artifact_model_serialization(self):

        # Construct a json representation of a ArtifactModel model
        artifact_model_model_json = {}
        artifact_model_model_json['cui'] = 'testString'
        artifact_model_model_json['ontology'] = 'testString'
        artifact_model_model_json['preferredName'] = 'testString'
        artifact_model_model_json['alternativeName'] = 'testString'
        artifact_model_model_json['semanticType'] = 'testString'
        artifact_model_model_json['rank'] = 38
        artifact_model_model_json['hitCount'] = 38
        artifact_model_model_json['score'] = 36.0
        artifact_model_model_json['surfaceForms'] = ['testString']

        # Construct a model instance of ArtifactModel by calling from_dict on the json representation
        artifact_model_model = ArtifactModel.from_dict(artifact_model_model_json)
        assert artifact_model_model != False

        # Construct a model instance of ArtifactModel by calling from_dict on the json representation
        artifact_model_model_dict = ArtifactModel.from_dict(artifact_model_model_json).__dict__
        artifact_model_model2 = ArtifactModel(**artifact_model_model_dict)

        # Verify the model instances are equivalent
        assert artifact_model_model == artifact_model_model2

        # Convert model instance back to dict and verify no loss of data
        artifact_model_model_json2 = artifact_model_model.to_dict()
        #assert artifact_model_model_json2 == artifact_model_model_json

#-----------------------------------------------------------------------------
# Test Class for Attribute
#-----------------------------------------------------------------------------
class TestAttribute():

    #--------------------------------------------------------
    # Test serialization/deserialization for Attribute
    #--------------------------------------------------------
    def test_attribute_serialization(self):

        # Construct a json representation of a Attribute model
        attribute_model_json = {}
        attribute_model_json['attributeId'] = 'testString'
        attribute_model_json['displayName'] = 'testString'
        attribute_model_json['count'] = 38

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model = Attribute.from_dict(attribute_model_json)
        assert attribute_model != False

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model_dict = Attribute.from_dict(attribute_model_json).__dict__
        attribute_model2 = Attribute(**attribute_model_dict)

        # Verify the model instances are equivalent
        assert attribute_model == attribute_model2

        # Convert model instance back to dict and verify no loss of data
        attribute_model_json2 = attribute_model.to_dict()
        assert attribute_model_json2 == attribute_model_json

#-----------------------------------------------------------------------------
# Test Class for Backend
#-----------------------------------------------------------------------------
class TestBackend():

    #--------------------------------------------------------
    # Test serialization/deserialization for Backend
    #--------------------------------------------------------
    def test_backend_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        message_model = {} # Message
        message_model['messageType'] = 'expanded_request'
        message_model['url'] = 'testString'
        message_model['request'] = { 'foo': 'bar' }
        message_model['headers'] = ['testString']
        message_model['status'] = 38
        message_model['response'] = { 'foo': 'bar' }

        # Construct a json representation of a Backend model
        backend_model_json = {}
        backend_model_json['messages'] = [message_model]

        # Construct a model instance of Backend by calling from_dict on the json representation
        backend_model = Backend.from_dict(backend_model_json)
        assert backend_model != False

        # Construct a model instance of Backend by calling from_dict on the json representation
        backend_model_dict = Backend.from_dict(backend_model_json).__dict__
        backend_model2 = Backend(**backend_model_dict)

        # Verify the model instances are equivalent
        assert backend_model == backend_model2

        # Convert model instance back to dict and verify no loss of data
        backend_model_json2 = backend_model.to_dict()
        assert backend_model_json2 == backend_model_json

#-----------------------------------------------------------------------------
# Test Class for BooleanOperands
#-----------------------------------------------------------------------------
class TestBooleanOperands():

    #--------------------------------------------------------
    # Test serialization/deserialization for BooleanOperands
    #--------------------------------------------------------
    def test_boolean_operands_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bool_operand_model = {} # BoolOperand
        bool_operand_model['boolOperand'] = 'testString'

        # Construct a json representation of a BooleanOperands model
        boolean_operands_model_json = {}
        boolean_operands_model_json['boolExpression'] = 'testString'
        boolean_operands_model_json['boolOperands'] = [bool_operand_model]

        # Construct a model instance of BooleanOperands by calling from_dict on the json representation
        boolean_operands_model = BooleanOperands.from_dict(boolean_operands_model_json)
        assert boolean_operands_model != False

        # Construct a model instance of BooleanOperands by calling from_dict on the json representation
        boolean_operands_model_dict = BooleanOperands.from_dict(boolean_operands_model_json).__dict__
        boolean_operands_model2 = BooleanOperands(**boolean_operands_model_dict)

        # Verify the model instances are equivalent
        assert boolean_operands_model == boolean_operands_model2

        # Convert model instance back to dict and verify no loss of data
        boolean_operands_model_json2 = boolean_operands_model.to_dict()
        assert boolean_operands_model_json2 == boolean_operands_model_json

#-----------------------------------------------------------------------------
# Test Class for CategoriesModel
#-----------------------------------------------------------------------------
class TestCategoriesModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for CategoriesModel
    #--------------------------------------------------------
    def test_categories_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        annotation_model_model = {} # AnnotationModel
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        string_builder_model = {} # StringBuilder

        # Construct a json representation of a CategoriesModel model
        categories_model_model_json = {}
        categories_model_model_json['modelLicense'] = 'testString'
        categories_model_model_json['highlightedTitle'] = string_builder_model
        categories_model_model_json['highlightedAbstract'] = string_builder_model
        categories_model_model_json['highlightedBody'] = string_builder_model
        categories_model_model_json['highlightedSections'] = {}
        categories_model_model_json['passages'] = {}
        categories_model_model_json['annotations'] = {}

        # Construct a model instance of CategoriesModel by calling from_dict on the json representation
        categories_model_model = CategoriesModel.from_dict(categories_model_model_json)
        assert categories_model_model != False

        # Construct a model instance of CategoriesModel by calling from_dict on the json representation
        categories_model_model_dict = CategoriesModel.from_dict(categories_model_model_json).__dict__
        categories_model_model2 = CategoriesModel(**categories_model_model_dict)

        # Verify the model instances are equivalent
        assert categories_model_model == categories_model_model2

        # Convert model instance back to dict and verify no loss of data
        categories_model_model_json2 = categories_model_model.to_dict()
        assert categories_model_model_json2 == categories_model_model_json

#-----------------------------------------------------------------------------
# Test Class for CommonDataModel
#-----------------------------------------------------------------------------
class TestCommonDataModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for CommonDataModel
    #--------------------------------------------------------
    def test_common_data_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        text_span_model = {} # TextSpan
        text_span_model['section'] = 'testString'
        text_span_model['begin'] = 38
        text_span_model['end'] = 38
        text_span_model['coveredText'] = 'testString'
        text_span_model['source'] = 'testString'
        text_span_model['type'] = 'testString'

        concept_model_model = {} # ConceptModel
        concept_model_model['uniqueId'] = 38
        concept_model_model['stickyIds'] = [38]
        concept_model_model['section'] = 'testString'
        concept_model_model['type'] = 'testString'
        concept_model_model['begin'] = 38
        concept_model_model['end'] = 38
        concept_model_model['coveredText'] = 'testString'
        concept_model_model['cui'] = 'testString'
        concept_model_model['preferredName'] = 'testString'
        concept_model_model['source'] = 'testString'
        concept_model_model['negated'] = True
        concept_model_model['hypothetical'] = True
        concept_model_model['timestamp'] = 26
        concept_model_model['attributeId'] = 'testString'
        concept_model_model['qualifiers'] = ['testString']
        concept_model_model['unit'] = 'testString'
        concept_model_model['minValue'] = 'testString'
        concept_model_model['maxValue'] = 'testString'
        concept_model_model['operator'] = 'testString'
        concept_model_model['features'] = {}
        concept_model_model['nluEntityIndex'] = 'testString'
        concept_model_model['nluMentionIndex'] = 'testString'
        concept_model_model['nluRelationId'] = 'testString'
        concept_model_model['nluSide'] = 'testString'
        concept_model_model['nluSourceType'] = 'testString'
        concept_model_model['nluRelation'] = 'testString'
        concept_model_model['nluTargetType'] = 'testString'
        concept_model_model['hits'] = 38

        relation_model_model = {} # RelationModel
        relation_model_model['relationId'] = 'testString'
        relation_model_model['relation'] = 'testString'
        relation_model_model['source'] = text_span_model
        relation_model_model['target'] = text_span_model

        data_model_model = {} # DataModel
        data_model_model['concepts'] = [concept_model_model]
        data_model_model['attributeValues'] = [concept_model_model]
        data_model_model['relations'] = [relation_model_model]
        data_model_model['mesh'] = [concept_model_model]
        data_model_model['text'] = [concept_model_model]

        unstructured_model_model = {} # UnstructuredModel
        unstructured_model_model['text'] = 'testString'
        unstructured_model_model['data'] = data_model_model

        # Construct a json representation of a CommonDataModel model
        common_data_model_model_json = {}
        common_data_model_model_json['unstructured'] = [unstructured_model_model]

        # Construct a model instance of CommonDataModel by calling from_dict on the json representation
        common_data_model_model = CommonDataModel.from_dict(common_data_model_model_json)
        assert common_data_model_model != False

        # Construct a model instance of CommonDataModel by calling from_dict on the json representation
        common_data_model_model_dict = CommonDataModel.from_dict(common_data_model_model_json).__dict__
        common_data_model_model2 = CommonDataModel(**common_data_model_model_dict)

        # Verify the model instances are equivalent
        assert common_data_model_model == common_data_model_model2

        # Convert model instance back to dict and verify no loss of data
        common_data_model_model_json2 = common_data_model_model.to_dict()
        assert common_data_model_model_json2 == common_data_model_model_json

#-----------------------------------------------------------------------------
# Test Class for Concept
#-----------------------------------------------------------------------------
class TestConcept():

    #--------------------------------------------------------
    # Test serialization/deserialization for Concept
    #--------------------------------------------------------
    def test_concept_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        count_model = {} # Count
        count_model['count'] = 38
        count_model['hits'] = 38

        # Construct a json representation of a Concept model
        concept_model_json = {}
        concept_model_json['ontology'] = 'testString'
        concept_model_json['cui'] = 'testString'
        concept_model_json['preferredName'] = 'testString'
        concept_model_json['alternativeName'] = 'testString'
        concept_model_json['semanticType'] = 'testString'
        concept_model_json['count'] = 38
        concept_model_json['hitCount'] = 38
        concept_model_json['score'] = 36.0
        concept_model_json['parents'] = count_model
        concept_model_json['children'] = count_model
        concept_model_json['siblings'] = count_model
        concept_model_json['related'] = count_model
        concept_model_json['documentIds'] = ['testString']
        concept_model_json['dataType'] = 'testString'
        concept_model_json['unit'] = 'testString'
        concept_model_json['operator'] = 'testString'
        concept_model_json['minValue'] = 'testString'
        concept_model_json['maxValue'] = 'testString'
        concept_model_json['vocab'] = 'testString'
        concept_model_json['properties'] = ['testString']

        # Construct a model instance of Concept by calling from_dict on the json representation
        concept_model = Concept.from_dict(concept_model_json)
        assert concept_model != False

        # Construct a model instance of Concept by calling from_dict on the json representation
        concept_model_dict = Concept.from_dict(concept_model_json).__dict__
        concept_model2 = Concept(**concept_model_dict)

        # Verify the model instances are equivalent
        assert concept_model == concept_model2

        # Convert model instance back to dict and verify no loss of data
        concept_model_json2 = concept_model.to_dict()
        assert concept_model_json2 == concept_model_json

#-----------------------------------------------------------------------------
# Test Class for ConceptInfoModel
#-----------------------------------------------------------------------------
class TestConceptInfoModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for ConceptInfoModel
    #--------------------------------------------------------
    def test_concept_info_model_serialization(self):

        # Construct a json representation of a ConceptInfoModel model
        concept_info_model_model_json = {}
        concept_info_model_model_json['cui'] = 'testString'
        concept_info_model_model_json['ontology'] = 'testString'
        concept_info_model_model_json['preferredName'] = 'testString'
        concept_info_model_model_json['semanticTypes'] = ['testString']
        concept_info_model_model_json['surfaceForms'] = ['testString']
        concept_info_model_model_json['definition'] = 'testString'
        concept_info_model_model_json['hasParents'] = True
        concept_info_model_model_json['hasChildren'] = True
        concept_info_model_model_json['hasSiblings'] = True

        # Construct a model instance of ConceptInfoModel by calling from_dict on the json representation
        concept_info_model_model = ConceptInfoModel.from_dict(concept_info_model_model_json)
        assert concept_info_model_model != False

        # Construct a model instance of ConceptInfoModel by calling from_dict on the json representation
        concept_info_model_model_dict = ConceptInfoModel.from_dict(concept_info_model_model_json).__dict__
        concept_info_model_model2 = ConceptInfoModel(**concept_info_model_model_dict)

        # Verify the model instances are equivalent
        assert concept_info_model_model == concept_info_model_model2

        # Convert model instance back to dict and verify no loss of data
        concept_info_model_model_json2 = concept_info_model_model.to_dict()
        assert concept_info_model_model_json2 == concept_info_model_model_json

#-----------------------------------------------------------------------------
# Test Class for ConceptListModel
#-----------------------------------------------------------------------------
class TestConceptListModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for ConceptListModel
    #--------------------------------------------------------
    def test_concept_list_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        artifact_model_model = {} # ArtifactModel
        artifact_model_model['cui'] = 'testString'
        artifact_model_model['ontology'] = 'testString'
        artifact_model_model['preferredName'] = 'testString'
        artifact_model_model['alternativeName'] = 'testString'
        artifact_model_model['semanticType'] = 'testString'
        artifact_model_model['rank'] = 38
        artifact_model_model['hitCount'] = 38
        artifact_model_model['score'] = 36.0
        artifact_model_model['surfaceForms'] = ['testString']

        # Construct a json representation of a ConceptListModel model
        concept_list_model_model_json = {}
        concept_list_model_model_json['concepts'] = [artifact_model_model]

        # Construct a model instance of ConceptListModel by calling from_dict on the json representation
        concept_list_model_model = ConceptListModel.from_dict(concept_list_model_model_json)
        assert concept_list_model_model != False

        # Construct a model instance of ConceptListModel by calling from_dict on the json representation
        concept_list_model_model_dict = ConceptListModel.from_dict(concept_list_model_model_json).__dict__
        concept_list_model_model2 = ConceptListModel(**concept_list_model_model_dict)

        # Verify the model instances are equivalent
        assert concept_list_model_model == concept_list_model_model2

        # Convert model instance back to dict and verify no loss of data
        concept_list_model_model_json2 = concept_list_model_model.to_dict()
        #assert concept_list_model_model_json2 == concept_list_model_model_json

#-----------------------------------------------------------------------------
# Test Class for ConceptModel
#-----------------------------------------------------------------------------
class TestConceptModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for ConceptModel
    #--------------------------------------------------------
    def test_concept_model_serialization(self):

        # Construct a json representation of a ConceptModel model
        concept_model_model_json = {}
        concept_model_model_json['uniqueId'] = 38
        concept_model_model_json['stickyIds'] = [38]
        concept_model_model_json['section'] = 'testString'
        concept_model_model_json['type'] = 'testString'
        concept_model_model_json['begin'] = 38
        concept_model_model_json['end'] = 38
        concept_model_model_json['coveredText'] = 'testString'
        concept_model_model_json['cui'] = 'testString'
        concept_model_model_json['preferredName'] = 'testString'
        concept_model_model_json['source'] = 'testString'
        concept_model_model_json['negated'] = True
        concept_model_model_json['hypothetical'] = True
        concept_model_model_json['timestamp'] = 26
        concept_model_model_json['attributeId'] = 'testString'
        concept_model_model_json['qualifiers'] = ['testString']
        concept_model_model_json['unit'] = 'testString'
        concept_model_model_json['minValue'] = 'testString'
        concept_model_model_json['maxValue'] = 'testString'
        concept_model_model_json['operator'] = 'testString'
        concept_model_model_json['features'] = {}
        concept_model_model_json['nluEntityIndex'] = 'testString'
        concept_model_model_json['nluMentionIndex'] = 'testString'
        concept_model_model_json['nluRelationId'] = 'testString'
        concept_model_model_json['nluSide'] = 'testString'
        concept_model_model_json['nluSourceType'] = 'testString'
        concept_model_model_json['nluRelation'] = 'testString'
        concept_model_model_json['nluTargetType'] = 'testString'
        concept_model_model_json['hits'] = 38

        # Construct a model instance of ConceptModel by calling from_dict on the json representation
        concept_model_model = ConceptModel.from_dict(concept_model_model_json)
        assert concept_model_model != False

        # Construct a model instance of ConceptModel by calling from_dict on the json representation
        concept_model_model_dict = ConceptModel.from_dict(concept_model_model_json).__dict__
        concept_model_model2 = ConceptModel(**concept_model_model_dict)

        # Verify the model instances are equivalent
        assert concept_model_model == concept_model_model2

        # Convert model instance back to dict and verify no loss of data
        concept_model_model_json2 = concept_model_model.to_dict()
        assert concept_model_model_json2 == concept_model_model_json

#-----------------------------------------------------------------------------
# Test Class for CorporaConfig
#-----------------------------------------------------------------------------
class TestCorporaConfig():

    #--------------------------------------------------------
    # Test serialization/deserialization for CorporaConfig
    #--------------------------------------------------------
    def test_corpora_config_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        corpus_model_model = {} # CorpusModel
        corpus_model_model['corpusName'] = 'testString'
        corpus_model_model['ontologies'] = ['testString']
        corpus_model_model['descriptiveName'] = 'testString'
        corpus_model_model['bvt'] = True
        corpus_model_model['elasticsearchIndex'] = 'testString'

        # Construct a json representation of a CorporaConfig model
        corpora_config_model_json = {}
        corpora_config_model_json['corpora'] = [corpus_model_model]

        # Construct a model instance of CorporaConfig by calling from_dict on the json representation
        corpora_config_model = CorporaConfigModel.from_dict(corpora_config_model_json)
        assert corpora_config_model != False

        # Construct a model instance of CorporaConfig by calling from_dict on the json representation
        corpora_config_model_dict = CorporaConfigModel.from_dict(corpora_config_model_json).__dict__
        corpora_config_model2 = CorporaConfigModel(**corpora_config_model_dict)

        # Verify the model instances are equivalent
        assert corpora_config_model == corpora_config_model2

        # Convert model instance back to dict and verify no loss of data
        corpora_config_model_json2 = corpora_config_model.to_dict()
        assert corpora_config_model_json2 == corpora_config_model_json

#-----------------------------------------------------------------------------
# Test Class for CorpusModel
#-----------------------------------------------------------------------------
class TestCorpusModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for CorpusModel
    #--------------------------------------------------------
    def test_corpus_model_serialization(self):

        # Construct a json representation of a CorpusModel model
        corpus_model_model_json = {}
        corpus_model_model_json['corpusName'] = 'testString'
        corpus_model_model_json['ontologies'] = ['testString']
        corpus_model_model_json['descriptiveName'] = 'testString'
        corpus_model_model_json['bvt'] = True
        corpus_model_model_json['elasticsearchIndex'] = 'testString'

        # Construct a model instance of CorpusModel by calling from_dict on the json representation
        corpus_model_model = CorpusModel.from_dict(corpus_model_model_json)
        assert corpus_model_model != False

        # Construct a model instance of CorpusModel by calling from_dict on the json representation
        corpus_model_model_dict = CorpusModel.from_dict(corpus_model_model_json).__dict__
        corpus_model_model2 = CorpusModel(**corpus_model_model_dict)

        # Verify the model instances are equivalent
        assert corpus_model_model == corpus_model_model2

        # Convert model instance back to dict and verify no loss of data
        corpus_model_model_json2 = corpus_model_model.to_dict()
        assert corpus_model_model_json2 == corpus_model_model_json

#-----------------------------------------------------------------------------
# Test Class for Count
#-----------------------------------------------------------------------------
class TestCount():

    #--------------------------------------------------------
    # Test serialization/deserialization for Count
    #--------------------------------------------------------
    def test_count_serialization(self):

        # Construct a json representation of a Count model
        count_model_json = {}
        count_model_json['count'] = 38
        count_model_json['hits'] = 38

        # Construct a model instance of Count by calling from_dict on the json representation
        count_model = Count.from_dict(count_model_json)
        assert count_model != False

        # Construct a model instance of Count by calling from_dict on the json representation
        count_model_dict = Count.from_dict(count_model_json).__dict__
        count_model2 = Count(**count_model_dict)

        # Verify the model instances are equivalent
        assert count_model == count_model2

        # Convert model instance back to dict and verify no loss of data
        count_model_json2 = count_model.to_dict()
        assert count_model_json2 == count_model_json

#-----------------------------------------------------------------------------
# Test Class for DataModel
#-----------------------------------------------------------------------------
class TestDataModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for DataModel
    #--------------------------------------------------------
    def test_data_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        text_span_model = {} # TextSpan
        text_span_model['section'] = 'testString'
        text_span_model['begin'] = 38
        text_span_model['end'] = 38
        text_span_model['coveredText'] = 'testString'
        text_span_model['source'] = 'testString'
        text_span_model['type'] = 'testString'

        concept_model_model = {} # ConceptModel
        concept_model_model['uniqueId'] = 38
        concept_model_model['stickyIds'] = [38]
        concept_model_model['section'] = 'testString'
        concept_model_model['type'] = 'testString'
        concept_model_model['begin'] = 38
        concept_model_model['end'] = 38
        concept_model_model['coveredText'] = 'testString'
        concept_model_model['cui'] = 'testString'
        concept_model_model['preferredName'] = 'testString'
        concept_model_model['source'] = 'testString'
        concept_model_model['negated'] = True
        concept_model_model['hypothetical'] = True
        concept_model_model['timestamp'] = 26
        concept_model_model['attributeId'] = 'testString'
        concept_model_model['qualifiers'] = ['testString']
        concept_model_model['unit'] = 'testString'
        concept_model_model['minValue'] = 'testString'
        concept_model_model['maxValue'] = 'testString'
        concept_model_model['operator'] = 'testString'
        concept_model_model['features'] = {}
        concept_model_model['nluEntityIndex'] = 'testString'
        concept_model_model['nluMentionIndex'] = 'testString'
        concept_model_model['nluRelationId'] = 'testString'
        concept_model_model['nluSide'] = 'testString'
        concept_model_model['nluSourceType'] = 'testString'
        concept_model_model['nluRelation'] = 'testString'
        concept_model_model['nluTargetType'] = 'testString'
        concept_model_model['hits'] = 38

        relation_model_model = {} # RelationModel
        relation_model_model['relationId'] = 'testString'
        relation_model_model['relation'] = 'testString'
        relation_model_model['source'] = text_span_model
        relation_model_model['target'] = text_span_model

        # Construct a json representation of a DataModel model
        data_model_model_json = {}
        data_model_model_json['concepts'] = [concept_model_model]
        data_model_model_json['attributeValues'] = [concept_model_model]
        data_model_model_json['relations'] = [relation_model_model]
        data_model_model_json['mesh'] = [concept_model_model]
        data_model_model_json['text'] = [concept_model_model]

        # Construct a model instance of DataModel by calling from_dict on the json representation
        data_model_model = DataModel.from_dict(data_model_model_json)
        assert data_model_model != False

        # Construct a model instance of DataModel by calling from_dict on the json representation
        data_model_model_dict = DataModel.from_dict(data_model_model_json).__dict__
        data_model_model2 = DataModel(**data_model_model_dict)

        # Verify the model instances are equivalent
        assert data_model_model == data_model_model2

        # Convert model instance back to dict and verify no loss of data
        data_model_model_json2 = data_model_model.to_dict()
        assert data_model_model_json2 == data_model_model_json

#-----------------------------------------------------------------------------
# Test Class for EntryModel
#-----------------------------------------------------------------------------
class TestEntryModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for EntryModel
    #--------------------------------------------------------
    def test_entry_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        string_builder_model = {} # StringBuilder

        sentence_model_model = {} # SentenceModel
        sentence_model_model['documentSection'] = 'testString'
        sentence_model_model['text'] = string_builder_model
        sentence_model_model['begin'] = 38
        sentence_model_model['end'] = 38
        sentence_model_model['timestamp'] = 26

        # Construct a json representation of a EntryModel model
        entry_model_model_json = {}
        entry_model_model_json['id'] = 'testString'
        entry_model_model_json['negated'] = True
        entry_model_model_json['sentences'] = [sentence_model_model]

        # Construct a model instance of EntryModel by calling from_dict on the json representation
        entry_model_model = EntryModel.from_dict(entry_model_model_json)
        assert entry_model_model != False

        # Construct a model instance of EntryModel by calling from_dict on the json representation
        entry_model_model_dict = EntryModel.from_dict(entry_model_model_json).__dict__
        entry_model_model2 = EntryModel(**entry_model_model_dict)

        # Verify the model instances are equivalent
        assert entry_model_model == entry_model_model2

        # Convert model instance back to dict and verify no loss of data
        entry_model_model_json2 = entry_model_model.to_dict()
        assert entry_model_model_json2 == entry_model_model_json

#-----------------------------------------------------------------------------
# Test Class for FieldOptions
#-----------------------------------------------------------------------------
class TestFieldOptions():

    #--------------------------------------------------------
    # Test serialization/deserialization for FieldOptions
    #--------------------------------------------------------
    def test_field_options_serialization(self):

        # Construct a json representation of a FieldOptions model
        field_options_model_json = {}
        field_options_model_json['supports'] = ['testString']

        # Construct a model instance of FieldOptions by calling from_dict on the json representation
        field_options_model = FieldOptions.from_dict(field_options_model_json)
        assert field_options_model != False

        # Construct a model instance of FieldOptions by calling from_dict on the json representation
        field_options_model_dict = FieldOptions.from_dict(field_options_model_json).__dict__
        field_options_model2 = FieldOptions(**field_options_model_dict)

        # Verify the model instances are equivalent
        assert field_options_model == field_options_model2

        # Convert model instance back to dict and verify no loss of data
        field_options_model_json2 = field_options_model.to_dict()
#        assert field_options_model_json2 == field_options_model_json

#-----------------------------------------------------------------------------
# Test Class for HistogramData
#-----------------------------------------------------------------------------
class TestHistogramData():

    #--------------------------------------------------------
    # Test serialization/deserialization for HistogramData
    #--------------------------------------------------------
    def test_histogram_data_serialization(self):

        # Construct a json representation of a HistogramData model
        histogram_data_model_json = {}
        histogram_data_model_json['date'] = 'testString'
        histogram_data_model_json['hits'] = 38

        # Construct a model instance of HistogramData by calling from_dict on the json representation
        histogram_data_model = HistogramData.from_dict(histogram_data_model_json)
        assert histogram_data_model != False

        # Construct a model instance of HistogramData by calling from_dict on the json representation
        histogram_data_model_dict = HistogramData.from_dict(histogram_data_model_json).__dict__
        histogram_data_model2 = HistogramData(**histogram_data_model_dict)

        # Verify the model instances are equivalent
        assert histogram_data_model == histogram_data_model2

        # Convert model instance back to dict and verify no loss of data
        histogram_data_model_json2 = histogram_data_model.to_dict()
        assert histogram_data_model_json2 == histogram_data_model_json

#-----------------------------------------------------------------------------
# Test Class for HitCount
#-----------------------------------------------------------------------------
class TestHitCount():

    #--------------------------------------------------------
    # Test serialization/deserialization for HitCount
    #--------------------------------------------------------
    def test_hit_count_serialization(self):

        # Construct a json representation of a HitCount model
        hit_count_model_json = {}
        hit_count_model_json['hitCount'] = 38

        # Construct a model instance of HitCount by calling from_dict on the json representation
        hit_count_model = HitCount.from_dict(hit_count_model_json)
        assert hit_count_model != False

        # Construct a model instance of HitCount by calling from_dict on the json representation
        hit_count_model_dict = HitCount.from_dict(hit_count_model_json).__dict__
        hit_count_model2 = HitCount(**hit_count_model_dict)

        # Verify the model instances are equivalent
        assert hit_count_model == hit_count_model2

        # Convert model instance back to dict and verify no loss of data
        hit_count_model_json2 = hit_count_model.to_dict()
        assert hit_count_model_json2 == hit_count_model_json


#-----------------------------------------------------------------------------
# Test Class for MetadataModel
#-----------------------------------------------------------------------------
class TestMetadataModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for MetadataModel
    #--------------------------------------------------------
    def test_metadata_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        field_options_model = {} # FieldOptions
        field_options_model['supports'] = ['testString']

        # Construct a json representation of a MetadataModel model
        metadata_model_model_json = {}
        metadata_model_model_json['fields'] = {}
        metadata_model_model_json['sectionFieldNames'] = ['testString']
        metadata_model_model_json['attrSectionFieldNames'] = ['testString']
        metadata_model_model_json['qualifierSectionFieldNames'] = ['testString']
        metadata_model_model_json['meshSectionFieldNames'] = ['testString']
        metadata_model_model_json['fieldIndexMap'] = {}

        # Construct a model instance of MetadataModel by calling from_dict on the json representation
        metadata_model_model = MetadataFields.from_dict(metadata_model_model_json)
        assert metadata_model_model != False

        # Construct a model instance of MetadataModel by calling from_dict on the json representation
        metadata_model_model_dict = MetadataFields.from_dict(metadata_model_model_json).__dict__
        metadata_model_model2 = MetadataFields(**metadata_model_model_dict)

        # Verify the model instances are equivalent
        assert metadata_model_model == metadata_model_model2

        # Convert model instance back to dict and verify no loss of data
        metadata_model_model_json2 = metadata_model_model.to_dict()
#        assert metadata_model_model_json2 == metadata_model_model_json

#-----------------------------------------------------------------------------
# Test Class for Passage
#-----------------------------------------------------------------------------
class TestPassage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Passage
    #--------------------------------------------------------
    def test_passage_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        string_builder_model = {} # StringBuilder

        # Construct a json representation of a Passage model
        passage_model_json = {}
        passage_model_json['documentSection'] = 'testString'
        passage_model_json['text'] = string_builder_model
        passage_model_json['timestamp'] = 26
        passage_model_json['preferredName'] = 'testString'

        # Construct a model instance of Passage by calling from_dict on the json representation
        passage_model = Passage.from_dict(passage_model_json)
        assert passage_model != False

        # Construct a model instance of Passage by calling from_dict on the json representation
        passage_model_dict = Passage.from_dict(passage_model_json).__dict__
        passage_model2 = Passage(**passage_model_dict)

        # Verify the model instances are equivalent
        assert passage_model == passage_model2

        # Convert model instance back to dict and verify no loss of data
        passage_model_json2 = passage_model.to_dict()
        assert passage_model_json2 == passage_model_json

#-----------------------------------------------------------------------------
# Test Class for Qualifer
#-----------------------------------------------------------------------------
class TestQualifer():

    #--------------------------------------------------------
    # Test serialization/deserialization for Qualifer
    #--------------------------------------------------------
    def test_qualifer_serialization(self):

        # Construct a json representation of a Qualifer model
        qualifer_model_json = {}
        qualifer_model_json['id'] = 'testString'
        qualifer_model_json['name'] = 'testString'

        # Construct a model instance of Qualifer by calling from_dict on the json representation
        qualifer_model = Qualifier.from_dict(qualifer_model_json)
        assert qualifer_model != False

        # Construct a model instance of Qualifer by calling from_dict on the json representation
        qualifer_model_dict = Qualifier.from_dict(qualifer_model_json).__dict__
        qualifer_model2 = Qualifier(**qualifer_model_dict)

        # Verify the model instances are equivalent
        assert qualifer_model == qualifer_model2

        # Convert model instance back to dict and verify no loss of data
        qualifer_model_json2 = qualifer_model.to_dict()
        assert qualifer_model_json2 == qualifer_model_json

#-----------------------------------------------------------------------------
# Test Class for RangeModel
#-----------------------------------------------------------------------------
class TestRangeModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for RangeModel
    #--------------------------------------------------------
    def test_range_model_serialization(self):

        # Construct a json representation of a RangeModel model
        range_model_model_json = {}
        range_model_model_json['operator'] = 'testString'
        range_model_model_json['min'] = 'testString'
        range_model_model_json['max'] = 'testString'
        range_model_model_json['count'] = 38

        # Construct a model instance of RangeModel by calling from_dict on the json representation
        range_model_model = RangeModel.from_dict(range_model_model_json)
        assert range_model_model != False

        # Construct a model instance of RangeModel by calling from_dict on the json representation
        range_model_model_dict = RangeModel.from_dict(range_model_model_json).__dict__
        range_model_model2 = RangeModel(**range_model_model_dict)

        # Verify the model instances are equivalent
        assert range_model_model == range_model_model2

        # Convert model instance back to dict and verify no loss of data
        range_model_model_json2 = range_model_model.to_dict()
        assert range_model_model_json2 == range_model_model_json

#-----------------------------------------------------------------------------
# Test Class for RankedDocument
#-----------------------------------------------------------------------------
class TestRankedDocument():

    #--------------------------------------------------------
    # Test serialization/deserialization for RankedDocument
    #--------------------------------------------------------
    def test_ranked_document_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        string_builder_model = {} # StringBuilder

        passage_model = {} # Passage
        passage_model['documentSection'] = 'testString'
        passage_model['text'] = string_builder_model
        passage_model['timestamp'] = 26
        passage_model['preferredName'] = 'testString'

        annotation_model_model = {} # AnnotationModel
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        passages_model_model = {} # PassagesModel
        passages_model_model['allPassages'] = [passage_model]
        passages_model_model['searchTermToPassages'] = {}

        ranked_doc_links_model = {} # RankedDocLinks
        ranked_doc_links_model['hrefSearchMatches'] = 'testString'
        ranked_doc_links_model['hrefCategories'] = 'testString'

        # Construct a json representation of a RankedDocument model
        ranked_document_model_json = {}
        ranked_document_model_json['documentId'] = 'testString'
        ranked_document_model_json['title'] = 'testString'
        ranked_document_model_json['metadata'] = {}
        ranked_document_model_json['sectionName'] = 'testString'
        ranked_document_model_json['sectionId'] = 'testString'
        ranked_document_model_json['corpus'] = 'testString'
        ranked_document_model_json['links'] = ranked_doc_links_model
        ranked_document_model_json['passages'] = passages_model_model
        ranked_document_model_json['annotations'] = {}

        # Construct a model instance of RankedDocument by calling from_dict on the json representation
        ranked_document_model = RankedDocument.from_dict(ranked_document_model_json)
        assert ranked_document_model != False

        # Construct a model instance of RankedDocument by calling from_dict on the json representation
        ranked_document_model_dict = RankedDocument.from_dict(ranked_document_model_json).__dict__
        ranked_document_model2 = RankedDocument(**ranked_document_model_dict)

        # Verify the model instances are equivalent
        assert ranked_document_model == ranked_document_model2

        # Convert model instance back to dict and verify no loss of data
        ranked_document_model_json2 = ranked_document_model.to_dict()
        assert ranked_document_model_json2 == ranked_document_model_json

#-----------------------------------------------------------------------------
# Test Class for RelatedConceptModel
#-----------------------------------------------------------------------------
class TestRelatedConceptModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for RelatedConceptModel
    #--------------------------------------------------------
    def test_related_concept_model_serialization(self):

        # Construct a json representation of a RelatedConceptModel model
        related_concept_model_model_json = {}
        related_concept_model_model_json['cui'] = 'testString'
        related_concept_model_model_json['ontology'] = 'testString'
        related_concept_model_model_json['preferredName'] = 'testString'
        related_concept_model_model_json['alternativeName'] = 'testString'
        related_concept_model_model_json['semanticType'] = 'testString'
        related_concept_model_model_json['rank'] = 38
        related_concept_model_model_json['hitCount'] = 38
        related_concept_model_model_json['score'] = 36.0
        related_concept_model_model_json['surfaceForms'] = ['testString']

        # Construct a model instance of RelatedConceptModel by calling from_dict on the json representation
        related_concept_model_model = RelatedConceptModel.from_dict(related_concept_model_model_json)
        assert related_concept_model_model != False

        # Construct a model instance of RelatedConceptModel by calling from_dict on the json representation
        related_concept_model_model_dict = RelatedConceptModel.from_dict(related_concept_model_model_json).__dict__
        related_concept_model_model2 = RelatedConceptModel(**related_concept_model_model_dict)

        # Verify the model instances are equivalent
        assert related_concept_model_model == related_concept_model_model2

        # Convert model instance back to dict and verify no loss of data
        related_concept_model_model_json2 = related_concept_model_model.to_dict()
        assert related_concept_model_model_json2 == related_concept_model_model_json

#-----------------------------------------------------------------------------
# Test Class for RelatedConceptsModel
#-----------------------------------------------------------------------------
class TestRelatedConceptsModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for RelatedConceptsModel
    #--------------------------------------------------------
    def test_related_concepts_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        related_concept_model_model = {} # RelatedConceptModel
        related_concept_model_model['cui'] = 'testString'
        related_concept_model_model['ontology'] = 'testString'
        related_concept_model_model['preferredName'] = 'testString'
        related_concept_model_model['alternativeName'] = 'testString'
        related_concept_model_model['semanticType'] = 'testString'
        related_concept_model_model['rank'] = 38
        related_concept_model_model['hitCount'] = 38
        related_concept_model_model['score'] = 36.0
        related_concept_model_model['surfaceForms'] = ['testString']

        # Construct a json representation of a RelatedConceptsModel model
        related_concepts_model_model_json = {}
        related_concepts_model_model_json['concepts'] = [related_concept_model_model]

        # Construct a model instance of RelatedConceptsModel by calling from_dict on the json representation
        related_concepts_model_model = RelatedConceptsModel.from_dict(related_concepts_model_model_json)
        assert related_concepts_model_model != False

        # Construct a model instance of RelatedConceptsModel by calling from_dict on the json representation
        related_concepts_model_model_dict = RelatedConceptsModel.from_dict(related_concepts_model_model_json).__dict__
        related_concepts_model_model2 = RelatedConceptsModel(**related_concepts_model_model_dict)

        # Verify the model instances are equivalent
        assert related_concepts_model_model == related_concepts_model_model2

        # Convert model instance back to dict and verify no loss of data
        related_concepts_model_model_json2 = related_concepts_model_model.to_dict()
        assert related_concepts_model_model_json2 == related_concepts_model_model_json

#-----------------------------------------------------------------------------
# Test Class for RelationModel
#-----------------------------------------------------------------------------
class TestRelationModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for RelationModel
    #--------------------------------------------------------
    def test_relation_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        text_span_model = {} # TextSpan
        text_span_model['section'] = 'testString'
        text_span_model['begin'] = 38
        text_span_model['end'] = 38
        text_span_model['coveredText'] = 'testString'
        text_span_model['source'] = 'testString'
        text_span_model['type'] = 'testString'

        # Construct a json representation of a RelationModel model
        relation_model_model_json = {}
        relation_model_model_json['relationId'] = 'testString'
        relation_model_model_json['relation'] = 'testString'
        relation_model_model_json['source'] = text_span_model
        relation_model_model_json['target'] = text_span_model

        # Construct a model instance of RelationModel by calling from_dict on the json representation
        relation_model_model = RelationModel.from_dict(relation_model_model_json)
        assert relation_model_model != False

        # Construct a model instance of RelationModel by calling from_dict on the json representation
        relation_model_model_dict = RelationModel.from_dict(relation_model_model_json).__dict__
        relation_model_model2 = RelationModel(**relation_model_model_dict)

        # Verify the model instances are equivalent
        assert relation_model_model == relation_model_model2

        # Convert model instance back to dict and verify no loss of data
        relation_model_model_json2 = relation_model_model.to_dict()
        assert relation_model_model_json2 == relation_model_model_json

#-----------------------------------------------------------------------------
# Test Class for SearchMatchesModel
#-----------------------------------------------------------------------------
class TestSearchMatchesModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for SearchMatchesModel
    #--------------------------------------------------------
    def test_search_matches_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        annotation_model_model = {} # AnnotationModel
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        string_builder_model = {} # StringBuilder

        # Construct a json representation of a SearchMatchesModel model
        search_matches_model_model_json = {}
        search_matches_model_model_json['externalId'] = 'testString'
        search_matches_model_model_json['documentId'] = 'testString'
        search_matches_model_model_json['parentDocumentId'] = 'testString'
        search_matches_model_model_json['publicationName'] = 'testString'
        search_matches_model_model_json['publicationDate'] = 'testString'
        search_matches_model_model_json['publicationURL'] = 'testString'
        search_matches_model_model_json['authors'] = ['testString']
        search_matches_model_model_json['title'] = 'testString'
        search_matches_model_model_json['medlineLicense'] = 'testString'
        search_matches_model_model_json['hrefPubMed'] = 'testString'
        search_matches_model_model_json['hrefPmc'] = 'testString'
        search_matches_model_model_json['hrefDoi'] = 'testString'
        search_matches_model_model_json['pdfUrl'] = 'testString'
        search_matches_model_model_json['referenceUrl'] = 'testString'
        search_matches_model_model_json['highlightedTitle'] = string_builder_model
        search_matches_model_model_json['highlightedAbstract'] = string_builder_model
        search_matches_model_model_json['highlightedBody'] = string_builder_model
        search_matches_model_model_json['highlightedSections'] = {}
        search_matches_model_model_json['passages'] = {}
        search_matches_model_model_json['annotations'] = {}

        # Construct a model instance of SearchMatchesModel by calling from_dict on the json representation
        search_matches_model_model = SearchMatchesModel.from_dict(search_matches_model_model_json)
        assert search_matches_model_model != False

        # Construct a model instance of SearchMatchesModel by calling from_dict on the json representation
        search_matches_model_model_dict = SearchMatchesModel.from_dict(search_matches_model_model_json).__dict__
        search_matches_model_model2 = SearchMatchesModel(**search_matches_model_model_dict)

        # Verify the model instances are equivalent
        assert search_matches_model_model == search_matches_model_model2

        # Convert model instance back to dict and verify no loss of data
        search_matches_model_model_json2 = search_matches_model_model.to_dict()
        assert search_matches_model_model_json2 == search_matches_model_model_json

#-----------------------------------------------------------------------------
# Test Class for SearchModel
#-----------------------------------------------------------------------------
class TestSearchModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for SearchModel
    #--------------------------------------------------------
    def test_search_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        text_span_model = {} # TextSpan
        text_span_model['section'] = 'testString'
        text_span_model['begin'] = 38
        text_span_model['end'] = 38
        text_span_model['coveredText'] = 'testString'
        text_span_model['source'] = 'testString'
        text_span_model['type'] = 'testString'

        concept_model_model = {} # ConceptModel
        concept_model_model['uniqueId'] = 38
        concept_model_model['stickyIds'] = [38]
        concept_model_model['section'] = 'testString'
        concept_model_model['type'] = 'testString'
        concept_model_model['begin'] = 38
        concept_model_model['end'] = 38
        concept_model_model['coveredText'] = 'testString'
        concept_model_model['cui'] = 'testString'
        concept_model_model['preferredName'] = 'testString'
        concept_model_model['source'] = 'testString'
        concept_model_model['negated'] = True
        concept_model_model['hypothetical'] = True
        concept_model_model['timestamp'] = 26
        concept_model_model['attributeId'] = 'testString'
        concept_model_model['qualifiers'] = ['testString']
        concept_model_model['unit'] = 'testString'
        concept_model_model['minValue'] = 'testString'
        concept_model_model['maxValue'] = 'testString'
        concept_model_model['operator'] = 'testString'
        concept_model_model['features'] = {}
        concept_model_model['nluEntityIndex'] = 'testString'
        concept_model_model['nluMentionIndex'] = 'testString'
        concept_model_model['nluRelationId'] = 'testString'
        concept_model_model['nluSide'] = 'testString'
        concept_model_model['nluSourceType'] = 'testString'
        concept_model_model['nluRelation'] = 'testString'
        concept_model_model['nluTargetType'] = 'testString'
        concept_model_model['hits'] = 38

        relation_model_model = {} # RelationModel
        relation_model_model['relationId'] = 'testString'
        relation_model_model['relation'] = 'testString'
        relation_model_model['source'] = text_span_model
        relation_model_model['target'] = text_span_model

        string_builder_model = {} # StringBuilder

        data_model_model = {} # DataModel
        data_model_model['concepts'] = [concept_model_model]
        data_model_model['attributeValues'] = [concept_model_model]
        data_model_model['relations'] = [relation_model_model]
        data_model_model['mesh'] = [concept_model_model]
        data_model_model['text'] = [concept_model_model]

        passage_model = {} # Passage
        passage_model['documentSection'] = 'testString'
        passage_model['text'] = string_builder_model
        passage_model['timestamp'] = 26
        passage_model['preferredName'] = 'testString'

        annotation_model_model = {} # AnnotationModel
        annotation_model_model['uniqueId'] = 38
        annotation_model_model['stickyIds'] = [38]
        annotation_model_model['ontology'] = 'testString'
        annotation_model_model['section'] = 'testString'
        annotation_model_model['preferredName'] = 'testString'
        annotation_model_model['cui'] = 'testString'
        annotation_model_model['attributeId'] = 'testString'
        annotation_model_model['qualifiers'] = ['testString']
        annotation_model_model['type'] = 'testString'
        annotation_model_model['negated'] = True
        annotation_model_model['hypothetical'] = True
        annotation_model_model['unit'] = 'testString'
        annotation_model_model['minValue'] = 'testString'
        annotation_model_model['maxValue'] = 'testString'
        annotation_model_model['operator'] = 'testString'
        annotation_model_model['nluSourceType'] = 'testString'
        annotation_model_model['nluRelation'] = 'testString'
        annotation_model_model['nluTargetType'] = 'testString'
        annotation_model_model['nluEntityIndex'] = 'testString'
        annotation_model_model['nluMentionIndex'] = 'testString'
        annotation_model_model['nluRelationId'] = 'testString'
        annotation_model_model['nluSide'] = 'testString'
        annotation_model_model['begin'] = 38
        annotation_model_model['end'] = 38
        annotation_model_model['score'] = 36.0
        annotation_model_model['timestamp'] = 26
        annotation_model_model['features'] = {}
        annotation_model_model['hits'] = 38

        bool_operand_model = {} # BoolOperand
        bool_operand_model['boolOperand'] = 'testString'

        count_model = {} # Count
        count_model['count'] = 38
        count_model['hits'] = 38

        message_model = {} # Message
        message_model['messageType'] = 'expanded_request'
        message_model['url'] = 'testString'
        message_model['request'] = { 'foo': 'bar' }
        message_model['headers'] = ['testString']
        message_model['status'] = 38
        message_model['response'] = { 'foo': 'bar' }

        passages_model_model = {} # PassagesModel
        passages_model_model['allPassages'] = [passage_model]
        passages_model_model['searchTermToPassages'] = {}

        ranked_doc_links_model = {} # RankedDocLinks
        ranked_doc_links_model['hrefSearchMatches'] = 'testString'
        ranked_doc_links_model['hrefCategories'] = 'testString'

        unstructured_model_model = {} # UnstructuredModel
        unstructured_model_model['text'] = 'testString'
        unstructured_model_model['data'] = data_model_model

        attribute_model = {} # Attribute
        attribute_model['attributeId'] = 'testString'
        attribute_model['displayName'] = 'testString'
        attribute_model['count'] = 38

        backend_model = {} # Backend
        backend_model['messages'] = [message_model]

        boolean_operands_model = {} # BooleanOperands
        boolean_operands_model['boolExpression'] = 'testString'
        boolean_operands_model['boolOperands'] = [bool_operand_model]

        common_data_model_model = {} # CommonDataModel
        common_data_model_model['unstructured'] = [unstructured_model_model]

        concept_model = {} # Concept
        concept_model['ontology'] = 'testString'
        concept_model['cui'] = 'testString'
        concept_model['preferredName'] = 'testString'
        concept_model['alternativeName'] = 'testString'
        concept_model['semanticType'] = 'testString'
        concept_model['count'] = 38
        concept_model['hitCount'] = 38
        concept_model['score'] = 36.0
        concept_model['parents'] = count_model
        concept_model['children'] = count_model
        concept_model['siblings'] = count_model
        concept_model['related'] = count_model
        concept_model['documentIds'] = ['testString']
        concept_model['dataType'] = 'testString'
        concept_model['unit'] = 'testString'
        concept_model['operator'] = 'testString'
        concept_model['minValue'] = 'testString'
        concept_model['maxValue'] = 'testString'
        concept_model['vocab'] = 'testString'
        concept_model['properties'] = ['testString']

        metadata_fields_model = {} # MetadataFields
        metadata_fields_model['corpus'] = 'testString'
        metadata_fields_model['corpusDescription'] = 'testString'
        metadata_fields_model['fields'] = {}

        qualifer_model = {} # Qualifer
        qualifer_model['id'] = 'testString'
        qualifer_model['name'] = 'testString'

        range_model_model = {} # RangeModel
        range_model_model['operator'] = 'testString'
        range_model_model['min'] = 'testString'
        range_model_model['max'] = 'testString'
        range_model_model['count'] = 38

        ranked_document_model = {} # RankedDocument
        ranked_document_model['documentId'] = 'testString'
        ranked_document_model['title'] = 'testString'
        ranked_document_model['metadata'] = {}
        ranked_document_model['sectionName'] = 'testString'
        ranked_document_model['sectionId'] = 'testString'
        ranked_document_model['corpus'] = 'testString'
        ranked_document_model['links'] = ranked_doc_links_model
        ranked_document_model['passages'] = passages_model_model
        ranked_document_model['annotations'] = {}

        # Construct a json representation of a SearchModel model
        search_model_model_json = {}
        search_model_model_json['href'] = 'testString'
        search_model_model_json['pageNumber'] = 38
        search_model_model_json['get_limit'] = 38
        search_model_model_json['totalDocumentCount'] = 38
        search_model_model_json['concepts'] = [concept_model]
        search_model_model_json['types'] = ['testString']
        search_model_model_json['attributes'] = [attribute_model]
        search_model_model_json['values'] = [concept_model]
        search_model_model_json['ranges'] = {}
        search_model_model_json['typeahead'] = [concept_model]
        search_model_model_json['aggregations'] = {}
        search_model_model_json['dateHistograms'] = {}
        search_model_model_json['qualifiers'] = [qualifer_model]
        search_model_model_json['backend'] = backend_model
        search_model_model_json['expandedQuery'] = { 'foo': 'bar' }
        search_model_model_json['parsedBoolExpression'] = boolean_operands_model
        search_model_model_json['conceptsExist'] = {}
        search_model_model_json['cursorId'] = 'testString'
        search_model_model_json['vocabs'] = ['testString']
        search_model_model_json['annotations'] = {}
        search_model_model_json['metadata'] = metadata_fields_model
        search_model_model_json['documents'] = [ranked_document_model]

        # Construct a model instance of SearchModel by calling from_dict on the json representation
        search_model_model = SearchModel.from_dict(search_model_model_json)
        assert search_model_model != False

        # Construct a model instance of SearchModel by calling from_dict on the json representation
        search_model_model_dict = SearchModel.from_dict(search_model_model_json).__dict__
        search_model_model2 = SearchModel(**search_model_model_dict)

        # Verify the model instances are equivalent
        assert search_model_model == search_model_model2

        # Convert model instance back to dict and verify no loss of data
        search_model_model_json2 = search_model_model.to_dict()
        assert search_model_model_json2 == search_model_model_json

#-----------------------------------------------------------------------------
# Test Class for SentenceModel
#-----------------------------------------------------------------------------
class TestSentenceModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for SentenceModel
    #--------------------------------------------------------
    def test_sentence_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        string_builder_model = {} # StringBuilder

        # Construct a json representation of a SentenceModel model
        sentence_model_model_json = {}
        sentence_model_model_json['documentSection'] = 'testString'
        sentence_model_model_json['text'] = string_builder_model
        sentence_model_model_json['begin'] = 38
        sentence_model_model_json['end'] = 38
        sentence_model_model_json['timestamp'] = 26

        # Construct a model instance of SentenceModel by calling from_dict on the json representation
        sentence_model_model = SentenceModel.from_dict(sentence_model_model_json)
        assert sentence_model_model != False

        # Construct a model instance of SentenceModel by calling from_dict on the json representation
        sentence_model_model_dict = SentenceModel.from_dict(sentence_model_model_json).__dict__
        sentence_model_model2 = SentenceModel(**sentence_model_model_dict)

        # Verify the model instances are equivalent
        assert sentence_model_model == sentence_model_model2

        # Convert model instance back to dict and verify no loss of data
        sentence_model_model_json2 = sentence_model_model.to_dict()
        assert sentence_model_model_json2 == sentence_model_model_json

#-----------------------------------------------------------------------------
# Test Class for ServiceStatus
#-----------------------------------------------------------------------------
class TestServiceStatus():

    #--------------------------------------------------------
    # Test serialization/deserialization for ServiceStatus
    #--------------------------------------------------------
    def test_service_status_serialization(self):

        # Construct a json representation of a ServiceStatus model
        service_status_model_json = {}
        service_status_model_json['serviceState'] = 'OK'
        service_status_model_json['stateDetails'] = 'testString'

        # Construct a model instance of ServiceStatus by calling from_dict on the json representation
        service_status_model = ServiceStatus.from_dict(service_status_model_json)
        assert service_status_model != False

        # Construct a model instance of ServiceStatus by calling from_dict on the json representation
        service_status_model_dict = ServiceStatus.from_dict(service_status_model_json).__dict__
        service_status_model2 = ServiceStatus(**service_status_model_dict)

        # Verify the model instances are equivalent
        assert service_status_model == service_status_model2

        # Convert model instance back to dict and verify no loss of data
        service_status_model_json2 = service_status_model.to_dict()
        assert service_status_model_json2 == service_status_model_json

#-----------------------------------------------------------------------------
# Test Class for TextSpan
#-----------------------------------------------------------------------------
class TestTextSpan():

    #--------------------------------------------------------
    # Test serialization/deserialization for TextSpan
    #--------------------------------------------------------
    def test_text_span_serialization(self):

        # Construct a json representation of a TextSpan model
        text_span_model_json = {}
        text_span_model_json['section'] = 'testString'
        text_span_model_json['begin'] = 38
        text_span_model_json['end'] = 38
        text_span_model_json['coveredText'] = 'testString'
        text_span_model_json['source'] = 'testString'
        text_span_model_json['type'] = 'testString'

        # Construct a model instance of TextSpan by calling from_dict on the json representation
        text_span_model = TextSpan.from_dict(text_span_model_json)
        assert text_span_model != False

        # Construct a model instance of TextSpan by calling from_dict on the json representation
        text_span_model_dict = TextSpan.from_dict(text_span_model_json).__dict__
        text_span_model2 = TextSpan(**text_span_model_dict)

        # Verify the model instances are equivalent
        assert text_span_model == text_span_model2

        # Convert model instance back to dict and verify no loss of data
        text_span_model_json2 = text_span_model.to_dict()
        assert text_span_model_json2 == text_span_model_json

#-----------------------------------------------------------------------------
# Test Class for UnstructuredModel
#-----------------------------------------------------------------------------
class TestUnstructuredModel():

    #--------------------------------------------------------
    # Test serialization/deserialization for UnstructuredModel
    #--------------------------------------------------------
    def test_unstructured_model_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        text_span_model = {} # TextSpan
        text_span_model['section'] = 'testString'
        text_span_model['begin'] = 38
        text_span_model['end'] = 38
        text_span_model['coveredText'] = 'testString'
        text_span_model['source'] = 'testString'
        text_span_model['type'] = 'testString'

        concept_model_model = {} # ConceptModel
        concept_model_model['uniqueId'] = 38
        concept_model_model['stickyIds'] = [38]
        concept_model_model['section'] = 'testString'
        concept_model_model['type'] = 'testString'
        concept_model_model['begin'] = 38
        concept_model_model['end'] = 38
        concept_model_model['coveredText'] = 'testString'
        concept_model_model['cui'] = 'testString'
        concept_model_model['preferredName'] = 'testString'
        concept_model_model['source'] = 'testString'
        concept_model_model['negated'] = True
        concept_model_model['hypothetical'] = True
        concept_model_model['timestamp'] = 26
        concept_model_model['attributeId'] = 'testString'
        concept_model_model['qualifiers'] = ['testString']
        concept_model_model['unit'] = 'testString'
        concept_model_model['minValue'] = 'testString'
        concept_model_model['maxValue'] = 'testString'
        concept_model_model['operator'] = 'testString'
        concept_model_model['features'] = {}
        concept_model_model['nluEntityIndex'] = 'testString'
        concept_model_model['nluMentionIndex'] = 'testString'
        concept_model_model['nluRelationId'] = 'testString'
        concept_model_model['nluSide'] = 'testString'
        concept_model_model['nluSourceType'] = 'testString'
        concept_model_model['nluRelation'] = 'testString'
        concept_model_model['nluTargetType'] = 'testString'
        concept_model_model['hits'] = 38

        relation_model_model = {} # RelationModel
        relation_model_model['relationId'] = 'testString'
        relation_model_model['relation'] = 'testString'
        relation_model_model['source'] = text_span_model
        relation_model_model['target'] = text_span_model

        data_model_model = {} # DataModel
        data_model_model['concepts'] = [concept_model_model]
        data_model_model['attributeValues'] = [concept_model_model]
        data_model_model['relations'] = [relation_model_model]
        data_model_model['mesh'] = [concept_model_model]
        data_model_model['text'] = [concept_model_model]

        # Construct a json representation of a UnstructuredModel model
        unstructured_model_model_json = {}
        unstructured_model_model_json['text'] = 'testString'
        unstructured_model_model_json['data'] = data_model_model

        # Construct a model instance of UnstructuredModel by calling from_dict on the json representation
        unstructured_model_model = UnstructuredModel.from_dict(unstructured_model_model_json)
        assert unstructured_model_model != False

        # Construct a model instance of UnstructuredModel by calling from_dict on the json representation
        unstructured_model_model_dict = UnstructuredModel.from_dict(unstructured_model_model_json).__dict__
        unstructured_model_model2 = UnstructuredModel(**unstructured_model_model_dict)

        # Verify the model instances are equivalent
        assert unstructured_model_model == unstructured_model_model2

        # Convert model instance back to dict and verify no loss of data
        unstructured_model_model_json2 = unstructured_model_model.to_dict()
        assert unstructured_model_model_json2 == unstructured_model_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
