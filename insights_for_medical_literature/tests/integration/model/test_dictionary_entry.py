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
import watson_health_cognitive_services.insights_for_medical_literature as wh

def test_dictionary_entry():
    children = []
    parents = []
    siblings = []
    definition = []
    surface_forms = []
    variants = []
    related = []
    semtypes = []
    model = wh.DictionaryEntry(cui='test', preferred_name='test', source='test', source_version='test',
                               vocab='test', children=children, definition=definition, parents=parents,
                               siblings=siblings, related=related, semtypes=semtypes, surface_forms=surface_forms,
                               variants=variants)
    model_diff = wh.DictionaryEntry(cui='test', preferred_name='test', source='test', source_version='test',
                                    vocab='test', children=children, definition=None, parents=parents,
                                    siblings=siblings, related=related, semtypes=semtypes,
                                    surface_forms=surface_forms, variants=variants)
    model_same = wh.DictionaryEntry(cui='test', preferred_name='test', source='test', source_version='test',
                                    vocab='test', children=children, definition=definition, parents=parents,
                                    siblings=siblings, related=related, semtypes=semtypes,
                                    surface_forms=surface_forms, variants=variants)

    de_obj = {}
    de_obj['children'] = children
    de_obj['cui'] = 'test'
    de_obj['definition'] = definition
    de_obj['parents'] = parents
    de_obj['preferredName'] = 'test'
    de_obj['semtypes'] = semtypes
    de_obj['siblings'] = siblings
    de_obj['surfaceForms'] = surface_forms
    de_obj['variants'] = variants
    de_obj['vocab'] = 'test'
    de_obj['related'] = related
    de_obj['source'] = 'test'
    de_obj['source_version'] = 'test'
    de_dict = model._from_dict(de_obj)
    assert de_dict is not None

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
