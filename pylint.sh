#!/bin/bash
# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 


python -m pylint ibm_whcs_sdk/annotator_for_clinical_data ibm_whcs_sdk/annotator_for_clinical_data/tests/unit ibm_whcs_sdk/annotator_for_clinical_data/tests/integration
python -m pylint ibm_whcs_sdk/insights_for_medical_literature ibm_whcs_sdk/insights_for_medical_literature/tests/unit ibm_whcs_sdk/insights_for_medical_literature/tests/integration
