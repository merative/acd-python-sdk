# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_UnstructuredContainer_model():
    container_annotation = acd.ContainerAnnotation()
    metadata_dict = {}
    model = acd.UnstructuredContainer(text="text", id="id", type="type", data=container_annotation,
                                     metadata=metadata_dict, uid=1)
    assert model.__str__() is not None
