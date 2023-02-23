# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import configparser
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
import ibm_whcs_sdk.annotator_for_clinical_data as wh

CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/annotator_for_clinical_data/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
VERSION = CONFIG.get('settings', 'version')
LEVEL = CONFIG.get('settings', 'logging_level')
DISABLE_SSL = (CONFIG.get('settings', 'disable_ssl')=='True')
FLOW = CONFIG.get('settings', 'flow')

ACD = wh.AnnotatorForClinicalDataV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
ACD.set_service_url(BASE_URL)
ACD.set_disable_ssl_verification(DISABLE_SSL)

def test_get_flows():
    response = ACD.get_flows()
    flow_list = response.get_result()
    assert flow_list is not None
    for key in flow_list:
        flow = flow_list[key]
        assert flow is not None

def test_get_flows_id():
    response = ACD.get_flows_by_id(FLOW)
    flow = wh.AcdFlow._from_dict(response.get_result())
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
        flow = ACD.get_flows_by_id(FLOW)
    except wh.ACDException as acde:
        assert acde.code == 404

def test_create_flow():
    test_elementList = []
    test_anno = wh.Annotator(name = 'concept_detection', parameters = {"include_optional_fields": ["medical_codes", "source_vocabularies"]})
    test_flowEntry = wh.FlowEntry(annotator=test_anno)
    test_elementList.append(test_flowEntry)
    test_flow = wh.Flow(elements = test_elementList, async_ = False)
    test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    try:
        response = ACD.create_flows(new_id = 'unittest_new_flow', new_name = 'test flow',
                              new_description = 'functional test flow', new_annotator_flows = test_annoFlows)
        assert response is not None
    except wh.ACDException as acde:
        # flow already exists - previous delete must have failed
        assert acde.code == 409

def test_update_flow():
    test_elementList = []
    test_anno = wh.Annotator(name = 'concept_detection')
    test_flowEntry = wh.FlowEntry(annotator=test_anno)
    test_elementList.append(test_flowEntry)
    test_flow = wh.Flow(elements = test_elementList, async_ = True)
    test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    response = ACD.update_flows(id = "unittest_new_flow", new_id = "unittest_new_flow", new_name = 'test flow',
                                         new_description = 'functional test flow', new_annotator_flows = test_annoFlows)
    assert response is not None

def test_delete_flow():
    response = ACD.delete_flows(id = "unittest_new_flow")
    assert response is not None
