# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_UnstructuredContainer_model():
    container_annotation = wh.ContainerAnnotation()
    metadata_dict = {}
    model = wh.UnstructuredContainer(text="text", id="id", type="type", data=container_annotation,
                                     metadata=metadata_dict, uid=1)
    assert model.__str__() is not None
