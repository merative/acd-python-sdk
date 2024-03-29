# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_CancerDiagnosis_model():
    disambiguation = acd.Disambiguation(validity="yes")
    model = acd.CancerDiagnosis(id="mine", type="yours", uid=1234, begin=23, end=1964,
                               covered_text="We got you covered", negated=False, hypothetical=False, cui=123,
                               section_normalized_name="normal", modality="high", section_surface_form="skin",
                               cancer="bad", disambiguation_data=disambiguation, extra_data="not much")
    assert model.__str__() is not None
