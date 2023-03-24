# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import configparser
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator
import acd_sdk.annotator_for_clinical_data as acd
from acd_sdk.annotator_for_clinical_data.tests.common import test_unstructured_container as tuc

CONFIG = configparser.RawConfigParser()
CONFIG.read('./acd_sdk/annotator_for_clinical_data/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
BEARER_TOKEN = CONFIG.get('settings', 'bearer_token')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = (CONFIG.get('settings', 'disable_ssl')=='True')
FLOW = CONFIG.get('settings', 'flow')

ACD_SERVICE = acd.AnnotatorForClinicalDataV1(
     authenticator=BearerTokenAuthenticator(bearer_token=BEARER_TOKEN),
     version=VERSION
     )
ACD_SERVICE.set_service_url(BASE_URL)
ACD_SERVICE.set_disable_ssl_verification(DISABLE_SSL)

LINE1 = 'The patient has cancer and is currently taking 400 ml sisplatin chemotherapy.\n'
LINE2 = 'HISTORY:  Patient is allergic to latex.  Patient cannot walk and needs help bathing and getting around.  '
LINE3 = 'The lab values were: white blood cell count 4.6, hemoglobin 12.2.  '
LINE4 = 'Echocardiogram demonstrated ejection fraction of approx 60%.  '
LINE5 = 'Patient cannot dress or feed without help as the patient can not see.  Patient may die soon but has not '
LINE6 = 'died yet.  Patient smoked for 20 years.  Patient can not clean up after defacating in toilet.  '
LINE7 = 'Jone Doe was seen at Baylor Hospitall in Austin, TX.  Johndoe@testaddress.com - (555) 555-5555 '
LINE8 = 'The patient started on metformin because his blood sugar was too high.'
LINE9 = 'CT scan showed a tumor in his lung.'
LINE10 = 'She had gallbladder removal September 19 2020'
LINE11 = 'Her father had lung cancer. Her mother had asthma and diabetes.'
LINE12 = 'Past addictions history: by report, pt with history of ETOH abuse; BAL 147.\n'
LINE13 = 'Allergic to penicillin.  Patient had a colonoscopy in 2009.'
LINE14 = 'Patient abuses vodka and smokes cigarettes and marijuana. Patiet attends monthly AA meetings.'
TEXT = LINE1 + LINE2 + LINE3 + LINE4 + LINE5 + LINE6 + LINE7 + LINE8 + LINE9 + LINE10 + LINE11 + LINE12 + LINE13 + LINE14

def test_analyze_flow():
    data = ACD_SERVICE.analyze_with_flow(FLOW, TEXT)
    tuc.TestUnstructuredContainer.test_unstructured_container(data=data)

def test_analyze_flow_container():
    container = acd.UnstructuredContainer(TEXT)
    data = ACD_SERVICE.analyze_with_flow(FLOW, container)
    tuc.TestUnstructuredContainer.test_unstructured_container(data=data)

def test_analyze_flow_request_list():
    container = [acd.UnstructuredContainer(TEXT)]
    container_group = ACD_SERVICE.analyze_with_flow(FLOW, container)

    for unstructured_container in container_group.unstructured:
        if unstructured_container.text is not None:
            assert unstructured_container.text == TEXT
        if unstructured_container.id is not None:
            assert unstructured_container.id != '0'
        if unstructured_container.type is not None:
            assert unstructured_container.type != 'bogus'
        
        assert unstructured_container.data is not None
        tuc.TestUnstructuredContainer.test_unstructured_container(data=unstructured_container.data)

def test_analyze_flow_org():
    response = ACD_SERVICE.analyze_with_flow_org(FLOW, TEXT)
    container_group = acd.ContainerGroup._from_dict(response.get_result())

    for unstructured_container in container_group.unstructured:
        if unstructured_container.text is not None:
            assert unstructured_container.text == TEXT
        if unstructured_container.id is not None:
            assert unstructured_container.id != '0'
        if unstructured_container.type is not None:
            assert unstructured_container.type != 'bogus'
        
        assert unstructured_container.data is not None
        tuc.TestUnstructuredContainer.test_unstructured_container(unstructured_container.data)

def test_analyze_flow_org_json():
    container = {}
    text = {}
    text['text'] = TEXT
    unstructured = [text]
    container['unstructured'] = unstructured

    response = ACD_SERVICE.analyze_with_flow_org(FLOW, container,
                                          content_type='application/json')
    container_group = acd.ContainerGroup._from_dict(response.get_result())

    for unstructured_container in container_group.unstructured:
        if unstructured_container.text is not None:
            assert unstructured_container.text == TEXT
        if unstructured_container.id is not None:
            assert unstructured_container.id != '0'
        if unstructured_container.type is not None:
            assert unstructured_container.type != 'bogus'
        
        assert unstructured_container.data is not None
        tuc.TestUnstructuredContainer.test_unstructured_container(unstructured_container.data)

def test_analyze_org():

    config_entry = acd.ConfigurationEntity(id='test', type='test', uid=99)
    configs = [config_entry]

    allergy_annotator = acd.Annotator(name=acd.Name.ALLERGY)
    attr_detect_annotator = acd.Annotator(name=acd.Name.ATTRIBUTE_DETECTION)
    bathing_annotator = acd.Annotator(name=acd.Name.BATHING_ASSISTANCE)
    cancer_annotator = acd.Annotator(name=acd.Name.CANCER)
    concept_detect_annotator = acd.Annotator(name=acd.Name.CONCEPT_DETECTION)
    disambig_annotator = acd.Annotator(name=acd.Name.DISAMBIGUATION)
    dressing_annotator = acd.Annotator(name=acd.Name.DRESSING_ASSISTANCE)
    eating_annotator = acd.Annotator(name=acd.Name.EATING_ASSISTANCE)
    ef_annotator = acd.Annotator(name=acd.Name.EJECTION_FRACTION)
    hypothetical_annotator = acd.Annotator(name=acd.Name.HYPOTHETICAL)
    lab_value_annotator = acd.Annotator(name=acd.Name.LAB_VALUE)
    medication_annotator = acd.Annotator(name=acd.Name.MEDICATION)
    named_entities_annotator = acd.Annotator(name=acd.Name.NAMED_ENTITIES)
    negation_annotator = acd.Annotator(name=acd.Name.NEGATION)
    procedure_annotator = acd.Annotator(name=acd.Name.PROCEDURE)
    seeing_annotator = acd.Annotator(name=acd.Name.SEEING_ASSISTANCE)
    smoking_annotator = acd.Annotator(name=acd.Name.SMOKING)
    spelling_annotator = acd.Annotator(name=acd.Name.SPELL_CHECKER)
    symptom_disease_annotator = acd.Annotator(name=acd.Name.SYMPTOM_DISEASE)
    toileting_annotator = acd.Annotator(name=acd.Name.TOILETING_ASSISTANCE)
    walking_annotator = acd.Annotator(name=acd.Name.WALKING_ASSISTANCE)
    section = acd.Annotator(name=acd.Name.SECTION)
    model_broker = acd.Annotator(name=acd.Name.MODEL_BROKER)

    flow_entries = []
    flow_entries.append(acd.FlowEntry(allergy_annotator))
    flow_entries.append(acd.FlowEntry(attr_detect_annotator))
    flow_entries.append(acd.FlowEntry(bathing_annotator))
    flow_entries.append(acd.FlowEntry(cancer_annotator))
    flow_entries.append(acd.FlowEntry(concept_detect_annotator))
    flow_entries.append(acd.FlowEntry(disambig_annotator))
    flow_entries.append(acd.FlowEntry(dressing_annotator))
    flow_entries.append(acd.FlowEntry(eating_annotator))
    flow_entries.append(acd.FlowEntry(ef_annotator))
    flow_entries.append(acd.FlowEntry(hypothetical_annotator))
    flow_entries.append(acd.FlowEntry(lab_value_annotator))
    flow_entries.append(acd.FlowEntry(medication_annotator))
    flow_entries.append(acd.FlowEntry(named_entities_annotator))
    flow_entries.append(acd.FlowEntry(negation_annotator))
    flow_entries.append(acd.FlowEntry(procedure_annotator))
    flow_entries.append(acd.FlowEntry(seeing_annotator))
    flow_entries.append(acd.FlowEntry(smoking_annotator))
    flow_entries.append(acd.FlowEntry(spelling_annotator))
    flow_entries.append(acd.FlowEntry(symptom_disease_annotator))
    flow_entries.append(acd.FlowEntry(toileting_annotator))
    flow_entries.append(acd.FlowEntry(walking_annotator))
    flow_entries.append(acd.FlowEntry(section))
    flow_entries.append(acd.FlowEntry(model_broker))

    flow = acd.Flow(elements = flow_entries, async_ = False)
    annotator_flow = acd.AnnotatorFlow(flow=flow)

    containers = [acd.UnstructuredContainer(text=TEXT)]
    flows = [annotator_flow]

    response = ACD_SERVICE.analyze_org(containers, flows)
    container_group = acd.ContainerGroup._from_dict(response.get_result())

    for unstructured_container in container_group.unstructured:
        if unstructured_container.text is not None:
            assert unstructured_container.text == TEXT
        if unstructured_container.id is not None:
            assert unstructured_container.id != '0'
        if unstructured_container.type is not None:
            assert unstructured_container.type != 'bogus'
        
        assert unstructured_container.data is not None
        tuc.TestUnstructuredContainer.test_unstructured_container(data=unstructured_container.data)

def test_analyze():

    config_entry = acd.ConfigurationEntity(id='test', type='test', uid=99)
    configs = [config_entry]

    allergy_annotator = acd.Annotator(name=acd.Name.ALLERGY)
    attr_detect_annotator = acd.Annotator(name=acd.Name.ATTRIBUTE_DETECTION)
    bathing_annotator = acd.Annotator(name=acd.Name.BATHING_ASSISTANCE)
    cancer_annotator = acd.Annotator(name=acd.Name.CANCER)
    concept_detect_annotator = acd.Annotator(name=acd.Name.CONCEPT_DETECTION)
    disambig_annotator = acd.Annotator(name=acd.Name.DISAMBIGUATION)
    dressing_annotator = acd.Annotator(name=acd.Name.DRESSING_ASSISTANCE)
    eating_annotator = acd.Annotator(name=acd.Name.EATING_ASSISTANCE)
    ef_annotator = acd.Annotator(name=acd.Name.EJECTION_FRACTION)
    hypothetical_annotator = acd.Annotator(name=acd.Name.HYPOTHETICAL)
    lab_value_annotator = acd.Annotator(name=acd.Name.LAB_VALUE)
    medication_annotator = acd.Annotator(name=acd.Name.MEDICATION)
    named_entities_annotator = acd.Annotator(name=acd.Name.NAMED_ENTITIES)
    negation_annotator = acd.Annotator(name=acd.Name.NEGATION)
    procedure_annotator = acd.Annotator(name=acd.Name.PROCEDURE)
    seeing_annotator = acd.Annotator(name=acd.Name.SEEING_ASSISTANCE)
    smoking_annotator = acd.Annotator(name=acd.Name.SMOKING)
    spelling_annotator = acd.Annotator(name=acd.Name.SPELL_CHECKER)
    symptom_disease_annotator = acd.Annotator(name=acd.Name.SYMPTOM_DISEASE)
    toileting_annotator = acd.Annotator(name=acd.Name.TOILETING_ASSISTANCE)
    walking_annotator = acd.Annotator(name=acd.Name.WALKING_ASSISTANCE)
    section = acd.Annotator(name=acd.Name.SECTION)
    model_broker = acd.Annotator(name=acd.Name.MODEL_BROKER)

    flow_entries = []
    flow_entries.append(acd.FlowEntry(allergy_annotator))
    flow_entries.append(acd.FlowEntry(attr_detect_annotator))
    flow_entries.append(acd.FlowEntry(bathing_annotator))
    flow_entries.append(acd.FlowEntry(cancer_annotator))
    flow_entries.append(acd.FlowEntry(concept_detect_annotator))
    flow_entries.append(acd.FlowEntry(disambig_annotator))
    flow_entries.append(acd.FlowEntry(dressing_annotator))
    flow_entries.append(acd.FlowEntry(eating_annotator))
    flow_entries.append(acd.FlowEntry(ef_annotator))
    flow_entries.append(acd.FlowEntry(hypothetical_annotator))
    flow_entries.append(acd.FlowEntry(lab_value_annotator))
    flow_entries.append(acd.FlowEntry(medication_annotator))
    flow_entries.append(acd.FlowEntry(named_entities_annotator))
#    flow_entries.append(acd.FlowEntry(negation_annotator))
    flow_entries.append(acd.FlowEntry(procedure_annotator))
    flow_entries.append(acd.FlowEntry(seeing_annotator))
    flow_entries.append(acd.FlowEntry(smoking_annotator))
    flow_entries.append(acd.FlowEntry(spelling_annotator))
    flow_entries.append(acd.FlowEntry(symptom_disease_annotator))
    flow_entries.append(acd.FlowEntry(toileting_annotator))
    flow_entries.append(acd.FlowEntry(walking_annotator))
    flow_entries.append(acd.FlowEntry(section))
    flow_entries.append(acd.FlowEntry(model_broker))
    flow = acd.Flow(elements = flow_entries, async_ = False)
    annotator_flow = acd.AnnotatorFlow(flow)

    containers = [acd.UnstructuredContainer(text=TEXT)]

    data = ACD_SERVICE.analyze(TEXT, flow)
    tuc.TestUnstructuredContainer.test_unstructured_container(data=data)

def test_analyze_text_array():

    config_entry = acd.ConfigurationEntity(id='test', type='test', uid=99)
    configs = [config_entry]

    allergy_annotator = acd.Annotator(name=acd.Name.ALLERGY)
    attr_detect_annotator = acd.Annotator(name=acd.Name.ATTRIBUTE_DETECTION)
    bathing_annotator = acd.Annotator(name=acd.Name.BATHING_ASSISTANCE)
    cancer_annotator = acd.Annotator(name=acd.Name.CANCER)
    concept_detect_annotator = acd.Annotator(name=acd.Name.CONCEPT_DETECTION)
    disambig_annotator = acd.Annotator(name=acd.Name.DISAMBIGUATION)
    dressing_annotator = acd.Annotator(name=acd.Name.DRESSING_ASSISTANCE)
    eating_annotator = acd.Annotator(name=acd.Name.EATING_ASSISTANCE)
    ef_annotator = acd.Annotator(name=acd.Name.EJECTION_FRACTION)
    hypothetical_annotator = acd.Annotator(name=acd.Name.HYPOTHETICAL)
    lab_value_annotator = acd.Annotator(name=acd.Name.LAB_VALUE)
    medication_annotator = acd.Annotator(name=acd.Name.MEDICATION)
    named_entities_annotator = acd.Annotator(name=acd.Name.NAMED_ENTITIES)
    negation_annotator = acd.Annotator(name=acd.Name.NEGATION)
    procedure_annotator = acd.Annotator(name=acd.Name.PROCEDURE)
    seeing_annotator = acd.Annotator(name=acd.Name.SEEING_ASSISTANCE)
    smoking_annotator = acd.Annotator(name=acd.Name.SMOKING)
    spelling_annotator = acd.Annotator(name=acd.Name.SPELL_CHECKER)
    symptom_disease_annotator = acd.Annotator(name=acd.Name.SYMPTOM_DISEASE)
    toileting_annotator = acd.Annotator(name=acd.Name.TOILETING_ASSISTANCE)
    walking_annotator = acd.Annotator(name=acd.Name.WALKING_ASSISTANCE)
    section = acd.Annotator(name=acd.Name.SECTION)
    model_broker = acd.Annotator(name=acd.Name.MODEL_BROKER)

    flow_entries = []
    flow_entries.append(acd.FlowEntry(allergy_annotator))
    flow_entries.append(acd.FlowEntry(attr_detect_annotator))
    flow_entries.append(acd.FlowEntry(bathing_annotator))
    flow_entries.append(acd.FlowEntry(cancer_annotator))
    flow_entries.append(acd.FlowEntry(concept_detect_annotator))
    flow_entries.append(acd.FlowEntry(disambig_annotator))
    flow_entries.append(acd.FlowEntry(dressing_annotator))
    flow_entries.append(acd.FlowEntry(eating_annotator))
    flow_entries.append(acd.FlowEntry(ef_annotator))
    flow_entries.append(acd.FlowEntry(hypothetical_annotator))
    flow_entries.append(acd.FlowEntry(lab_value_annotator))
    flow_entries.append(acd.FlowEntry(medication_annotator))
    flow_entries.append(acd.FlowEntry(named_entities_annotator))
#    flow_entries.append(acd.FlowEntry(negation_annotator))
    flow_entries.append(acd.FlowEntry(procedure_annotator))
    flow_entries.append(acd.FlowEntry(seeing_annotator))
    flow_entries.append(acd.FlowEntry(smoking_annotator))
    flow_entries.append(acd.FlowEntry(spelling_annotator))
    flow_entries.append(acd.FlowEntry(symptom_disease_annotator))
    flow_entries.append(acd.FlowEntry(toileting_annotator))
    flow_entries.append(acd.FlowEntry(walking_annotator))
    flow_entries.append(acd.FlowEntry(section))
    flow_entries.append(acd.FlowEntry(model_broker))
    flow = acd.Flow(elements = flow_entries, async_ = False)
    annotator_flow = acd.AnnotatorFlow(flow)

    containers = [acd.UnstructuredContainer(text=TEXT)]

    container_group = ACD_SERVICE.analyze([TEXT], flow)

    for unstructured_container in container_group.unstructured:
        if unstructured_container.text is not None:
            assert unstructured_container.text == TEXT
        if unstructured_container.id is not None:
            assert unstructured_container.id != '0'
        if unstructured_container.type is not None:
            assert unstructured_container.type != 'bogus'
        
        assert unstructured_container.data is not None
        tuc.TestUnstructuredContainer.test_unstructured_container(data=unstructured_container.data)
