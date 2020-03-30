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
import watson_health_cognitive_services.insights_for_medical_literature as wh

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
CORPUS = CONFIG.get('settings', 'corpus')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_fields():
    metadata = IML_TEST.get_fields(CORPUS)
    field_map = metadata.fields
    for key in field_map:
        assert key is not None
        field_options = field_map[key]
        sup = wh.Supports()
        supports = sup._from_dict(field_options)
        supports_list = supports.supports
        for support in supports_list:
            assert support is not None
        assert field_options is not None

    section_names = metadata.section_field_names
    for names in section_names:
        assert names is not None

    mesh_section_names = metadata.mesh_section_field_names
    for mesh_names in mesh_section_names:
        if mesh_names is not None:
            assert mesh_names == 'mesh'

    attribute_section_names = metadata.attr_section_field_names
    for attr_names in attribute_section_names:
        assert attr_names is not None

    field_index_map = metadata.field_index_map
    for key in field_index_map:
        assert key is not None
        assert field_index_map[key] is not None

def test_get_fields_no_corpus():
    try:
        IML_TEST.get_fields(None)
    except ValueError as exp:
        assert exp is not None
