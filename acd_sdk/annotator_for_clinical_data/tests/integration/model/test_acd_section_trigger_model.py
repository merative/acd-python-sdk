# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_SectionTrigger_model():
    model = acd.SectionTrigger(begin=1, end=2, covered_text="We got you covered",
                              section_normalized_name="snn", source="source", type="type", extra="more")
    assert model.__str__() is not None
