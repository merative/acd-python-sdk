# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Section_model():
    sectiontrigger_data = wh.SectionTrigger()
    model = wh.Section(begin=1, covered_text="cover", end=2, type="type", section_type="big",
                       trigger=sectiontrigger_data)
    assert model.__str__() is not None
