# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_SymptomDisease_model():
    disambiguation = wh.Disambiguation(validity="yes")
    temporal_list = []
    model = wh.SymptomDisease(id="name", type="type", uid=124, begin=1, end=2, covered_text="We got you covered",
                              negated=False, hypothetical=False, cui=123, icd10_code="10",
                              section_normalized_name="snn", modality="active", symptom_disease_surface_form="sdsf",
                              date_in_milliseconds="20", snomed_concept_id="sn_concept_id", ccs_code="ccscode",
                              symptom_disease_normalized_name="sdnn", section_surface_form="ssf", icd9_code="icd9",
                              hcc_code="hcc", disambiguation_data=disambiguation, temporal=temporal_list, extra="more")

    assert model.__str__() is not None
