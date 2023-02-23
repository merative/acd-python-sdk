# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_TemporalSpan_model():
    temporal_type_dict = {}
    model = wh.Temporal(begin=1, end=2, covered_text="We got you covered",
                           temporal_type=temporal_type_dict, extra="more")
    assert model.__str__() is not None
