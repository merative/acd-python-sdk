# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_AssistanceAnnotation_model():
    model = wh.AssistanceAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                    negated=False, hypothetical=False, primary_action_normalized_name="pann",
                                    modality="modality", primary_action_surface_form="primary_action_surface_form",
                                    section_normalized_name="snn", section_surface_form="ssf", extra="more")
    assert model.__str__() is not None
