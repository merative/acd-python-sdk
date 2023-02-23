# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from ibm_whcs_sdk.annotator_for_clinical_data.tests.common import test_insight_model as ti

class TestSymptomDiseaseAnnotation(object):

    @staticmethod
    def test_symptom_disease(annotation_list=None):
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
                if annotation.date_in_milliseconds is not None:
                    assert len(annotation.date_in_milliseconds) > 0
                if annotation.icd10_code is not None:
                    assert len(annotation.icd10_code) > 0
                if annotation.icd9_code is not None:
                    assert len(annotation.icd9_code) > 0
                if annotation.snomed_concept_id is not None:
                    assert len(annotation.snomed_concept_id) > 0
                if annotation.ccs_code is not None:
                    assert len(annotation.ccs_code) > 0
                if annotation.hcc_code is not None:
                    assert len(annotation.hcc_code) > 0
                if annotation.modality is not None:
                    assert len(annotation.modality) > 0
                if annotation.symptom_disease_surface_form is not None:
                    assert len(annotation.symptom_disease_surface_form) > 0
                if annotation.symptom_disease_normalized_name is not None:
                    assert len(annotation.symptom_disease_normalized_name) > 0
                if annotation.section_normalized_name is not None:
                    assert len(annotation.section_normalized_name) > 0
                if annotation.section_surface_form is not None:
                    assert len(annotation.section_surface_form) > 0
                if annotation.insight_model_data is not None:
                    ti.TestInsightModel.test_insight_model_data(annotation.insight_model_data)
                if annotation.temporal is not None:
                    for entry in annotation.temporal:
                        assert entry is not None
