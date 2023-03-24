# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestConceptValueAnnotation(object):

    @staticmethod
    def test_concept_value(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                if annotation.id is not None:
                    assert len(annotation.id) > 0
                if annotation.type is not None:
                    assert len(annotation.type) > 0
                assert annotation.begin is not None
                assert annotation.end is not None
                assert annotation.covered_text is not None
                if annotation.uid is not None:
                 assert annotation.uid > 0
                if annotation.preferred_name is not None:
                    assert len(annotation.preferred_name) > 0
                if annotation.source is not None:
                    assert len(annotation.source) > 0
                if annotation.cui is not None:
                    assert len(annotation.cui) > 0
                if annotation.dimension is not None:
                    assert len(annotation.dimension) > 0
                if annotation.trigger is not None:
                    assert len(annotation.trigger) > 0
                if annotation.value is not None:
                    assert len(annotation.value) > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
