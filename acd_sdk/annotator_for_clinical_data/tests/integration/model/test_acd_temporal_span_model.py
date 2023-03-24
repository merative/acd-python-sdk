# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_TemporalSpan_model():
    temporal_type_dict = {}
    model = acd.Temporal(begin=1, end=2, covered_text="We got you covered",
                           temporal_type=temporal_type_dict, extra="more")
    assert model.__str__() is not None
