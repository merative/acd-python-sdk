# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2021, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from acd_sdk.annotator_for_clinical_data.tests.common import test_annotation as ta
from acd_sdk.annotator_for_clinical_data.tests.common import test_attribute_values as tav
from acd_sdk.annotator_for_clinical_data.tests.common import test_assistance_annotation as taa
from acd_sdk.annotator_for_clinical_data.tests.common import test_cancer_diagnosis as tcd
from acd_sdk.annotator_for_clinical_data.tests.common import test_concept_annotation as tca
from acd_sdk.annotator_for_clinical_data.tests.common import test_concept_value_annotation as tcva
from acd_sdk.annotator_for_clinical_data.tests.common import test_ejection_fraction as tef
from acd_sdk.annotator_for_clinical_data.tests.common import test_lab_value as tlv
from acd_sdk.annotator_for_clinical_data.tests.common import test_medication as tm
from acd_sdk.annotator_for_clinical_data.tests.common import test_negated_span as tns
from acd_sdk.annotator_for_clinical_data.tests.common import test_procedure as tp
from acd_sdk.annotator_for_clinical_data.tests.common import test_smoking as ts
from acd_sdk.annotator_for_clinical_data.tests.common import test_symptom_disease as tsd
from acd_sdk.annotator_for_clinical_data.tests.common import test_section as tsec
from acd_sdk.annotator_for_clinical_data.tests.common import test_nlu_entities as tne
from acd_sdk.annotator_for_clinical_data.tests.common import test_relation as tr
from acd_sdk.annotator_for_clinical_data.tests.common import test_spelling_correction as tsc
from acd_sdk.annotator_for_clinical_data.tests.common import test_spell_corrected_text as tsct
from acd_sdk.annotator_for_clinical_data.tests.common import test_temporal_span as tts

class TestUnstructuredContainer(object):

    @staticmethod
    def test_unstructured_container(data=None):
        if data is not None:
            if data.allergy_ind is not None:
                ta.TestAnnotation.test_annotation(data.allergy_ind)
            if data.allergy_medication_ind is not None:
                ta.TestAnnotation.test_annotation(data.allergy_medication_ind)
            if data.attribute_values is not None:
                tav.TestAttributeValueAnnotation.test_attribute_values(data.attribute_values)
            if data.bathing_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.bathing_assistance_ind)
            if data.ica_cancer_diagnosis_ind is not None:
                tcd.TestCancerDiagnosisAnnotation.test_cancer_diagnosis(data.ica_cancer_diagnosis_ind)
            if data.concepts is not None:
                tca.TestConceptAnnotation.test_concept_annotation(data.concepts)
            if data.concept_values is not None:
                tcva.TestConceptValueAnnotation.test_concept_value(data.concept_values)
            if data.dressing_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.dressing_assistance_ind)
            if data.eating_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.eating_assistance_ind)
            if data.ejection_fraction_ind is not None:
                tef.TestEjectionFractionAnnotation.test_ejection_fraction(data.ejection_fraction_ind)
            if data.hypothetical_spans is not None:
                ta.TestAnnotation.test_annotation(data.hypothetical_spans)
            if data.email_address_ind is not None:
                ta.TestAnnotation.test_annotation(data.email_address_ind)
            if data.lab_value_ind is not None:
                tlv.TestLabValueAnnotation.test_lab_value_annotation(data.lab_value_ind)
            if data.medication_ind is not None:
                tm.TestMedicationAnnotation.test_medication_annotation(data.medication_ind)
            if data.location_ind is not None:
                ta.TestAnnotation.test_annotation(data.location_ind)
            if data.person_ind is not None:
                ta.TestAnnotation.test_annotation(data.person_ind)
            if data.u_s_phone_number_ind is not None:
                ta.TestAnnotation.test_annotation(data.u_s_phone_number_ind)
            if data.medical_institution_ind is not None:
                ta.TestAnnotation.test_annotation(data.medical_institution_ind)
            if data.organization_ind is not None:
                ta.TestAnnotation.test_annotation(data.organization_ind)
            if data.negated_spans is not None:
                tns.TestNegatedSpanAnnotation.test_negated_span(data.negated_spans)
            if data.procedure_ind is not None:
                tp.TestProcedureAnnotation.test_procedure_annotation(data.procedure_ind)
            if data.seeing_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.seeing_assistance_ind)
            if data.smoking_ind is not None:
                ts.TestSmokingAnnotation.test_smoking_annotation(data.smoking_ind)
            if data.symptom_disease_ind is not None:
                tsd.TestSymptomDiseaseAnnotation.test_symptom_disease(data.symptom_disease_ind)
            if data.toileting_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.toileting_assistance_ind)
            if data.walking_assistance_ind is not None:
                taa.TestAssistanceAnnotation.test_assistance_annotation(data.walking_assistance_ind)
            if data.sections is not None:
                tsec.TestSectionAnnotation.test_section_annotation(data.sections)
            if data.nlu_entities is not None:
                tne.TestNluEntitiesAnnotation.test_nlu_entities(data.nlu_entities)
            if data.relations is not None:
                tr.TestRelationAnnotation.test_relation_annotation(data.relations)
            if data.spelling_corrections is not None:
                tsc.TestSpellingCorrection.test_spelling_correction(data.spelling_corrections)
            if data.spell_corrected_text is not None:
                tsct.TestSpellCorrectedText.test_spell_corrected_text(data.spell_corrected_text)
            if data.temporal_spans is not None:
                tts.TestTemporalSpanAnnotation.test_temporal_span(data.temporal_spans)
            if data.lines is not None:
                ta.TestAnnotation.test_annotation(data.lines)
            if data.sentences is not None:
                ta.TestAnnotation.test_annotation(data.sentences)
            if data.paragraphs is not None:
                ta.TestAnnotation.test_annotation(data.paragraphs)
