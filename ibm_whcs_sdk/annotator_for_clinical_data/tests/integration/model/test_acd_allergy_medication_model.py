# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_AllergyMedication_model():
    medication_data = wh.MedicationAnnotation()
    model = wh.AllergyMedication(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered", negated=False,
                                 hypothetical=False, section_normalized_name="snn", section_surface_form="ssf",
                                 medication=[medication_data])
    assert model.__str__() is not None
