# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestSectionAnnotation(object):

    @staticmethod
    def test_section_annotation(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.type is not None
                if annotation.section_type is not None:
                    assert len(annotation.section_type) > 0
                assert annotation.begin > 0
                assert annotation.end > annotation.begin
                if annotation.covered_text is not None:
                    assert len(annotation.covered_text) > 0
                if annotation.trigger is not None:
                    section_trigger = annotation.trigger
                    assert section_trigger.begin > 0
                    assert section_trigger.end > section_trigger.begin
                    assert section_trigger.covered_text is not None
                    assert section_trigger.source is not None
                    assert section_trigger.section_normalized_name is not None
                    assert section_trigger.type is not None
