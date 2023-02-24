# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestEjectionFractionAnnotation(object):

    @staticmethod
    def test_ejection_fraction(annotation_list=None):
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
                if annotation.first_value is not None:
                    assert len(annotation.first_value) > 0
                if annotation.second_value is not None:
                    assert len(annotation.second_value) > 0
                if annotation.is_range is not None:
                    assert len(annotation.is_range) > 0
                if annotation.ef_alphabetic_value_normalized_name is not None:
                    assert len(annotation.ef_alphabetic_value_normalized_name) > 0
                if annotation.ef_alphabetic_value_surface_form is not None:
                    assert len(annotation.ef_alphabetic_value_surface_form) > 0
                if annotation.ef_term_normalized_name is not None:
                    assert len(annotation.ef_term_normalized_name) > 0
                if annotation.ef_term_surface_form is not None:
                    assert len(annotation.ef_term_surface_form) > 0
                if annotation.ef_suffix_normalized_name is not None:
                    assert len(annotation.ef_suffix_normalized_name) > 0
                if annotation.ef_suffix_surface_form is not None:
                    assert len(annotation.ef_suffix_surface_form) > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
