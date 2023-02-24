# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_AnnotatorFlow_model():
    flow_data = acd.Flow()
    model = acd.AnnotatorFlow(profile="mine", flow=flow_data)
    assert model.__str__() is not None
