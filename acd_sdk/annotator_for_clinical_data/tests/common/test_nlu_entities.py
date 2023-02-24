# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestNluEntitiesAnnotation(object):

    @staticmethod
    def test_nlu_entities(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.type is not None
                assert annotation.source is not None
                assert annotation.begin > 0
                assert annotation.end > annotation.begin
                assert annotation.relevance > 0
                if annotation.uid is not None:
                    assert annotation.uid > 0
