# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_AcdProfile_model():
    annotators_list = []
    model = wh.AcdProfile(id="id", name="name", description="very good", annotators=annotators_list)
    assert model.__str__() is not None
