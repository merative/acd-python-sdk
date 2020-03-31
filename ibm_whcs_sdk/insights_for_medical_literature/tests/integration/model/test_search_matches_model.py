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

def test_search_matches_model():
    authors = []
    highlighted_sections = {}
    passages = {}
    annotations = {}

    model = wh.SearchMatchesModel(
        external_id='test',
        document_id='test',
        parent_document_id='test',
        publication_name='test',
        publication_date='test',
        publication_url='test',
        authors=authors,
        title='test',
        medline_license='test',
        href_pub_med='test',
        pdf_url='test',
        reference_url='test',
        highlighted_title='test',
        highlighted_abstract='test',
        highlighted_body='test',
        highlighted_sections=highlighted_sections,
        passages=passages,
        annotations=annotations
    )

    model_diff = wh.SearchMatchesModel(
        external_id='test',
        document_id='test',
        parent_document_id='test',
        publication_name='test',
        publication_date='test',
        publication_url='exam',
        authors=authors,
        title='test',
        medline_license='test',
        href_pub_med='test',
        pdf_url='test',
        reference_url='test',
        highlighted_title='test',
        highlighted_abstract='test',
        highlighted_body='test',
        highlighted_sections=highlighted_sections,
        passages=passages,
        annotations=annotations
    )

    model_same = wh.SearchMatchesModel(
        external_id='test',
        document_id='test',
        parent_document_id='test',
        publication_name='test',
        publication_date='test',
        publication_url='test',
        authors=authors,
        title='test',
        medline_license='test',
        href_pub_med='test',
        pdf_url='test',
        reference_url='test',
        highlighted_title='test',
        highlighted_abstract='test',
        highlighted_body='test',
        highlighted_sections=highlighted_sections,
        passages=passages,
        annotations=annotations
    )

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
