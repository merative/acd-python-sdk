# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Smoking_model():
    model = wh.Smoking(id="name", type="type", uid=123, begin=1, end=2, covered_text="We got you covered",
                       negated=False, hypothetical=False, participation="yes", section_normalized_name="snn",
                       modality="y", current="today", smoke_term_surface_form="stsf",
                       smoke_term_normalized_name="stnn", section_surface_form="ssf", more="extra")
    assert model.__str__() is not None
