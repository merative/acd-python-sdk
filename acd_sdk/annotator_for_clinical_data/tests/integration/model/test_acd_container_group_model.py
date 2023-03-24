# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_ContainerGroup_model():
    unstructured_list = []
    annotator_flows_list = []
    model = acd.ContainerGroup(unstructured=unstructured_list, annotator_flows=annotator_flows_list)
    assert model.__str__() is not None
