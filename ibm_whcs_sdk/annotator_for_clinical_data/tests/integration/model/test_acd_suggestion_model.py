# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Suggestion_model():
    semtypes_data = []
    model = wh.Suggestion(text="come back", confidence=1.0, applied=True, semtypes=semtypes_data, extra="more")
    assert model.__str__() is not None
