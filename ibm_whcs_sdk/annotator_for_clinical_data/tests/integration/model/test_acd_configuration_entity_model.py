# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_ConfigurationEntity_model():
    model = wh.ConfigurationEntity(id="id", type="type", uid=1)
    assert model.__str__() is not None
