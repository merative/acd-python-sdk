# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_SpellingCorrection_model():
    suggestion_data = []
    model = wh.SpellingCorrection(begin=1, end=2, covered_text="covered", suggestions=suggestion_data)
    assert model.__str__() is not None
