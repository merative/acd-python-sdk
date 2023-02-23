# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_AcdFlow_model():
    annotator_flows_list = wh.AnnotatorFlow(wh.Flow())
    model = wh.AcdFlow(id="id", name="name", description="describe", annotator_flows=[annotator_flows_list])
    assert model.__str__() is not None
