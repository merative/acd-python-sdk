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

def test_metadata_model():
    fields = {}
    section_field_names = []
    attr_section_field_names = []
    qualifier_section_field_names = []
    mesh_section_field_names = []

    model = wh.MetadataModel(fields=fields, section_field_names=section_field_names,
                             attr_section_field_names=attr_section_field_names,
                             qualifier_section_field_names=qualifier_section_field_names,
                             mesh_section_field_names=mesh_section_field_names)
    model_diff = wh.MetadataModel(fields=fields, section_field_names=section_field_names,
                                  attr_section_field_names=None,
                                  qualifier_section_field_names=qualifier_section_field_names,
                                  mesh_section_field_names=mesh_section_field_names)
    model_same = wh.MetadataModel(fields=fields, section_field_names=section_field_names,
                                  attr_section_field_names=attr_section_field_names,
                                  qualifier_section_field_names=qualifier_section_field_names,
                                  mesh_section_field_names=mesh_section_field_names)

    assert model.__str__() is not None
    assert model.__eq__(model_same)
    assert model.__ne__(model_diff)
