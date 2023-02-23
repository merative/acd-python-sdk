# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_RequestContainer_model():
    unstructured_list = []
    annotator_flows_list = []
    model = wh.RequestContainer(unstructured=unstructured_list, annotator_flows=annotator_flows_list)
    assert model.__str__() is not None
