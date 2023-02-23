# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_SpellCorrectedText_model():
    model = wh.SpellCorrectedText(corrected_text="wrong", debug_text="good luck")
    assert model.__str__() is not None
