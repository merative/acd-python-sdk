#!/bin/bash
# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 


python -m pylint acd_sdk/annotator_for_clinical_data acd_sdk/annotator_for_clinical_data/tests/unit acd_sdk/annotator_for_clinical_data/tests/integration
