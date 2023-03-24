# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_AcdFlow_model():
    annotator_flows_list = acd.AnnotatorFlow(acd.Flow())
    model = acd.AcdFlow(id="id", name="name", description="describe", annotator_flows=[annotator_flows_list])
    assert model.__str__() is not None
