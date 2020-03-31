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

def test_document_text_model():
    metadata = []
    model = wh.DocumentTextModel(external_id='test', document_id='test', parent_document_id='test', title='test',
                                 abstract_text='test', body='test', pdf_url='test', reference_url='test',
                                 metadata=metadata)
    model_diff = wh.DocumentTextModel(external_id='test', document_id='test', parent_document_id='test',
                                      title='test', abstract_text='test', body=None, pdf_url='test',
                                      reference_url='test', metadata=metadata)
    model_same = wh.DocumentTextModel(external_id='test', document_id='test', parent_document_id='test',
                                      title='test', abstract_text='test', body='test', pdf_url='test',
                                      reference_url='test', metadata=metadata)

    text_model_obj = {}
    text_model_obj['externalId'] = 'test'
    text_model_obj['documentId'] = 'test'
    text_model_obj['parentDocumentId'] = 'test'
    text_model_obj['title'] = 'test'
    text_model_obj['abstractText'] = 'test'
    text_model_obj['body'] = 'test'
    text_model_obj['pdfUrl'] = 'test'
    text_model_obj['referenceUrl'] = 'test'
    text_model_obj['metadata'] = metadata
    document_text_model = model._from_dict(text_model_obj)

    assert model.__str__() is not None
    assert model.__eq__(document_text_model)
    assert model.__ne__(model_diff)
