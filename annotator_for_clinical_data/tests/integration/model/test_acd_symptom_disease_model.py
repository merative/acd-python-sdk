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

def test_SymptomDisease_model():
    disambiguation = wh.Disambiguation(validity="yes")

    model = wh.SymptomDisease(id="name", type="type", uid=124, begin=1, end=2, covered_text="We got you covered",
                              negated=False, hypothetical=False, cui=123, icd10_code="10",
                              section_normalized_name="snn", modality="active", symptom_disease_surface_form="sdsf",
                              date_in_milliseconds="20", snomed_concept_id="sn_concept_id", ccs_code="ccscode",
                              symptom_disease_normalized_name="sdnn", section_surface_form="ssf", icd9_code="icd9",
                              hcc_code="hcc", disambiguation_data=disambiguation, extra="more")

    assert model.__str__() is not None
