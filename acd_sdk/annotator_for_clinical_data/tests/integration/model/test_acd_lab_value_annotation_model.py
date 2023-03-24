# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_LabValueAnnotation_model():
    model = acd.LabValueAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                  negated=False, hypothetical=False, loinc_id="loinc", low_value="1",
                                  date_in_milliseconds="20", lab_type_surface_form="ltsf",
                                  lab_type_normalized_name="ltnn", lab_value="labValue",
                                  section_normalized_name="snn", section_surface_form="ssf", extra="more")
    assert model.__str__() is not None
