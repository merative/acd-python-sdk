# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_Flow_model():
    flowentry_data = acd.FlowEntry()
    model = acd.Flow(elements=[flowentry_data])
    assert model.__str__() is not None
