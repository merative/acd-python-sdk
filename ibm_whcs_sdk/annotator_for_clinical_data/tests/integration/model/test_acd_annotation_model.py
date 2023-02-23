# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Annotation_model():
    model = wh.Annotation(id="id", type="type", uid=1, begin=1, end=2, covered_text="covered", negated=False,
                          hypothetical=False, section_normalized_name="snn", section_surface_form="ssf", extra="more")
    assert model.__str__() is not None
