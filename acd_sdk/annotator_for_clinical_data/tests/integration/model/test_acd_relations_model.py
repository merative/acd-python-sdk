# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_Relations_model():
    node_list = []
    model = acd.Relations(source="source", score=1.0, nodes=node_list, type="type")
    assert model.__str__() is not None
