# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from acd_sdk.annotator_for_clinical_data.tests.common import test_insight_model as ti

class TestMedicationAnnotation(object):

    @staticmethod
    def test_medication_annotation(annotation_list=None):
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
                if annotation.cui is not None:
                    assert len(annotation.cui) > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
                if annotation.drug is not None:
                    for drug_obj in annotation.drug:
                        assert drug_obj is not None
                if annotation.insight_model_data is not None:
                    ti.TestInsightModel.test_insight_model_data(annotation.insight_model_data)
                if annotation.temporal is not None:
                    for entry in annotation.temporal:
                        assert entry is not None
                if annotation.disambiguation_data is not None:
                    assert annotation.disambiguation_data.validity is not None
