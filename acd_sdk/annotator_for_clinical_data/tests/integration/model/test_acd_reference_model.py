# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2021, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_Reference_model():
    model = acd.Reference(uid=1, selection_label="sl", value_index=1, extra="more")
    assert model.__str__() is not None
