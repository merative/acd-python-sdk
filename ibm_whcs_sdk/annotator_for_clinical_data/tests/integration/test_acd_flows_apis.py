# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
import ibm_whcs_sdk.annotator_for_clinical_data as wh

CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/annotator_for_clinical_data/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
VERSION = CONFIG.get('settings', 'version')
LEVEL = CONFIG.get('settings', 'logging_level')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
FLOW = CONFIG.get('settings', 'flow')

ACD = wh.AnnotatorForClinicalDataV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_flows():
    response = ACD.get_flows()
    flow_list = response.get_result()
    assert flow_list is not None
    for key in flow_list:
        flow = flow_list[key]
        assert flow is not None

def test_get_flow():
    response = ACD.get_flow(FLOW)
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

def test_get_bad_flow():
    try:
        flow = ACD.get_flow(FLOW)
    except wh.ACDException as acde:
        assert acde.code == 404

def test_create_flow():
    test_elementList = []
    test_anno = wh.Annotator(name = 'concept_detection')
    test_flowEntry = wh.FlowEntry(annotator=test_anno)
    test_elementList.append(test_flowEntry)
    test_flow = wh.Flow(test_elementList, False)
    test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    try:
        response = ACD.create_persisted_flow(new_id = 'unittest_new_flow', new_name = 'test flow',
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
    test_flow = wh.Flow(test_elementList, True)
    test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
    test_annoFlows = []
    test_annoFlows.append(test_annoFlow)
    response = ACD.update_persisted_flow(flow_id = "unittest_new_flow", new_name = 'test flow',
                                         new_description = 'functional test flow', new_annotator_flows = test_annoFlows)
    assert response is not None

def test_delete_flow():
    response = ACD.delete_persisted_flow(id = "unittest_new_flow")
    assert response is not None
