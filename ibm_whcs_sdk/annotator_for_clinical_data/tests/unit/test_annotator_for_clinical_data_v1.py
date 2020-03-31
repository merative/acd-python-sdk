#from unittest import TestCase
import unittest
import configparser
import responses
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

#########################
# ACD
#########################


def check_for_null_or_error_resp(resp):
     if resp is None:
         return True
     else:
         if type(resp) == 'dict':
            if 'code' in resp:
                if resp['code'] > 299:
                   return True
     return False

class TestAnnotatorForClinicalDataV1(unittest.TestCase):

   # TEST:  Get an annotator definition
   #    - Get the definition of the 'concept_detection' annotator
   #    - Assert if response is None or response status code > 299
   def test_get_annotator_g(self):
        resp = ACD.get_annotator('concept_detection')
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get list of annotator definitions
   #    - Get the list of annotators
   #    - Assert if response is None or response status code > 299
   def test_list_annotators_g(self):
        resp = ACD.list_annotators()
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get list of flow definitions
   #    - Get the list of flows
   #    - Assert if response is None or response status code > 299
   def test_get_flows_g(self):
        resp = ACD.get_flows()
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get list of profile definitions
   #    - Get the list of profiles
   #    - Assert if response is None or response status code > 299
   def test_get_profiles_g(self):
        resp = ACD.get_profiles()
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get annotations using 'analyze_with_flow' with persisted flow
   #    - Get the definition of 'unittest_test_flow' flow
   #    - Assert if response is None or response status code > 299
   #    - If 'unittest_test_flow' does not exist, persist a new 'unittest_test_flow' definition
   #    - Call 'analyze_with_flow' using 'unittest_test_flow'
   #    - Verify expected annotations returned
   #    - Delete 'unittest_test_flow' flow
   #    - Assert if response is None or response status code > 299
   def test_analyze_with_flow_g(self):
        flow_id = "unittest_test_flow"
        try:
           resp = ACD.get_flow(flow_id)
           assert check_for_null_or_error_resp(resp) == False
           flow_exists = True
        except wh.ACDException as e:
           flow_exists = False
        if flow_exists == False:
           test_elementList = []
           test_anno = wh.Annotator(name = "concept_detection")
           test_flowEntry = wh.FlowEntry(annotator=test_anno)
           test_elementList.append(test_flowEntry)
           test_anno = wh.Annotator(name = "symptom_disease")
           test_flowEntry = wh.FlowEntry(annotator=test_anno)
           test_elementList.append(test_flowEntry)
           test_flow = wh.Flow(test_elementList, False)
           test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
           test_annoFlows = [test_annoFlow]
           resp = ACD.create_persisted_flow(new_id=flow_id, new_name="unittest test flow", new_description="Unittest Test Flow", new_annotator_flows=test_annoFlows)
        resp = ACD.analyze_with_flow(flow_id, "Patient has heart disease")
        assert resp.concepts is not None
        assert resp.symptom_disease_ind is not None
        resp = ACD.delete_persisted_flow(flow_id)
        assert check_for_null_or_error_resp(resp) == False

   # TEST:  Get annotations using 'analyze' with flow definition
   #    - Build a new Flow with the 'concept_detection' and 'symptom_disease' annotators
   #    - Call 'analyze' with some text and the new Flow
   #    - Assert if no concepts or symptom_disease_ind annotations returned
   def test_analyze(self):
        test_elementList = []
        test_anno = wh.Annotator(name = "concept_detection")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_anno = wh.Annotator(name = "symptom_disease")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_flow = wh.Flow(test_elementList, False)
        resp = ACD.analyze("Patient has diabetes", test_flow)
        assert resp.concepts is not None
        assert resp.symptom_disease_ind is not None

   # TEST:  Get annotations using 'analyze' with invalid flow definition
   #    - Build a new Flow with the 'concepts_detection' annotator
   #    - Call 'analyze' with some text and the new Flow
   #    - Assert if ACDException raised and unexpected error code
   def test_analyze_invalid_annotator_e(self):
        error_code = 400
        test_elementList = []
        test_anno = wh.Annotator(name = "concepts_detection")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_flow = wh.Flow(test_elementList, False)
        try:
           resp = ACD.analyze("Patient has diabetes", test_flow)
        except wh.ACDException as ex:
           assert ex.code == error_code

class TestAnnotatorForClinicalDataV1Mock():

   # TEST: Get an annotator definition using mock response
   #   - Build a mock GET /annotators/{id} response with HTTP 200
   #   - Get the mock 'concept detection' annotator definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_get_annotator_mock_g(self):
        endpoint = '/v1/annotators/concept_detection?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.GET,
                  url,
                  body="{\"description\": \"MOCK Detect UMLS concepts from medical data.\"}",
                  status=200,
                  content_type='application/json')
        ACD.get_annotator('concept_detection')
        assert len(responses.calls) == 1

   # TEST: Get an invalid annotator definition using mock response
   #   - Build a mock GET /annotators/{id} response with HTTP 400
   #   - Get the mock 'concepts detection' annotator definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_get_invalid_annotator_mock_e(self):
        endpoint = '/v1/annotators/concepts_detection?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 400
        responses.add(responses.GET,
                  url,
                  body="{}",
                  status=error_code,
                  content_type='application/json')
        try:
            ACD.get_annotator('concepts_detection')
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert ex.code == error_code

   # TEST:  Get list of annotator definitions using mock response
   #   - Build a mock GET /annotators response with HTTP 200
   #   - Get the mock list of annotator definitions
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_list_annotators_mock_g(self):
        endpoint = '/v1/annotators?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.GET,
                  url,
                  body="{\"allergy\": {\"description\": \"MOCK Detect allergy information from clinic notes.\"},\"attribute_detection\": {\"description\": \"MOCK **EXPERIMENTAL** Detect clinical attributes from a set of concepts and concept values.\"}}",
                  status=200,
                  content_type='application/json')
        ACD.list_annotators()
        assert len(responses.calls) == 1

   # TEST:  Get flow definition using mock response
   #   - Build a mock GET /flows/{id} response with HTTP 200
   #   - Get the 'unittest_flow' flow definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_get_flow_mock_g(self):
        endpoint = '/v1/flows/unittest_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 200
        responses.add(responses.GET,
                  url,
                  body="{\"id\": \"unittest_flow\", \"description\": \"Unittest Flow\", \"AnnotatorFlows\": [{\"flow\": {\"elements\": [{\"annotator\": {\"name\": \"concept_value\"}}], \"async\": false}}]}",
                  status=error_code,
                  content_type='application/json')
        ACD.get_flow('unittest_flow')
        assert len(responses.calls) == 1

   # TEST:  Get invalid flow definition using mock response
   #   - Build a mock GET /flows/{id} response with HTTP 404
   #   - Get the 'unittest_bogus_flow' flow definition
   #   - Assert if no ACDException is raised and expected text is not in mock response
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_get_invalid_flow_mock_e(self):
        endpoint = '/v1/flows/unittest_bogus_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 404
        responses.add(responses.GET,
                  url,
                  body="{\"code\": 404, \"message\": \"Flow ID: unittest_bogus_flow was not found in the list.\", \"correlationId\": \"MOCK\"}",
                  status=error_code,
                  content_type='application/json')
        try:
            ACD.get_flow('unittest_bogus_flow')
            assert 'Flow ID: unittest_bogus_flow was not found in the list.' in responses.calls[0].response.text
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert ex.code == error_code

   # TEST:  Get list of flow definitions using mock response
   #   - Build a mock GET /flows response with HTTP 200
   #   - Get the mock list of flow definitions
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_get_flows_mock_g(self):
        endpoint = '/v1/flows?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.GET,
                  url,
                  body="{\"mock_flow1\": {\"description\": \"MOCK Flow1 Unittest\"},\"mock_flow2\": {\"description\": \"MOCK Flow2 Unittest\"}}",
                  status=200,
                  content_type='application/json')
        ACD.get_flows()
        assert len(responses.calls) == 1

   # TEST:  Get profile definition using mock response
   #   - Build a mock GET /profile/{id} response with HTTP 200
   #   - Get the 'unittest_profile' profile definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_get_profile_mock_g(self):
        endpoint = '/v1/profiles/unittest_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 200
        responses.add(responses.GET,
                  url,
                  body="{\"id\": \"unittest_profile\", \"name\": \"Unittest Profile\", \"description\": \"Unittest Profile Description\", \"annotators\": [{\"name\": \"concept_detection\", \"parameters\": {\"libraries\": [\"umls.latest\"]}}]}",
                  status=error_code,
                  content_type='application/json')
        ACD.get_profile('unittest_profile')
        assert len(responses.calls) == 1

   # TEST:  Get invalid profile definition using mock response
   #   - Build a mock GET /profiles/{id} response with HTTP 404
   #   - Get the 'unittest_bogus_profile' profile definition
   #   - Assert if no ACDException is raised and expected text not in mock response
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_get_invalid_profile_mock_e(self):
        endpoint = '/v1/profiles/unittest_bogus_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 404
        responses.add(responses.GET,
                  url,
                  body="{\"code\": 404, \"message\": \"Profile ID: unittest_bogus_profile was not found in the list.\", \"correlationId\": \"MOCK\"}",
                  status=error_code,
                  content_type='application/json')
        try:
            ACD.get_profile('unittest_bogus_profile')
            assert 'Profile ID: unittest_bogus_profile was not found in the list.' in responses.calls[0].response.text
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert ex.code == error_code

   # TEST:  Get list of profile definitions using mock response
   #   - Build a mock GET /profiles response with HTTP 200
   #   - Get the mock list of profile definitions
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_get_profiles_mock_g(self):
        endpoint = '/v1/profiles?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.GET,
                  url,
                  body="{\"mock_profile1\": {\"description\": \"MOCK Profile1 Unittest\"},\"mock_profile2\": {\"description\": \"MOCK Profile2 Unittest\"}}",
                  status=200,
                  content_type='application/json')
        ACD.get_profiles()
        assert len(responses.calls) == 1

   # TEST:  Persist new flow definition using mock response
   #   - Build a mock POST /flows response with HTTP 201
   #   - Persist the new flow definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_create_flow_mock_g(self):
        # Success = HTTP 201 with no response body.  This conflicts with setting header 'Accept: application/json'
        # With mock responses, will set 'body={}' to prevent JSONDecodeError
        endpoint = '/v1/flows?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.POST,
                  url,
                  body="{}",
                  status=201,
                  content_type='application/json')
        test_elementList = []
        test_anno = wh.Annotator(name = "concept_detection")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_flow = wh.Flow(test_elementList, False)
        test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
        test_annoFlows = []
        test_annoFlows.append(test_annoFlow)
        ACD.create_persisted_flow(new_id = "unittest_new_flow", new_annotator_flows = test_annoFlows)
        assert len(responses.calls) == 1

   # TEST:  Persist new invalid flow definition using mock response
   #   - Build a mock POST /flows response with HTTP 409
   #   - Persist the new invalid flow definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_create_invalid_flow_mock_e(self):
        endpoint = '/v1/flows?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 409
        responses.add(responses.POST,
                  url,
                  body="{\"code\": 409, \"message\": \"Conflict\", \"level\": \"ERROR\", \"description\": \"Flow ID unittest_new_flow already exists\", \"correlationId\": \"123456789\"}",
                  status=409,
                  content_type='application/json')
        test_elementList = []
        test_anno = wh.Annotator(name = "concept_detection")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_flow = wh.Flow(test_elementList, False)
        test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
        test_annoFlows = []
        test_annoFlows.append(test_annoFlow)
        try:
            ACD.create_persisted_flow(new_id = "unittest_new_flow", new_annotator_flows = test_annoFlows)
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Persist new profile definition using mock response
   #   - Build a mock POST /profiles response with HTTP 201
   #   - Persist the new profile definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_create_profile_mock_g(self):
        # Success = HTTP 201 with no response body.  This conflicts with setting header 'Accept: application/json'
        # With mock responses, will set 'body={}' to prevent JSONDecodeError
        endpoint = '/v1/profiles?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.POST,
                  url,
                  body="{}",
                  status=201,
                  content_type='application/json')
        test_annoList = []
        test_anno = wh.Annotator(name = "concept_detection", parameters = "{\"libraries\": [\"umls.latest\"]}")
        test_annoList.append(test_anno)
        ACD.create_profile(new_id = "unittest_new_profile", new_annotators = test_annoList)
        assert len(responses.calls) == 1

   # TEST:  Persist new invalid profile definition using mock response
   #   - Build a mock POST /flows response with HTTP 400
   #   - Persist the new invalid profile definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_create_invalid_profile_mock_e(self):
        endpoint = '/v1/profiles?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 400
        responses.add(responses.POST,
                  url,
                  body="{\"code\":400, \"message\": \"Bad Request\", \"level\": \"ERROR\", \"correlationId\": \"MOCK\"}",
                  status=error_code,
                  content_type='application/json')
        test_annoList = []
        try:
            ACD.create_profile(new_id = "unittest_bad_profile", new_annotators = test_annoList)
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Delete profile definition using mock response
   #   - Build a mock DELETE /profiles/{id} response with HTTP 200
   #   - Delete the 'unittest_profile' profile definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_delete_profile_mock_g(self):
        endpoint = '/v1/profiles/unittest_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.DELETE,
                  url,
                  body="{}",
                  status=200,
                  content_type='application/json')
        ACD.delete_profile('unittest_profile')
        assert len(responses.calls) == 1

   # TEST:  Delete invalid profile definition using mock response
   #   - Build a mock DELETE /profiles/{id} response with HTTP 404
   #   - Persist the new invalid profile definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_delete_invalid_profile_mock_e(self):
        endpoint = '/v1/profiles/unittest_bad_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 404
        responses.add(responses.DELETE,
                  url,
                  body="{\"code\":404, \"message\": \"Profile ID: unittest_bad_profile was not found in the list.\", \"level\": \"ERROR\", \"correlationId\": \"12345678\"}",
                  status=error_code,
                  content_type='application/json')
        try:
            ACD.delete_profile("unittest_bad_profile")
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Delete flow definition using mock response
   #   - Build a mock DELETE /flows/{id} response with HTTP 200
   #   - Delete the 'unittest_flow' flow definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_delete_flow_mock_g(self):
        endpoint = '/v1/flows/unittest_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.DELETE,
                  url,
                  body="{}",
                  status=200,
                  content_type='application/json')
        ACD.delete_persisted_flow('unittest_flow')
        assert len(responses.calls) == 1

   # TEST:  Delete invalid flow definition using mock response
   #   - Build a mock DELETE /flows/{id} response with HTTP 404
   #   - Persist the new invalid flows definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_delete_invalid_flow_mock_e(self):
        endpoint = '/v1/flows/unittest_bad_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 404
        responses.add(responses.DELETE,
                  url,
                  body="{\"code\":404, \"message\": \"Flow ID: unittest_bad_flow was not found in the list.\", \"level\": \"ERROR\", \"correlationId\": \"12345678\"}",
                  status=error_code,
                  content_type='application/json')
        try:
            ACD.delete_persisted_flow("unittest_bad_flow")
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Update profile definition using mock response
   #   - Build a mock PUT /profiles/{id} response with HTTP 200
   #   - Update with the new profile definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_update_profile_mock_g(self):
        endpoint = '/v1/profiles/unittest_new_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.PUT,
                  url,
                  body="{}",
                  status=200,
                  content_type='application/json')
        test_annoList = []
        test_anno = wh.Annotator(name = "concept_detection", parameters = "{\"libraries\": [\"umls.latest\"]}")
        test_annoList.append(test_anno)
        ACD.update_profile(id = "unittest_new_profile", new_annotators = test_annoList)
        assert len(responses.calls) == 1

   # TEST:  Update flow definition using mock response
   #   - Build a mock PUT /flows/{id} response with HTTP 200
   #   - Update with the new flow definition
   #   - Assert if Responses call count != 1
   @responses.activate
   def test_update_flow_mock_g(self):
        endpoint = '/v1/flows/unittest_new_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.PUT,
                  url,
                  body="{}",
                  status=200,
                  content_type='application/json')
        test_elementList = []
        test_anno = wh.Annotator(name = "concept_detection")
        test_flowEntry = wh.FlowEntry(annotator=test_anno)
        test_elementList.append(test_flowEntry)
        test_flow = wh.Flow(test_elementList, False)
        test_annoFlow = wh.AnnotatorFlow(flow = test_flow)
        test_annoFlows = []
        test_annoFlows.append(test_annoFlow)
        ACD.update_persisted_flow(id = "unittest_new_flow", new_annotator_flows = test_annoFlows)
        assert len(responses.calls) == 1

   # TEST:  Update invalid profile definition using mock response
   #   - Build a mock PUT /profiles/{id} response with HTTP 404
   #   - Update with the invalid profile definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_update_invalid_profile_mock_e(self):
        endpoint = '/v1/profiles/unittest_bad_profile?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 404
        responses.add(responses.PUT,
                  url,
                  body="{\"code\": 404, \"message\": \"Profile ID: unittest_bad_profile was not found in the list.\", \"level\": \"ERROR\", \"correlationId\": \"12345678\"}",
                  status = error_code,
                  content_type='application/json')
        test_annoList = []
        try:
            ACD.update_profile(id = "unittest_bad_profile", new_annotators = test_annoList)
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Update invalid flow definition using mock response
   #   - Build a mock PUT /flows/{id} response with HTTP 400
   #   - Update with the invalid flow definition
   #   - Assert if ACDException is raised and Responses call count != 1 or unexpected ACDException code
   @responses.activate
   def test_update_invalid_flow_mock_e(self):
        endpoint = '/v1/flows/unittest_bad_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        error_code = 400
        responses.add(responses.PUT,
                  url,
                  body="{\"code\": 400, \"message\": \"Bad Request\", \"level\": \"ERROR\", \"correlationId\": \"MOCK\"}",
                  status=error_code,
                  content_type='application/json')
        test_annoFlows = []
        try:
            ACD.update_persisted_flow(id = "unittest_bad_flow", new_annotator_flows = test_annoFlows)
        except wh.ACDException as ex:
            assert len(responses.calls) == 1
            assert error_code == ex.code

   # TEST:  Get annotations using 'analyze_with_flow' with invalid flow using mock response
   #    - Build a mock POST /analyze/{id} response with HTTP 404
   #    - Call 'analyze/{id}'
   #    - Assert if Responses call count != 1
   @responses.activate
   def test_analyze_with_flow_invalid_flow_mock_e(self):
        error_code = 404
        endpoint = '/v1/analyze/unittest_bogus_flow?version=2017-08-04'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.POST,
                  url,
                  body="{\"code\": 404, \"message\": \"Flow ID: unittest_bogus_flow was not found in the list.\", \"level\": \"ERROR\", \"correlationId\": \"12345678\"}",
                  status = 404,
                  content_type='application/json')
        try:
           resp = ACD.analyze_with_flow("unittest_bogus_flow", "Patient has heart disease")
        except wh.ACDException as ex:
           assert ex.code == error_code

   # TEST:  Delete user_data using 'delete' invalid tenant_id using mock response
   #    - Build a mock DELETE /user_data response with HTTP 400
   #    - Call 'delete'
   #    - Assert if Responses call count != 1
   @responses.activate
   def test_delete_user_data_mock_e(self):
        error_code = 400
        endpoint = '/v1/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.DELETE,
                  url,
                  body="{\"code\": 400, \"message\": \"The tenant id could not be determined from the request.\", \"level\": \"ERROR\", \"correlationId\": \"12345678\"}",
                  status = 400,
                  content_type='application/json')
        try:
            resp = ACD.delete_user_data()
        except wh.ACDException as ex:
            print ("Error Occurred:  Code ", ex.code, " Message ", ex.message, " CorrelationId ", ex.correlationId)
            assert ex.code == error_code


#########################
# ACD - data model
#########################

def test_concept_model():
    dict_concept = {
      u'id': '0',
      u'uid': 0,
      u'begin': 733,
      u'coveredText': u'inpatient',
      u'cui': u'C0021562',
      u'disambiguationData': {u'validity': u'VALID'},
      u'end': 742,
      u'hypothetical': False,
      u'loincId': u'LP32937-2,LA6511-5',
      u'meshId': u'M0011377',
      u'nciCode': u'C25182',
      u'negated': False,
      u'preferredName': u'inpatient',
      u'semanticType': u'podg',
      u'snomedConceptId': u'416800000',
      u'source': u'umls',
      u'sourceVersion': u'2018AA',
      u'type': u'umls.PatientOrDisabledGroup',
      u'vocabs': u'MTH,LNC,NCI',
      u'icd9Code': u'MOCK9',
      u'icd10Code': u'MOCK10',
      u'snomedConceptId': u'MOCK-snomed',
      u'rxNormId': u'MOCK-rx',
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'cptCode': u'44950,44955,1014622,1007583',
      u'unknownField': u'MOCK-unknown',
    }

    concept = wh.Concept._from_dict(dict_concept)
    assert concept.id == '0'
    assert concept.type == 'umls.PatientOrDisabledGroup'
    assert concept.uid == 0
    assert concept.begin == 733
    assert concept.end == 742
    assert concept.covered_text == 'inpatient'
    assert concept.negated == False
    assert concept.hypothetical == False
    assert concept.cui == 'C0021562'
    assert concept.preferred_name == 'inpatient'
    assert concept.semantic_type == 'podg'
    assert concept.source == 'umls'
    assert concept.source_version == '2018AA'
    assert isinstance(concept.disambiguation_data, wh.Disambiguation)
    assert concept.disambiguation_data.validity == 'VALID'
    assert concept.icd9_code == 'MOCK9'
    assert concept.icd10_code == 'MOCK10'
    assert concept.nci_code == 'C25182'
    assert concept.snomed_concept_id == 'MOCK-snomed'
    assert concept.mesh_id == 'M0011377'
    assert concept.rx_norm_id == 'MOCK-rx'
    assert concept.loinc_id == 'LP32937-2,LA6511-5'
    assert concept.vocabs == 'MTH,LNC,NCI'
    assert concept.section_normalized_name == 'MOCK-sectionName'
    assert concept.section_surface_form == 'MOCK-sectionSurfaceForm'
    assert concept.cpt_code == '44950,44955,1014622,1007583'
    # make sure all fields were known and got parsed explicitly
    assert concept._additionalProperties == set(['unknownField'])
    assert concept.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = concept._to_dict()

    # make sure we're robust to alternative rxNormID capitalization
    dict_concept = {
      u'rxNormID': u'MOCK-rx',
    }
    concept = wh.Concept._from_dict(dict_concept)
    assert concept.rx_norm_id == 'MOCK-rx'
    assert concept._additionalProperties == set([])

def test_concept_value_model():
    dict_concept_value = {
      u'id': '0',
      u'type': 'umls.PatientOrDisabledGroup',
      u'uid': 0,
      u'begin': 733,
      u'coveredText': u'inpatient',
      u'cui': u'C0021562',
      u'end': 742,
      u'hypothetical': False,
      u'negated': False,
      u'preferredName': u'inpatient',
      u'source': u'umls',
      u'trigger': u'MOCK-trigger',
      u'value': u'MOCK-value',
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'unknownField': u'MOCK-unknown',
    }

    concept_value = wh.ConceptValue._from_dict(dict_concept_value)
    assert concept_value.id == '0'
    assert concept_value.type == 'umls.PatientOrDisabledGroup'
    assert concept_value.uid == 0
    assert concept_value.begin == 733
    assert concept_value.end == 742
    assert concept_value.covered_text == 'inpatient'
    assert concept_value.negated == False
    assert concept_value.hypothetical == False
    assert concept_value.cui == 'C0021562'
    assert concept_value.preferred_name == 'inpatient'
    assert concept_value.trigger == 'MOCK-trigger'
    assert concept_value.source == 'umls'
    assert concept_value.value == 'MOCK-value'
    assert concept_value.section_normalized_name == 'MOCK-sectionName'
    assert concept_value.section_surface_form == 'MOCK-sectionSurfaceForm'
    # make sure all fields were known and got parsed explicitly
    assert concept_value._additionalProperties == set(['unknownField'])
    assert concept_value.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = concept_value._to_dict()

def test_attribute_model():
    dict_attr = {
      u'id': '0',
      u'uid': 0,
      u'begin': 733,
      u'coveredText': u'inpatient',
      u'concept': {u'cui': u'C0021562'},
      u'end': 742,
      u'hypothetical': False,
      u'loincId': u'LP32937-2,LA6511-5',
      u'meshId': u'M0011377',
      u'nciCode': u'C25182',
      u'negated': False,
      u'preferredName': u'inpatient',
      u'snomedConceptId': u'416800000',
      u'source': u'umls',
      u'sourceVersion': u'2018AA',
      u'type': u'umls.PatientOrDisabledGroup',
      u'vocabs': u'MTH,LNC,NCI',
      u'icd9Code': u'MOCK9',
      u'icd10Code': u'MOCK10',
      u'snomedConceptId': u'MOCK-snomed',
      u'rxNormId': u'MOCK-rx',
      u'values': [{
          'value':'MOCK-attr-value',
          'frequency':'MOCK-attr-frequency',
          'duration':'MOCK-attr-duration',
          'unit':'MOCK-attr-unit',
          'dimension':'MOCK-attr-dimension'
      }],
      u'name': u'MOCK-name',
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'cptCode': u'44950,44955,1014622,1007583',
      u'disambiguationData': {u'validity': u'VALID'},
      u'unknownField': u'MOCK-unknown',
    }

    attr = wh.AttributeValueAnnotation._from_dict(dict_attr)
    assert attr.id == '0'
    assert attr.type == 'umls.PatientOrDisabledGroup'
    assert attr.uid == 0
    assert attr.begin == 733
    assert attr.end == 742
    assert attr.covered_text == 'inpatient'
    assert attr.negated == False
    assert attr.hypothetical == False
    assert attr.preferred_name == 'inpatient'
    assert len(attr.values) == 1
    assert isinstance(attr.values[0], wh.AttributeValueEntry)
    # make sure we can access values as class fields
    assert attr.values[0].value == 'MOCK-attr-value'
    assert attr.values[0].frequency == 'MOCK-attr-frequency'
    assert attr.values[0].duration == 'MOCK-attr-duration'
    assert attr.values[0].unit == 'MOCK-attr-unit'
    assert attr.values[0].dimension == 'MOCK-attr-dimension'
    # make sure we can access values as dict entries (for backwards compatibility)
    assert attr.values[0]['value'] == 'MOCK-attr-value'
    assert attr.values[0]['frequency'] == 'MOCK-attr-frequency'
    assert attr.values[0]['duration'] == 'MOCK-attr-duration'
    assert attr.values[0]['unit'] == 'MOCK-attr-unit'
    assert attr.values[0]['dimension'] == 'MOCK-attr-dimension'
    assert attr.source == 'umls'
    assert attr.source_version == '2018AA'
    assert isinstance(attr.concept, wh.Concept)
    assert attr.concept.cui == 'C0021562'
    assert attr.name == 'MOCK-name'
    assert attr.icd9_code == 'MOCK9'
    assert attr.icd10_code == 'MOCK10'
    assert attr.nci_code == 'C25182'
    assert attr.snomed_concept_id == 'MOCK-snomed'
    assert attr.mesh_id == 'M0011377'
    assert attr.rx_norm_id == 'MOCK-rx'
    assert attr.loinc_id == 'LP32937-2,LA6511-5'
    assert attr.vocabs == 'MTH,LNC,NCI'
    assert attr.section_normalized_name == 'MOCK-sectionName'
    assert attr.section_surface_form == 'MOCK-sectionSurfaceForm'
    assert attr.cpt_code == '44950,44955,1014622,1007583'
    assert isinstance(attr.disambiguation_data, wh.Disambiguation)
    assert attr.disambiguation_data.validity == 'VALID'
    # make sure all fields were known and got parsed explicitly
    assert attr._additionalProperties == set(['unknownField'])
    assert attr.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = attr._to_dict()

    # make sure we're robust to alternative rxNormID capitalization
    dict_attr = {
      u'rxNormID': u'MOCK-rx',
    }
    attr = wh.AttributeValueAnnotation._from_dict(dict_attr)
    assert attr.rx_norm_id == 'MOCK-rx'
    assert attr._additionalProperties == set([])

def test_section_model():
    dict_section = {
      u'begin': 0,
      u'coveredText': u'FAMILY HISTORY etc...',
      u'end': 756,
      u'trigger': {
        u'begin': 0,
        u'coveredText': u'FAMILY HISTORY',
        u'end': 14,
        u'sectionNormalizedName': u'family history',
        u'source': u'internal',
        u'type': u'aci.SectionTrigger'},
      u'type': u'aci.Section',
      u'sectionType': u'MOCK-sectiontype',
      u'unknownField': u'MOCK-unknown',
    }

    section = wh.Section._from_dict(dict_section)
    assert section.begin == 0
    assert section.covered_text == 'FAMILY HISTORY etc...'
    assert section.end == 756
    assert section.type == 'aci.Section'
    assert section.section_type == 'MOCK-sectiontype'
    assert isinstance(section.trigger, wh.SectionTrigger)
    assert section.trigger.begin == 0
    assert section.trigger.covered_text == 'FAMILY HISTORY'
    assert section.trigger.end == 14
    assert section.trigger.section_normalized_name == 'family history'
    assert section.trigger.source == 'internal'
    assert section.trigger.type == 'aci.SectionTrigger'
    # make sure all fields were known and got parsed explicitly
    assert section._additionalProperties == set(['unknownField'])
    assert section.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = section._to_dict()

def test_annotation_model():
    dict_annotation = {
      u'begin': 0,
      u'coveredText': u'FAMILY HISTORY etc...',
      u'end': 756,
      u'type': u'aci.MOCK-annotation',
      u'negated': True,
      u'hypothetical': False,
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'unknownField': u'MOCK-unknown',
    }

    annotation = wh.Annotation._from_dict(dict_annotation)
    assert annotation.begin == 0
    assert annotation.covered_text == 'FAMILY HISTORY etc...'
    assert annotation.end == 756
    assert annotation.type == 'aci.MOCK-annotation'
    assert annotation.negated == True
    assert annotation.hypothetical == False
    assert annotation.section_normalized_name == 'MOCK-sectionName'
    assert annotation.section_surface_form == 'MOCK-sectionSurfaceForm'
    # make sure all fields were known and got parsed explicitly
    assert annotation._additionalProperties == set(['unknownField'])
    assert annotation.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = annotation._to_dict()

def test_assistance_model():
    dict_assistance = {
      u'begin': 0,
      u'coveredText': u'FAMILY HISTORY etc...',
      u'end': 756,
      u'type': u'aci.MOCK-assistance',
      u'negated': True,
      u'hypothetical': False,
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'primaryActionNormalizedName': u'MOCK-primaryActionNormalizedName',
      u'modality': u'MOCK-modality',
      u'primaryActionSurfaceForm': u'MOCK-primaryActionSurfaceForm',
      u'unknownField': u'MOCK-unknown',
    }

    assistance = wh.AssistanceAnnotation._from_dict(dict_assistance)
    assert assistance.begin == 0
    assert assistance.covered_text == 'FAMILY HISTORY etc...'
    assert assistance.end == 756
    assert assistance.type == 'aci.MOCK-assistance'
    assert assistance.negated == True
    assert assistance.hypothetical == False
    assert assistance.section_normalized_name == 'MOCK-sectionName'
    assert assistance.section_surface_form == 'MOCK-sectionSurfaceForm'
    assert assistance.primary_action_normalized_name == 'MOCK-primaryActionNormalizedName'
    assert assistance.modality == 'MOCK-modality'
    assert assistance.primary_action_surface_form == 'MOCK-primaryActionSurfaceForm'
    # make sure all fields were known and got parsed explicitly
    assert assistance._additionalProperties == set(['unknownField'])
    assert assistance.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = assistance._to_dict()

def test_allergymed_model():
    dict_allergymed = {
      u'begin': 0,
      u'coveredText': u'FAMILY HISTORY etc...',
      u'end': 756,
      u'type': u'aci.MOCK-allergymed',
      u'negated': True,
      u'hypothetical': False,
      u'sectionNormalizedName': u'MOCK-sectionName',
      u'sectionSurfaceForm': u'MOCK-sectionSurfaceForm',
      u'medication': [{
        u'begin': 97,
        u'coveredText': u'penicillin',
        u'cui': u'C0220892',
        u'drug': [{u'begin': 97,
          u'complex': u'false',
          u'coveredText': u'penicillin',
          u'cui': u'C0220892',
          u'end': 107,
          u'name1': [{u'begin': 97,
            u'coveredText': u'penicillin',
            u'cui': u'C0220892',
            u'drugNormalizedName': u'penicillin',
            u'drugSurfaceForm': u'penicillin',
            u'end': 107,
            u'rxNormID': u'70618',
            u'type': u'aci.DrugName'}],
          u'type': u'aci.Ind_Drug'}],
        u'end': 107,
        u'type': u'aci.MedicationInd'
      }],
      u'unknownField': u'MOCK-unknown',
    }

    allergymed = wh.AllergyMedication._from_dict(dict_allergymed)
    assert allergymed.begin == 0
    assert allergymed.covered_text == 'FAMILY HISTORY etc...'
    assert allergymed.end == 756
    assert allergymed.type == 'aci.MOCK-allergymed'
    assert allergymed.negated == True
    assert allergymed.hypothetical == False
    assert allergymed.section_normalized_name == 'MOCK-sectionName'
    assert allergymed.section_surface_form == 'MOCK-sectionSurfaceForm'
    assert isinstance(allergymed.medication, list)
    assert len(allergymed.medication) == 1
    assert isinstance(allergymed.medication[0], wh.MedicationAnnotation)
    assert allergymed.medication[0].begin == 97
    assert allergymed.medication[0].end == 107
    assert allergymed.medication[0].cui == 'C0220892'
    assert allergymed.medication[0].covered_text == 'penicillin'
    assert allergymed.medication[0].type == 'aci.MedicationInd'
    assert isinstance(allergymed.medication[0].drug, list)
    assert len(allergymed.medication[0].drug)==1
    # Note: in the future we may want to change drug from a dict into a proper class; then this will need to change
    assert isinstance(allergymed.medication[0].drug[0], dict)
    # make sure all fields were known and got parsed explicitly
    assert allergymed._additionalProperties == set(['unknownField'])
    assert allergymed.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = allergymed._to_dict()

def test_nlu_entities_model():
    dict_nlu_entities = {
      u'begin': 0,
      u'coveredText': u'amoxicillin',
      u'end': 11,
      u'type': u'Drug',
      u'source': u'IBM Default NLU Model',
      u'relevance': 0.223901,
      u'unknownField': u'MOCK-unknown',
    }

    nlu_entities = wh.NluEntities._from_dict(dict_nlu_entities)
    assert nlu_entities.begin == 0
    assert nlu_entities.covered_text == 'amoxicillin'
    assert nlu_entities.end == 11
    assert nlu_entities.type == 'Drug'
    assert nlu_entities.source == 'IBM Default NLU Model'
    assert nlu_entities.relevance == 0.223901
    # make sure all fields were known and got parsed explicitly
    assert nlu_entities._additionalProperties == set(['unknownField'])
    assert nlu_entities.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = nlu_entities._to_dict()

def test_relations_model():
    dict_relations = {
      u'source': u'IBM Default NLU Model',
      u'score': 0.932613,
      u'nodes': [{
        u'entity': {
          u'uid': 1}}],
      u'type': u'hasAttribute',
      u'unknownField': u'MOCK-unknown',
    }

    relations = wh.Relations._from_dict(dict_relations)
    assert relations.source == 'IBM Default NLU Model'
    assert relations.score == 0.932613
    assert isinstance(relations.nodes[0], wh.Node)
    assert len(relations.nodes[0].entity) == 1
    assert isinstance(relations.nodes[0].entity, dict)
    assert relations.type == 'hasAttribute'
    # make sure all fields were known and got parsed explicitly
    assert relations._additionalProperties == set(['unknownField'])
    assert relations.unknownField == 'MOCK-unknown'
    # make sure that _to_dict doesn't blow up
    _ = relations._to_dict()

def test_spelling_corrections_model():
    dict_spelling_corrections = {
        u'begin' : 0,
        u'end' : 9,
        u'coveredText' : u'Patientts',
        u'suggestions' : [{
                           u'applied' : True,
                           u'confidence' : 0.96,
                           u'semtypes' : [ "umls.patientOrDisabledGroup"],
                           u'text' : "Patients"
                           },
                           {
                           u'applied' : False,
                           u'confidence' : 0.85,
                           u'semtypes' : [ "umls.patientOrDisabledGroup"],
                           u'text' : "Patient"
                           }
                          ]
    }

    correction = wh.SpellingCorrection._from_dict(dict_spelling_corrections)
    assert correction.begin == 0
    assert correction.end == 9
    assert correction.covered_text == u'Patientts'
    assert len(correction.suggestions) == 2
    suggestion = correction.suggestions[0]
    assert suggestion.applied == True
    assert suggestion.confidence == 0.96
    assert len(suggestion.semtypes) == 1
    assert suggestion.semtypes[0] == "umls.patientOrDisabledGroup"
    assert suggestion.text == "Patients"
    suggestion = correction.suggestions[1]
    assert suggestion.applied == False
    assert suggestion.confidence == 0.85
    assert len(suggestion.semtypes) == 1
    assert suggestion.semtypes[0] == "umls.patientOrDisabledGroup"
    assert suggestion.text == "Patient"

    # make the deserialized dict equals the original dict
    assert correction._to_dict() == dict_spelling_corrections

def test_spell_corrected_text_model():
    dict_spell_corrected_text = {
        u'correctedText' : u'Patients with stage II breast cancer',
        u'debugText' : ">>>Patientts->Patients(0.96) <<< with stage II >>>breast cancre->breast cancer(0.97)<<<"
    }
    spell_corrected_text = wh.SpellCorrectedText._from_dict(dict_spell_corrected_text)
    assert spell_corrected_text.corrected_text == "Patients with stage II breast cancer"
    assert spell_corrected_text.debug_text == ">>>Patientts->Patients(0.96) <<< with stage II >>>breast cancre->breast cancer(0.97)<<<"

     # make the deserialized dict equals the original dict
    assert spell_corrected_text._to_dict() == dict_spell_corrected_text

def test_spelling_corrections_at_container_level():
    container_json = '''
    {
        "unstructured": [
          {
            "text": "Patientts with stage II breast cancre",
            "data": {
              "spellCorrectedText": [
                {
                  "correctedText": "Patients with stage II breast cancer",
                  "debugText": ">>>Patientts->Patients(0.96) <<< with stage II >>>breast cancre->breast cancer(0.97)<<<"
                }
              ],
              "spellingCorrections": [
                {
                  "begin": 0,
                  "end": 9,
                  "coveredText": "Patientts",
                  "suggestions": [
                    {
                      "applied": true,
                      "confidence": 0.96,
                      "semtypes": [
                        "umls.PatientOrDisabledGroup"
                      ],
                      "text": "Patients"
                    },
                    {
                      "applied": false,
                      "confidence": 0.85,
                      "semtypes": [
                        "umls.PatientOrDisabledGroup"
                      ],
                      "text": "Patient"
                    },
                    {
                      "applied": false,
                      "confidence": 0.85,
                      "semtypes": [
                        "umls.IntellectualProduct"
                      ],
                      "text": "Patents"
                    },
                    {
                      "applied": false,
                      "confidence": 0.7,
                      "text": "Patiently"
                    }
                  ]
                },
                {
                  "begin": 24,
                  "end": 37,
                  "coveredText": "breast cancre",
                  "suggestions": [
                    {
                      "applied": true,
                      "confidence": 0.97,
                      "semtypes": [
                        "umls.NeoplasticProcess"
                      ],
                      "text": "breast cancer"
                    }
                  ]
                }
              ]
            }
          }
        ]
        }'''
    #Convert the json string to native dict
    container_dict = json.loads(container_json)
    # load the first container
    container_obj = wh.ContainerAnnotation._from_dict(container_dict['unstructured'][0]['data'])
    #do some basic checks of the container to ensure the basic structure of the objects was loaded
    assert container_obj.spelling_corrections[0].covered_text == "Patientts"
    assert container_obj.spelling_corrections[1].covered_text == "breast cancre"
    #check that the suggestions are there
    assert container_obj.spelling_corrections[0].suggestions[0].text == "Patients"
    assert container_obj.spelling_corrections[1].suggestions[0].text == "breast cancer"

    #Check the _to_dict() against the original container dictionary
    assert container_obj._to_dict() == container_dict["unstructured"][0]["data"]
