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

def test_Procedure_model():
    disambiguation = wh.Disambiguation()
    model = wh.Procedure(id="name", type="type", uid=123, begin=1, end=2, covered_text="We got you covered",
                         negated=False, hypothetical=False, cui=234, section_normalized_name="snn",
                         date_in_milliseconds="20", snomed_concept_id="sci", procedure_surface_form="psf",
                         procedure_normalized_name="pnn", section_surface_form="ssf",
                         disambiguation_data=disambiguation, extra="more")
    assert model.__str__() is not None
