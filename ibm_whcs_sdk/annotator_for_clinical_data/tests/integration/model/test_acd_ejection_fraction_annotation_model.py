# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_EjectionFractionAnnotation_model():
    model = wh.EjectionFractionAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                          negated=False, hypothetical=False, first_value="1",
                                          ef_alphabetic_value_surface_form="eavsf", second_value="2",
                                          ef_term_surface_form="etsf", ef_suffix_surface_form="essf",
                                          ef_suffix_normalized_name="esnn",
                                          ef_alphabetic_value_normalized_name="eavnn", ef_term_normalized_name="etnn",
                                          is_range="yes", section_normalized_name="snn", section_surface_form="ssf")
    assert model.__str__() is not None
