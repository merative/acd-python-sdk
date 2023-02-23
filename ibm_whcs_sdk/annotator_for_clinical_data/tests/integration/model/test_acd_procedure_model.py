# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_Procedure_model():
    disambiguation = wh.Disambiguation()
    temporal_list = []
    model = wh.Procedure(id="name", type="type", uid=123, begin=1, end=2, covered_text="We got you covered",
                         negated=False, hypothetical=False, cui=234, section_normalized_name="snn",
                         date_in_milliseconds="20", snomed_concept_id="sci", procedure_surface_form="psf",
                         procedure_normalized_name="pnn", section_surface_form="ssf",
                         disambiguation_data=disambiguation, temporal=temporal_list, extra="more")
    assert model.__str__() is not None
