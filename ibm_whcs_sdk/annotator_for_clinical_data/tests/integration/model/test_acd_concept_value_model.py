# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_ConceptValue_model():
    model = wh.ConceptValue(id="name", type="type", uid=123, begin=1, end=2, covered_text="We got you covered",
                            negated=False, hypothetical=False, cui=234, dimension="large", preferred_name="other name",
                            trigger="pull", source="truth", value="important", section_normalized_name="snn",
                            section_surface_form="ssf", extra="more")
    assert model.__str__() is not None
