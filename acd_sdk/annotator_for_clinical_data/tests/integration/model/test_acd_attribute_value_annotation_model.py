# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2021, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import acd_sdk.annotator_for_clinical_data as acd

def test_AttributeValueAnnotation_model():
    value_list = []
    disambiguation = acd.Disambiguation()
    insight_data = acd.InsightModelData()
    derived_from_list = []
    temporal_list = []
    evidence_spans_list = []
    model = acd.AttributeValueAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                        negated=False, hypothetical=False, preferred_name="preferred",
                                        values=value_list, source="source", source_version="sv", name="name",
                                        icd9_code="icd9", icd10_code="icd10", nci_code="nci", snomed_concept_id="sci",
                                        mesh_id="meshID", rx_norm_id="rni", loinc_id="li", vocabs="vocab",
                                        section_normalized_name="snn", section_surface_form="ssf", cpt_code="cpt",
                                        disambiguation_data=disambiguation, insight_model_data=insight_data, 
                                        ccs_code="ccs", hcc_code="hcc", rule_id="rule", derived_from=derived_from_list, 
                                        temporal=temporal_list, evidence_spans=evidence_spans_list, extra="more")
    assert model.__str__() is not None
