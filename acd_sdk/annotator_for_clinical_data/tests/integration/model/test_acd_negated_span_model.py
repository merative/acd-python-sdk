# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_NegatedSpan_model():
    trigger_data = []
    model = acd.NegatedSpan(id="name", type="type", uid=123, begin=1, end=2, covered_text="We got you covered",
                           negated=False, hypothetical=False, trigger=trigger_data, extra="more")
    assert model.__str__() is not None
