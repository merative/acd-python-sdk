# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_Section_model():
    sectiontrigger_data = acd.SectionTrigger()
    model = acd.Section(begin=1, covered_text="cover", end=2, type="type", section_type="big",
                       trigger=sectiontrigger_data)
    assert model.__str__() is not None
