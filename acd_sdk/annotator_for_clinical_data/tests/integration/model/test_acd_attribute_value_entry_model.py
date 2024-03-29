# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_AttributeValueEntry_model():
    model = acd.AttributeValueEntry(value="23", unit="pounds", frequency="once per day", duration="5",
                                   dimension="5x5", extra="more")
    assert model.__str__() is not None
