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

import watson_health_cognitive_services.annotator_for_clinical_data as wh

def test_AttributeValueAnnotation_model():
    value_list = []
    disambiguation = wh.Disambiguation()
    model = wh.AttributeValueAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                        negated=False, hypothetical=False, preferred_name="preferred",
                                        values=value_list, source="source", source_version="sv", name="name",
                                        icd9_code="icd9", icd10_code="icd10", nci_code="nci", snomed_concept_id="sci",
                                        mesh_id="meshID", rx_norm_id="rni", loinc_id="li", vocabs="vocab",
                                        section_normalized_name="snn", section_surface_form="ssf", cpt_code="cpt",
                                        disambiguation_data=disambiguation, extra="more")
    assert model.__str__() is not None
