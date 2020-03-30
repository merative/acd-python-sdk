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


def test_attribute_entry():
    field_values = []
    field_values.append('test')
    possible_values = []

    entry = wh.AttributeEntry(
        attr_name='test',
        data_type='test',
        default_value='test',
        display_name='test',
        description='test',
        doc_id='test',
        field_values=field_values,
        maximum_value='test',
        minimum_value='test',
        multi_value=False,
        units='test',
        value_type='test',
        possible_values=possible_values
    )

    entry_diff = wh.AttributeEntry(
        attr_name='test',
        data_type='test',
        default_value='test',
        display_name='test',
        description='test',
        doc_id='test',
        field_values=field_values,
        maximum_value='test',
        minimum_value='test',
        multi_value=True,
        units='test',
        value_type='test',
        possible_values=possible_values
    )

    entry_same = wh.AttributeEntry(
        attr_name='test',
        data_type='test',
        default_value='test',
        display_name='test',
        description='test',
        doc_id='test',
        field_values=field_values,
        maximum_value='test',
        minimum_value='test',
        multi_value=False,
        units='test',
        value_type='test',
        possible_values=possible_values
    )

    attr_entry = {}
    attr_entry['attr_name'] = 'test'
    attr_entry['data_type'] = 'test'
    attr_entry['default_value'] = 'test'
    attr_entry['display_name'] = 'test'
    attr_entry['description'] = 'test'
    attr_entry['doc_id'] = 'test'
    attr_entry['field_values'] = field_values
    attr_entry['maximum_value'] = 'test'
    attr_entry['minimum_value'] = 'test'
    attr_entry['multi_value'] = False
    attr_entry['units'] = 'test'
    attr_entry['valueType'] = 'test'
    attr_entry['possible_values'] = possible_values
    attr_entry_dict = entry._from_dict(attr_entry)
    assert attr_entry_dict is not None

    assert entry.__str__() is not None
    assert entry.__eq__(entry_same)
    assert entry.__ne__(entry_diff)
