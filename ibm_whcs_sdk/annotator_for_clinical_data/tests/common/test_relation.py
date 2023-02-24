# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestRelationAnnotation(object):

    @staticmethod
    def test_relation_annotation(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.source is not None
                assert annotation.score > 0
                assert annotation.type is not None
                nodes = annotation.nodes
                for node in nodes:
                    assert node.entity.uid > 0
