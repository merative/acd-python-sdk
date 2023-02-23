# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Annotator_model():
    annotator_data = wh.Annotator(name='concept_value')
    flow_data = wh.Flow()
    parameter_data = []
    configurations_data = []
    model = wh.Annotator(name='concept_value', parameters=parameter_data, configurations=configurations_data)
    assert model.__str__() is not None
