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
import unittest
import configparser
import watson_health_cognitive_services as wh

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
VERSION = CONFIG.get('settings', 'version')
CORPUS = CONFIG.get('settings', 'corpus')

IML_test = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, VERSION, True)

#########################
# IML
#########################

def check_for_null_or_error_resp(resp):
     if resp is None:
         return True
     else:
         if type(resp) == 'dict':
            if 'code' in resp:
                if resp['code'] > 299:
                   return True
     return False

class TestInsightsMedicalLiterature(unittest.TestCase):

   # TEST:  Get Corpus metadata
   #    - get the list of fields defined for the corpus
   #    - Assert if response is None or response status code > 299
   def test_getFields_g(self):
       resp = IML_test.get_fields(corpus)
       assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get Corpus metadata - invalid corpus
   #    - get the list of fields defined for the corpus
   #    - Assert exception raised with error code 400
   def test_getFields_e(self):
       error_code = 400
       try:
           resp = IML_test.get_fields('medline9')
       except wh.IMLException as ex:
           assert ex.code == error_code
           
   # TEST:  Get Corpus concepts
   #    - get the list of concepts defined for the corpus
   #    - Assert if response is None or response status code > 299
   def test_getConcepts_g(self):
       resp = IML_test.get_concepts(corpus,preferred_names='Sepsis', limit=20)
       assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get Corpus concepts - invalid concept
   #    - get the list of concepts defined for the corpus
   #    - Assert exception raised with error code 400
   def test_getConcepts_e(self):
       error_code = 400
       try:
           resp = IML_test.get_concepts(corpus,preferred_names='aaaaa', limit=20)
       except wh.IMLException as ex:
           assert ex.code == error_code

   # TEST:  Query typeahead 
   #    - Get the list of cuis of 'over eat' 
   #    - Assert if response is None or response status code > 299
   def test_typeahead_g(self):
        resp = IML_test.typeahead(corpus, 'Seps')
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Query typeahead - invalid concept
   #    - Get the list of cuis of 'over eat' 
   #    - Assert exception raised with error code 400
   def test_typeahead_e(self):
       error_code = 400
       try:
           resp = IML_test.typeahead(corpus, 'aaaa')
       except wh.IMLException as ex:
           assert ex.code == error_code

   # TEST:  Get Corpus concept
   #    - get a specific concept defined in the corpus
   #    - Assert if response is None or response status code > 299
   def test_getCuiInfo_g(self):
       resp = IML_test.get_cui_info(corpus, 'C0018787', 'umls', 'preferredName, definition, semanticTypes', 'true')
       assert check_for_null_or_error_resp(resp) == False
       
   # TEST:  Get Corpus concept - invalid concept
   #    - get a specific concept defined in the corpus
   #    - Assert exception raised with error code 400
   def test_getCuiInfo_e(self):
       error_code = 400
       try:
           resp = IML_test.get_cui_info(corpus, 'F0018787', 'umls', 'preferredName, definition, semanticTypes', 'true')
       except wh.IMLException as ex:
           assert ex.code == error_code

   # TEST:  Get related concepts for a specific concept
   #    - get the parents, children, or siblings of a specific concept defined in the corpus
   #    - Assert if response is None or response status code > 299
   def test_getRelatedConcepts_g(self):
       resp = IML_test.get_related_concepts(corpus, 'C0018787', 'par', 'umls', 'false', 'false')
       assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get related concepts for a specific concept - invalid concept
   #    - get the parents, children, or siblings of a specific concept defined in the corpus
   #    - Assert exception raised with error code 400
   def test_getRelatedConcepts_e(self):
       error_code = 400
       try:
           resp = IML_test.get_related_concepts('med9', 'C0018787', 'par', 'umls', 'false', 'false')
       except wh.IMLException as ex:
           assert ex.code == error_code
       
   # TEST:  Get corpus config
   #    - get the configuration for a specific corpus
   #    - Assert if response is None or response status code > 299
   def test_getCorpusConfig_g(self):
       resp = IML_test.get_corpus_config(corpus)
       assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get corpus config - invalid corpus
   #    - get the configuration for a specific corpus
   #    - Assert exception raised with error code 400
   def test_getCorpusConfig_e(self):
       error_code = 400
       try:
           resp = IML_test.get_corpus_config('med9')
       except wh.IMLException as ex:
           assert ex.code == error_code

   # TEST:  Get semantic types
   #    - get the semantic types found for a specific corpus
   #    - Assert if response is None or response status code > 299
   def test_getSemanticTypes_g(self):
       resp = IML_test.get_semantic_types(corpus)
       assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get semantic types
   #    - get the semantic types found for a specific corpus
   #    - Assert exception raised with error code 400
   def test_getSemanticTypes_e(self):
       error_code = 400
       try:
           resp = IML_test.get_semantic_types('med9')
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Documents
   # - get document count per provider
   # - Assert if response is None or response status code > 299
   def test_getDocuments_g(self):
        resp = IML_test.get_documents(corpus)
        assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Documents - invalide corpus
   # - get document count per provider
   # - Assert exception raised with error code 400
   def test_getDocuments_e(self):
       error_code = 400
       try:
           resp = IML_test.get_documents('med9')
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Document Info
   # - get details for a specific document
   # - Assert if response is None or response status code > 299
   def test_getDocumentInfo_g(self):
        resp = IML_test.get_document_info(corpus, '22437179')
        assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Document Info - invalide corpus
   # - get document count per provider
   # - Assert exception raised with error code 400
   def test_getDocumentInfo_e(self):
       error_code = 404
       try:
           resp = IML_test.get_document_info(corpus, 'N1')
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Document Annotations
   # - get details for a specific document
   # - Assert if response is None or response status code > 299
   def test_getDocumentAnnotations_g(self):
        resp = IML_test.get_document_annotations(corpus, '22437179', 'title')
        assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Documents - invalide section
   # - get document count per provider
   # - Assert exception raised with error code 404
   def test_getDocumentAnnotations_e(self):
       error_code = 404
       try:
           resp = IML_test.get_document_annotations(corpus, '22437179', 'body')
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Document Categories
   # - get details for a specific document
   # - Assert if response is None or response status code > 299
   def test_getDocumentCategories_g(self):
        resp = IML_test.get_document_categories(corpus, '22437179', '<u>', '</u>')
        assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Documents Categories - invalide docid
   # - get document count per provider
   # - Assert exception raised with error code 404
   def test_getDocumentCategories_e(self):
       error_code = 404
       try:
           resp = IML_test.get_document_categories(corpus, 'N1', '<u>', '</u>' )
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Document Search Matches
   # - get search matches for a specific document
   # - Assert if response is None or response status code > 299
   def test_getDocumentSearchMatches_g(self):
        resp = IML_test.get_search_matches(corpus, '22437179', '0.1', 'C0018787')
        assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Documents Search Matches - invalid docid
   # - get document count per provider
   # - Assert exception raised with error code 404
   def test_getDocumentSearchMatches_e(self):
       error_code = 404
       try:
           resp = IML_test.get_search_matches(corpus, 'N1', '0.1', 'C0018787')
       except wh.IMLException as ex:
           assert ex.code == error_code

   #TEST:  Get Document Search Results
   # - get search results from valid criteria
   # - Assert if response is None or response status code > 299
   def test_search_g(self):
       title = wh.Title(0)
       concept = {}
       concept['bool'] = "Heart"
       concept['id'] = "C0018787"
       concept['ontology'] = "umls"
       concept['type'] = "BodyPartOrganOrOrganComponent"

       concept_list = []
       concept_list.append(concept)

       query = wh.Query("Heart", concept_list)

       documents = wh.Documents("10", "0")
       returns = wh.ReturnsModel(documents)
       resp = IML_test.search(corpus, query, returns)
       assert check_for_null_or_error_resp(resp) == False

   #TEST:  Get Document Search Results - invalid corpus
   # - get search results from valid criteria
   # - Assert if response is None or response status code > 299
   def test_search_e(self):
       title = wh.Title(0)
       concept = {}
       concept['bool'] = "Heart"
       concept['id'] = "C0018787"
       concept['ontology'] = "umls"
       concept['type'] = "BodyPartOrganOrOrganComponent"

       concept_list = []
       concept_list.append(concept)

       query = wh.Query("Heart", concept_list)

       documents = wh.Documents("10", "0")
       returns = wh.ReturnsModel(documents)
       error_code = 400
       try:
           resp = IML_test.search('med9', query, returns)
       except wh.IMLException as ex:
           assert ex.code == error_code

if __name__ == '__main__':
    unittest.main()
