# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from acd_sdk.annotator_for_clinical_data.tests.common import test_insight_model as ti

class TestConceptAnnotation(object):

    @staticmethod
    def test_concept_annotation(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                if annotation.id is not None:
                    assert len(annotation.id) > 0
                if annotation.type is not None:
                    assert len(annotation.type) > 0
                assert annotation.begin >= 0
                assert annotation.end > annotation.begin
                assert annotation.covered_text is not None
                if annotation.semantic_type is not None:
                    assert len(annotation.semantic_type) > 0
                if annotation.uid is not None:
                    assert annotation.uid > 0
                if annotation.cui is not None:
                    assert len(annotation.cui) > 0
                if annotation.preferred_name is not None:
                    assert len(annotation.preferred_name) > 0
                if annotation.source is not None:
                    assert len(annotation.source) > 0
                if annotation.source_version is not None:
                    assert len(annotation.source_version) > 0
                if annotation.icd9_code is not None:
                    assert len(annotation.icd9_code) > 0
                if annotation.icd10_code is not None:
                    assert len(annotation.icd10_code) > 0
                if annotation.nci_code is not None:
                    assert len(annotation.nci_code) > 0
                if annotation.snomed_concept_id is not None:
                    assert len(annotation.snomed_concept_id) > 0
                if annotation.mesh_id is not None:
                    assert len(annotation.mesh_id) > 0
                if annotation.rx_norm_id is not None:
                    assert len(annotation.rx_norm_id) > 0
                if annotation.loinc_id is not None:
                    assert len(annotation.loinc_id) > 0
                if annotation.vocabs is not None:
                    assert len(annotation.vocabs) > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
                if annotation.cpt_code is not None:
                    assert len(annotation.cpt_code) > 0
                if annotation.disambiguation_data is not None:
                    assert annotation.disambiguation_data.validity is not None
                if annotation.insight_model_data is not None:
                    ti.TestInsightModel.test_insight_model_data(annotation.insight_model_data)
                if annotation.rule_id is not None:
                    assert len(annotation.rule_id) > 0
                if annotation.derived_from is not None:
                    for entry in annotation.derived_from:
                        assert entry is not None
                        if entry.uid is not None:
                            assert entry.uid >= 0
                        if entry.selection_label is not None:
                            assert len(entry.selection_label) > 0
                if annotation.temporal is not None:
                    for entry in annotation.temporal:
                        assert entry is not None
