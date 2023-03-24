# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2021, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestAnnotation(object):

    @staticmethod
    def test_annotation(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                if annotation.id is not None:
                    assert len(annotation.id) > 0
                if annotation.type is not None:
                    assert len(annotation.type) > 0
                assert annotation.begin is not None
                assert annotation.end is not None
                if annotation.covered_text is not None:
                    assert len(annotation.covered_text) > 0
                if annotation.uid is not None:
                    assert annotation.uid > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
