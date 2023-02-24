# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_Annotator_model():
    annotator_data = acd.Annotator(name='concept_value')
    flow_data = acd.Flow()
    parameter_data = []
    configurations_data = []
    model = acd.Annotator(name='concept_value', parameters=parameter_data, configurations=configurations_data)
    assert model.__str__() is not None
