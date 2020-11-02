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

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_ContainerAnnotation_model():
    allergy_ind = []
    allergy_medication_ind = []
    attribute_values = []
    bathing_assistance_ind = []
    ica_cancer_diagnosis_ind = []
    concepts = []
    concept_values = []
    dressing_assistance_ind = []
    eating_assistance_ind = []
    ejection_fraction_ind = []
    hypothetical_spans = []
    lab_value_ind = []
    medication_ind = []
    email_address_ind = []
    location_ind = []
    person_ind = []
    u_s_phone_number_ind = []
    medical_institution_ind = []
    organization_ind = []
    negated_spans = []
    procedure_ind = []
    seeing_assistance_ind = []
    smoking_ind = []
    symptom_disease_ind = []
    toileting_assistance_ind = []
    walking_assistance_ind = []
    sections = []
    nlu_entities = []
    relations = []
    spelling_corrections = []
    spell_corrected_text = []
    temporal_spans = []
    model = wh.ContainerAnnotation(allergy_ind=allergy_ind, allergy_medication_ind=allergy_medication_ind,
                                   attribute_values=attribute_values, bathing_assistance_ind=bathing_assistance_ind,
                                   ica_cancer_diagnosis_ind=ica_cancer_diagnosis_ind, concepts=concepts,
                                   concept_values=concept_values, dressing_assistance_ind=dressing_assistance_ind,
                                   eating_assistance_ind=eating_assistance_ind,
                                   ejection_fraction_ind=ejection_fraction_ind, hypothetical_spans=hypothetical_spans,
                                   lab_value_ind=lab_value_ind, medication_ind=medication_ind,
                                   email_address_ind=email_address_ind, location_ind=location_ind,
                                   person_ind=person_ind, u_s_phone_number_ind=u_s_phone_number_ind,
                                   medical_institution_ind=medical_institution_ind, organization_ind=organization_ind,
                                   negated_spans=negated_spans, procedure_ind=procedure_ind,
                                   seeing_assistance_ind=seeing_assistance_ind, smoking_ind=smoking_ind,
                                   symptom_disease_ind=symptom_disease_ind,
                                   toileting_assistance_ind=toileting_assistance_ind,
                                   walking_assistance_ind=walking_assistance_ind, sections=sections,
                                   nlu_entities=nlu_entities, relations=relations,
                                   spelling_corrections=spelling_corrections, spell_corrected_text=spell_corrected_text,
                                   temporal_spans=temporal_spans)
    assert model.__str__() is not None
