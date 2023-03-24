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

def test_get_flows():
    response = ACD_SERVICE.get_flows()
    flow_list = response.get_result()
    assert flow_list is not None
    for key in flow_list:
        flow = flow_list[key]
        assert flow is not None

def test_get_flows_id():
    response = ACD_SERVICE.get_flows_by_id(FLOW)
    flow = acd.AcdFlow._from_dict(response.get_result())
    assert flow is not None
    assert flow.id == FLOW
    assert flow.name is not None
    assert flow.description is not None
    annotator_flows = flow.annotator_flows
    if annotator_flows is not None:
        for annotator_flow in annotator_flows:
            assert annotator_flow.profile is not None
            assert annotator_flow.flow is not None

def test_get_bad_flows_id():
    try:
        flow = ACD_SERVICE.get_flows_by_id(FLOW)
    except acd.ACDException as acde:
        assert acde.code == 404

def test_create_flow():
    test_elementList = []
    test_anno = acd.Annotator(name = 'concept_detection', parameters = {"include_optional_fields": ["medical_codes", "source_vocabularies"]})
    test_flowEntry = acd.FlowEntry(annotator=test_anno)
    test_elementList.append(test_flowEntry)
    test_flow = acd.Flow(elements = test_elementList, async_ = False)
    test_annoFlow = acd.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    try:
        response = ACD_SERVICE.create_flows(new_id = 'unittest_new_flow', new_name = 'test flow',
                              new_description = 'functional test flow', new_annotator_flows = test_annoFlows)
        assert response is not None
    except acd.ACDException as acde:
        # flow already exists - previous delete must have failed
        assert acde.code == 409

def test_update_flow():
    test_elementList = []
    test_anno = acd.Annotator(name = 'concept_detection')
    test_flowEntry = acd.FlowEntry(annotator=test_anno)
    test_elementList.append(test_flowEntry)
    test_flow = acd.Flow(elements = test_elementList, async_ = True)
    test_annoFlow = acd.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    response = ACD_SERVICE.update_flows(id = "unittest_new_flow", new_id = "unittest_new_flow", new_name = 'test flow',
                                         new_description = 'functional test flow', new_annotator_flows = test_annoFlows)
    assert response is not None

def test_delete_flow():
    response = ACD_SERVICE.delete_flows(id = "unittest_new_flow")
    assert response is not None
