# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from ibm_whcs_sdk.annotator_for_clinical_data.tests.common import test_section
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import pytest
import requests
import responses
import tempfile
from ibm_whcs_sdk.annotator_for_clinical_data import *

VERSION = 'testString'

SERVICE = AnnotatorForClinicalDataV1(
    authenticator=NoAuthAuthenticator(),
    version=VERSION
    )

BASE_URL = 'https://us-south.wh-acd.cloud.ibm.com/wh-acd/api'
SERVICE.set_service_url(BASE_URL)

##############################################################################
# Start of Service: Profiles
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_profiles
#-----------------------------------------------------------------------------
class TestGetProfiles():

    #--------------------------------------------------------
    # get_profiles()
    #--------------------------------------------------------
    @responses.activate
    def test_get_profiles_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.get_profiles()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_profiles_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_profiles_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_profiles(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_profile
#-----------------------------------------------------------------------------
class TestCreateProfile():

    #--------------------------------------------------------
    # create_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_create_profile_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Annotator model
        annotator_model = {}
        annotator_model['name'] = 'testString'
        annotator_model['parameters'] = {}
        annotator_model['configurations'] = [configuration_entity_model]

        # Set up parameter values
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotators = [annotator_model]

        # Invoke method
        response = SERVICE.create_profile(
            new_id=new_id,
            new_name=new_name,
            new_description=new_description,
            new_published_date=new_published_date,
            new_publish=new_publish,
            new_version=new_version,
            new_cartridge_id=new_cartridge_id,
            new_annotators=new_annotators,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['publishedDate'] == 'testString'
        assert req_body['publish'] == True
        assert req_body['version'] == 'testString'
        assert req_body['cartridgeId'] == 'testString'
        assert req_body['annotators'] == [annotator_model]


    #--------------------------------------------------------
    # test_create_profile_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_profile_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Annotator model
        annotator_model = {}
        annotator_model['name'] = 'testString'
        annotator_model['parameters'] = {}
        annotator_model['configurations'] = [configuration_entity_model]

        # Set up parameter values
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotators = [annotator_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.create_profile(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_profile
#-----------------------------------------------------------------------------
class TestGetProfile():

    #--------------------------------------------------------
    # get_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_get_profile_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "publishedDate": "published_date", "publish": false, "version": "version", "cartridgeId": "cartridge_id", "annotators": [{"name": "name", "parameters": {"mapKey": ["inner"]}, "configurations": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.get_profile(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_profile_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_profile_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "publishedDate": "published_date", "publish": false, "version": "version", "cartridgeId": "cartridge_id", "annotators": [{"name": "name", "parameters": {"mapKey": ["inner"]}, "configurations": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_profile(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_profile
#-----------------------------------------------------------------------------
class TestUpdateProfile():

    #--------------------------------------------------------
    # update_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_update_profile_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Annotator model
        annotator_model = {}
        annotator_model['name'] = 'testString'
        annotator_model['parameters'] = {}
        annotator_model['configurations'] = [configuration_entity_model]

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotators = [annotator_model]

        # Invoke method
        response = SERVICE.update_profile(
            id,
            new_id=new_id,
            new_name=new_name,
            new_description=new_description,
            new_published_date=new_published_date,
            new_publish=new_publish,
            new_version=new_version,
            new_cartridge_id=new_cartridge_id,
            new_annotators=new_annotators,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['publishedDate'] == 'testString'
        assert req_body['publish'] == True
        assert req_body['version'] == 'testString'
        assert req_body['cartridgeId'] == 'testString'
        assert req_body['annotators'] == [annotator_model]


    #--------------------------------------------------------
    # test_update_profile_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_profile_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Annotator model
        annotator_model = {}
        annotator_model['name'] = 'testString'
        annotator_model['parameters'] = {}
        annotator_model['configurations'] = [configuration_entity_model]

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotators = [annotator_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.update_profile(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_profile
#-----------------------------------------------------------------------------
class TestDeleteProfile():

    #--------------------------------------------------------
    # delete_profile()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_profile_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.delete_profile(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_profile_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_profile_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/profiles/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.delete_profile(**req_copy)



# endregion
##############################################################################
# End of Service: Profiles
##############################################################################

##############################################################################
# Start of Service: Flows
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_flows
#-----------------------------------------------------------------------------
class TestGetFlows():

    #--------------------------------------------------------
    # get_flows()
    #--------------------------------------------------------
    @responses.activate
    def test_get_flows_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/flows'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.get_flows()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_flows_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_flows_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/flows'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_flows(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_flows
#-----------------------------------------------------------------------------
class TestCreateFlows():

    #--------------------------------------------------------
    # create_flows()
    #--------------------------------------------------------
    @responses.activate
    def test_create_flows_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/flows'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotator_flows = [annotator_flow_model]

        # Invoke method
        response = SERVICE.create_flows(
            new_id=new_id,
            new_name=new_name,
            new_description=new_description,
            new_published_date=new_published_date,
            new_publish=new_publish,
            new_version=new_version,
            new_cartridge_id=new_cartridge_id,
            new_annotator_flows=new_annotator_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['publishedDate'] == 'testString'
        assert req_body['publish'] == True
        assert req_body['version'] == 'testString'
        assert req_body['cartridgeId'] == 'testString'
        assert req_body['annotatorFlows'] == [annotator_flow_model]


    #--------------------------------------------------------
    # test_create_flows_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_flows_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/flows'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotator_flows = [annotator_flow_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.create_flows(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_flows_by_id
#-----------------------------------------------------------------------------
class TestGetFlowsById():

    #--------------------------------------------------------
    # get_flows_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_flows_by_id_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "publishedDate": "published_date", "publish": false, "version": "version", "cartridgeId": "cartridge_id", "annotatorFlows": [{"profile": "profile", "flow": {"elements": [{}], "async": true}, "id": "id", "type": "type", "data": {"mapKey": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}]}, "metadata": {"mapKey": {"anyKey": "anyValue"}}, "globalConfigurations": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}], "uid": 3}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.get_flows_by_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_flows_by_id_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_flows_by_id_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        mock_response = '{"id": "id", "name": "name", "description": "description", "publishedDate": "published_date", "publish": false, "version": "version", "cartridgeId": "cartridge_id", "annotatorFlows": [{"profile": "profile", "flow": {"elements": [{}], "async": true}, "id": "id", "type": "type", "data": {"mapKey": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}]}, "metadata": {"mapKey": {"anyKey": "anyValue"}}, "globalConfigurations": [{"id": "id", "type": "type", "uid": 3, "mergeid": 7}], "uid": 3}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_flows_by_id(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_flows
#-----------------------------------------------------------------------------
class TestUpdateFlows():

    #--------------------------------------------------------
    # update_flows()
    #--------------------------------------------------------
    @responses.activate
    def test_update_flows_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotator_flows = [annotator_flow_model]

        # Invoke method
        response = SERVICE.update_flows(
            id,
            new_id=new_id,
            new_name=new_name,
            new_description=new_description,
            new_published_date=new_published_date,
            new_publish=new_publish,
            new_version=new_version,
            new_cartridge_id=new_cartridge_id,
            new_annotator_flows=new_annotator_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['publishedDate'] == 'testString'
        assert req_body['publish'] == True
        assert req_body['version'] == 'testString'
        assert req_body['cartridgeId'] == 'testString'
        assert req_body['annotatorFlows'] == [annotator_flow_model]


    #--------------------------------------------------------
    # test_update_flows_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_flows_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        id = 'testString'
        new_id = 'testString'
        new_name = 'testString'
        new_description = 'testString'
        new_published_date = 'testString'
        new_publish = True
        new_version = 'testString'
        new_cartridge_id = 'testString'
        new_annotator_flows = [annotator_flow_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.update_flows(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_flows
#-----------------------------------------------------------------------------
class TestDeleteFlows():

    #--------------------------------------------------------
    # delete_flows()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_flows_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.delete_flows(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_flows_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_flows_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/flows/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.delete_flows(**req_copy)



# endregion
##############################################################################
# End of Service: Flows
##############################################################################

##############################################################################
# Start of Service: ACD
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for run_pipeline
#-----------------------------------------------------------------------------
class TestRunPipeline():

    #--------------------------------------------------------
    # run_pipeline()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        unstructured = [unstructured_container_model]
        annotator_flows = [annotator_flow_model]
        debug_text_restore = True
        return_analyzed_text = True

        # Invoke method
        response = SERVICE.run_pipeline(
            unstructured=unstructured,
            annotator_flows=annotator_flows,
            debug_text_restore=debug_text_restore,
            return_analyzed_text=return_analyzed_text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'debug_text_restore={}'.format('true' if debug_text_restore else 'false') in query_string
        assert 'return_analyzed_text={}'.format('true' if return_analyzed_text else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['unstructured'] == [unstructured_container_model]
        assert req_body['annotatorFlows'] == [annotator_flow_model]


    #--------------------------------------------------------
    # test_run_pipeline_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        unstructured = [unstructured_container_model]
        annotator_flows = [annotator_flow_model]

        # Invoke method
        response = SERVICE.run_pipeline(
            unstructured=unstructured,
            annotator_flows=annotator_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['unstructured'] == [unstructured_container_model]
        assert req_body['annotatorFlows'] == [annotator_flow_model]


    #--------------------------------------------------------
    # test_run_pipeline_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Set up parameter values
        unstructured = [unstructured_container_model]
        annotator_flows = [annotator_flow_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.run_pipeline(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for run_pipeline_with_flow
#-----------------------------------------------------------------------------
class TestRunPipelineWithFlow():

    #--------------------------------------------------------
    # run_pipeline_with_flow()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_with_flow_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze/testString'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a AnalyticFlowBeanInput model
        analytic_flow_bean_input_model = {}
        analytic_flow_bean_input_model['unstructured'] = [unstructured_container_model]
        analytic_flow_bean_input_model['annotatorFlows'] = [annotator_flow_model]

        # Set up parameter values
        flow_id = 'testString'
        return_analyzed_text = True
        analytic_flow_bean_input = analytic_flow_bean_input_model
        content_type = 'application/json'
        debug_text_restore = True

        # Invoke method
        response = SERVICE.run_pipeline_with_flow(
            flow_id,
            return_analyzed_text,
            analytic_flow_bean_input,
            content_type=content_type,
            debug_text_restore=debug_text_restore,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'return_analyzed_text={}'.format('true' if return_analyzed_text else 'false') in query_string
        assert 'debug_text_restore={}'.format('true' if debug_text_restore else 'false') in query_string
        # Validate body params


    #--------------------------------------------------------
    # test_run_pipeline_with_flow_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_with_flow_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze/testString'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a AnalyticFlowBeanInput model
        analytic_flow_bean_input_model = {}
        analytic_flow_bean_input_model['unstructured'] = [unstructured_container_model]
        analytic_flow_bean_input_model['annotatorFlows'] = [annotator_flow_model]

        # Set up parameter values
        flow_id = 'testString'
        return_analyzed_text = True
        analytic_flow_bean_input = analytic_flow_bean_input_model

        # Invoke method
        response = SERVICE.run_pipeline_with_flow(
            flow_id,
            return_analyzed_text,
            analytic_flow_bean_input,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'return_analyzed_text={}'.format('true' if return_analyzed_text else 'false') in query_string
        # Validate body params


    #--------------------------------------------------------
    # test_run_pipeline_with_flow_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_run_pipeline_with_flow_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/analyze/testString'
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a FlowEntry model
        flow_entry_model = {}

        # Construct a dict representation of a ConfigurationEntity model
        configuration_entity_model = {}
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a dict representation of a Flow model
        flow_model = {}
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a dict representation of a AnnotatorFlow model
        annotator_flow_model = {}
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Construct a dict representation of a UnstructuredContainer model
        unstructured_container_model = {}
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a dict representation of a AnalyticFlowBeanInput model
        analytic_flow_bean_input_model = {}
        analytic_flow_bean_input_model['unstructured'] = [unstructured_container_model]
        analytic_flow_bean_input_model['annotatorFlows'] = [annotator_flow_model]

        # Set up parameter values
        flow_id = 'testString'
        return_analyzed_text = True
        analytic_flow_bean_input = analytic_flow_bean_input_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "flow_id": flow_id,
            "return_analyzed_text": return_analyzed_text,
            "analytic_flow_bean_input": analytic_flow_bean_input,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.run_pipeline_with_flow(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_annotators
#-----------------------------------------------------------------------------
class TestGetAnnotators():

    #--------------------------------------------------------
    # get_annotators()
    #--------------------------------------------------------
    @responses.activate
    def test_get_annotators_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/annotators'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = SERVICE.get_annotators()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_annotators_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_annotators_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/annotators'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_annotators(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_annotators_by_id
#-----------------------------------------------------------------------------
class TestGetAnnotatorsById():

    #--------------------------------------------------------
    # get_annotators_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_annotators_by_id_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/annotators/testString'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.get_annotators_by_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_annotators_by_id_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_annotators_by_id_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/annotators/testString'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.get_annotators_by_id(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_user_specific_artifacts
#-----------------------------------------------------------------------------
class TestDeleteUserSpecificArtifacts():

    #--------------------------------------------------------
    # delete_user_specific_artifacts()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_specific_artifacts_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/user_data'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Invoke method
        response = SERVICE.delete_user_specific_artifacts()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_user_specific_artifacts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_specific_artifacts_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/user_data'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.delete_user_specific_artifacts(**req_copy)



# endregion
##############################################################################
# End of Service: ACD
##############################################################################

##############################################################################
# Start of Service: Cartridges
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for cartridges_get
#-----------------------------------------------------------------------------
class TestCartridgesGet():

    #--------------------------------------------------------
    # cartridges_get()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_get_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.cartridges_get()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_get_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_get_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"data": ["data"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.cartridges_get(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for cartridges_post_multipart
#-----------------------------------------------------------------------------
class TestCartridgesPostMultipart():

    #--------------------------------------------------------
    # cartridges_post_multipart()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_post_multipart_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        archive_file = io.BytesIO(b'This is a mock file.').getvalue()
        archive_file_content_type = 'testString'

        # Invoke method
        response = SERVICE.cartridges_post_multipart(
            archive_file=archive_file,
            archive_file_content_type=archive_file_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_post_multipart_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_post_multipart_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.cartridges_post_multipart()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_post_multipart_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_post_multipart_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.cartridges_post_multipart(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for cartridges_put_multipart
#-----------------------------------------------------------------------------
class TestCartridgesPutMultipart():

    #--------------------------------------------------------
    # cartridges_put_multipart()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_put_multipart_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        archive_file = io.BytesIO(b'This is a mock file.').getvalue()
        archive_file_content_type = 'testString'

        # Invoke method
        response = SERVICE.cartridges_put_multipart(
            archive_file=archive_file,
            archive_file_content_type=archive_file_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_put_multipart_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_put_multipart_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.cartridges_put_multipart()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_put_multipart_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_put_multipart_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.cartridges_put_multipart(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for cartridges_get_id
#-----------------------------------------------------------------------------
class TestCartridgesGetId():

    #--------------------------------------------------------
    # cartridges_get_id()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_get_id_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges/testString'
        mock_response = '{"id": "id", "name": "name", "status": "status", "statusCode": 11, "statusLocation": "status_location", "startTime": "start_time", "endTime": "end_time", "duration": "duration", "correlationId": "correlation_id", "artifactResponseCode": 22, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = SERVICE.cartridges_get_id(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_cartridges_get_id_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_cartridges_get_id_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/cartridges/testString'
        mock_response = '{"id": "id", "name": "name", "status": "status", "statusCode": 11, "statusLocation": "status_location", "startTime": "start_time", "endTime": "end_time", "duration": "duration", "correlationId": "correlation_id", "artifactResponseCode": 22, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.cartridges_get_id(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for deploy_cartridge
#-----------------------------------------------------------------------------
class TestDeployCartridge():

    #--------------------------------------------------------
    # deploy_cartridge()
    #--------------------------------------------------------
    @responses.activate
    def test_deploy_cartridge_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/deploy'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        archive_file = io.BytesIO(b'This is a mock file.').getvalue()
        archive_file_content_type = 'testString'
        update = True

        # Invoke method
        response = SERVICE.deploy_cartridge(
            archive_file=archive_file,
            archive_file_content_type=archive_file_content_type,
            update=update,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'update={}'.format('true' if update else 'false') in query_string


    #--------------------------------------------------------
    # test_deploy_cartridge_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_deploy_cartridge_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/deploy'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.deploy_cartridge()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_deploy_cartridge_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_deploy_cartridge_value_error(self):
        # Set up mock
        url = BASE_URL + '/v1/deploy'
        mock_response = '{"code": 4, "artifactResponse": [{"code": 4, "message": "message", "level": "ERROR", "description": "description", "moreInfo": "more_info", "correlationId": "correlation_id", "artifact": "artifact", "href": "href"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                SERVICE.deploy_cartridge(**req_copy)



# endregion
##############################################################################
# End of Service: Cartridges
##############################################################################

##############################################################################
# Start of Service: Status
##############################################################################
# region


#-----------------------------------------------------------------------------
# Test Class for get_health_check_status
#-----------------------------------------------------------------------------
class TestGetHealthCheckStatus():

    #--------------------------------------------------------
    # get_health_check_status()
    #--------------------------------------------------------
    @responses.activate
    def test_get_health_check_status_all_params(self):
        # Set up mock
        url = BASE_URL + '/v1/status/health_check'
        mock_response = '{"version": "version", "upTime": "up_time", "serviceState": "OK", "stateDetails": "state_details", "hostName": "host_name", "requestCount": 13, "maxMemoryMb": 13, "commitedMemoryMb": 18, "inUseMemoryMb": 16, "availableProcessors": 20, "concurrentRequests": 19, "maxConcurrentRequests": 23, "totalRejectedRequests": 23, "totalBlockedRequests": 22}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accept = 'application/json'
        format = 'json'

        # Invoke method
        response = SERVICE.get_health_check_status(
            accept=accept,
            format=format,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'format={}'.format(format) in query_string


    #--------------------------------------------------------
    # test_get_health_check_status_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_health_check_status_required_params(self):
        # Set up mock
        url = BASE_URL + '/v1/status/health_check'
        mock_response = '{"version": "version", "upTime": "up_time", "serviceState": "OK", "stateDetails": "state_details", "hostName": "host_name", "requestCount": 13, "maxMemoryMb": 13, "commitedMemoryMb": 18, "inUseMemoryMb": 16, "availableProcessors": 20, "concurrentRequests": 19, "maxConcurrentRequests": 23, "totalRejectedRequests": 23, "totalBlockedRequests": 22}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = SERVICE.get_health_check_status()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Status
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for AcdCartridges
#-----------------------------------------------------------------------------
class TestAcdCartridges():

    #--------------------------------------------------------
    # Test serialization/deserialization for AcdCartridges
    #--------------------------------------------------------
    def test_acd_cartridges_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        service_error_model = {} # ServiceError
        service_error_model['code'] = 38
        service_error_model['message'] = 'testString'
        service_error_model['level'] = 'ERROR'
        service_error_model['description'] = 'testString'
        service_error_model['moreInfo'] = 'testString'
        service_error_model['correlationId'] = 'testString'
        service_error_model['artifact'] = 'testString'
        service_error_model['href'] = 'testString'

        # Construct a json representation of a AcdCartridges model
        acd_cartridges_model_json = {}
        acd_cartridges_model_json['id'] = 'testString'
        acd_cartridges_model_json['name'] = 'testString'
        acd_cartridges_model_json['status'] = 'testString'
        acd_cartridges_model_json['statusCode'] = 38
        acd_cartridges_model_json['statusLocation'] = 'testString'
        acd_cartridges_model_json['startTime'] = 'testString'
        acd_cartridges_model_json['endTime'] = 'testString'
        acd_cartridges_model_json['duration'] = 'testString'
        acd_cartridges_model_json['correlationId'] = 'testString'
        acd_cartridges_model_json['artifactResponseCode'] = 38
        acd_cartridges_model_json['artifactResponse'] = [service_error_model]

        # Construct a model instance of AcdCartridges by calling from_dict on the json representation
        acd_cartridges_model = AcdCartridges.from_dict(acd_cartridges_model_json)
        assert acd_cartridges_model != False

        # Construct a model instance of AcdCartridges by calling from_dict on the json representation
        acd_cartridges_model_dict = AcdCartridges.from_dict(acd_cartridges_model_json).__dict__
        acd_cartridges_model2 = AcdCartridges(**acd_cartridges_model_dict)

        # Verify the model instances are equivalent
        assert acd_cartridges_model == acd_cartridges_model2

        # Convert model instance back to dict and verify no loss of data
        acd_cartridges_model_json2 = acd_cartridges_model.to_dict()
        assert acd_cartridges_model_json2 == acd_cartridges_model_json

#-----------------------------------------------------------------------------
# Test Class for AcdFlow
#-----------------------------------------------------------------------------
class TestAcdFlow():

    #--------------------------------------------------------
    # Test serialization/deserialization for AcdFlow
    #--------------------------------------------------------
    def test_acd_flow_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        flow_entry_model = {} # FlowEntry

        configuration_entity_model = {} # ConfigurationEntity
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        flow_model = {} # Flow
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        annotator_flow_model = {} # AnnotatorFlow
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
#        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        # Construct a json representation of a AcdFlow model
        acd_flow_model_json = {}
        acd_flow_model_json['id'] = 'testString'
        acd_flow_model_json['name'] = 'testString'
        acd_flow_model_json['description'] = 'testString'
        acd_flow_model_json['publishedDate'] = 'testString'
        acd_flow_model_json['publish'] = True
        acd_flow_model_json['version'] = 'testString'
        acd_flow_model_json['cartridgeId'] = 'testString'
        acd_flow_model_json['annotatorFlows'] = [annotator_flow_model]

        # Construct a model instance of AcdFlow by calling from_dict on the json representation
        acd_flow_model = AcdFlow.from_dict(acd_flow_model_json)
        assert acd_flow_model != False

        # Construct a model instance of AcdFlow by calling from_dict on the json representation
        acd_flow_model_dict = AcdFlow.from_dict(acd_flow_model_json).__dict__
        acd_flow_model2 = AcdFlow(**acd_flow_model_dict)

        # Verify the model instances are equivalent
        assert acd_flow_model == acd_flow_model2

        # Convert model instance back to dict and verify no loss of data
        acd_flow_model_json2 = acd_flow_model.to_dict()
        assert acd_flow_model_json2 == acd_flow_model_json

#-----------------------------------------------------------------------------
# Test Class for AcdProfile
#-----------------------------------------------------------------------------
class TestAcdProfile():

    #--------------------------------------------------------
    # Test serialization/deserialization for AcdProfile
    #--------------------------------------------------------
    def test_acd_profile_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        configuration_entity_model = {} # ConfigurationEntity
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        annotator_model = {} # Annotator
        annotator_model['name'] = 'testString'
        annotator_model['parameters'] = {}
#        annotator_model['configurations'] = [configuration_entity_model]

        # Construct a json representation of a AcdProfile model
        acd_profile_model_json = {}
        acd_profile_model_json['id'] = 'testString'
        acd_profile_model_json['name'] = 'testString'
        acd_profile_model_json['description'] = 'testString'
        acd_profile_model_json['publishedDate'] = 'testString'
        acd_profile_model_json['publish'] = True
        acd_profile_model_json['version'] = 'testString'
        acd_profile_model_json['cartridgeId'] = 'testString'
        acd_profile_model_json['annotators'] = [annotator_model]

        # Construct a model instance of AcdProfile by calling from_dict on the json representation
        acd_profile_model = AcdProfile.from_dict(acd_profile_model_json)
        assert acd_profile_model != False

        # Construct a model instance of AcdProfile by calling from_dict on the json representation
        acd_profile_model_dict = AcdProfile.from_dict(acd_profile_model_json).__dict__
        acd_profile_model2 = AcdProfile(**acd_profile_model_dict)

        # Verify the model instances are equivalent
        assert acd_profile_model == acd_profile_model2

        # Convert model instance back to dict and verify no loss of data
        acd_profile_model_json2 = acd_profile_model.to_dict()
        assert acd_profile_model_json2 == acd_profile_model_json

#-----------------------------------------------------------------------------
# Test Class for AnalyticFlowBeanInput
#-----------------------------------------------------------------------------
class TestAnalyticFlowBeanInput():

    #--------------------------------------------------------
    # Test serialization/deserialization for AnalyticFlowBeanInput
    #--------------------------------------------------------
    def test_analytic_flow_bean_input_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        flow_entry_model = {} # FlowEntry

        configuration_entity_model = {} # ConfigurationEntity
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        flow_model = {} # Flow
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        annotator_flow_model = {} # AnnotatorFlow
        annotator_flow_model['profile'] = 'testString'
        annotator_flow_model['flow'] = flow_model
        annotator_flow_model['id'] = 'testString'
        annotator_flow_model['type'] = 'testString'
        annotator_flow_model['data'] = {}
        annotator_flow_model['metadata'] = {}
#        annotator_flow_model['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model['uid'] = 26

        unstructured_container_model = {} # UnstructuredContainer
        unstructured_container_model['text'] = 'testString'
        unstructured_container_model['id'] = 'testString'
        unstructured_container_model['type'] = 'testString'
        unstructured_container_model['data'] = {}
        unstructured_container_model['metadata'] = {}
        unstructured_container_model['uid'] = 26

        # Construct a json representation of a AnalyticFlowBeanInput model
        analytic_flow_bean_input_model_json = {}
        analytic_flow_bean_input_model_json['unstructured'] = [unstructured_container_model]
        analytic_flow_bean_input_model_json['annotatorFlows'] = [annotator_flow_model]

        # Construct a model instance of AnalyticFlowBeanInput by calling from_dict on the json representation
        analytic_flow_bean_input_model = AnalyticFlowBeanInput.from_dict(analytic_flow_bean_input_model_json)
        assert analytic_flow_bean_input_model != False

        # Construct a model instance of AnalyticFlowBeanInput by calling from_dict on the json representation
        analytic_flow_bean_input_model_dict = AnalyticFlowBeanInput.from_dict(analytic_flow_bean_input_model_json).__dict__
        analytic_flow_bean_input_model2 = AnalyticFlowBeanInput(**analytic_flow_bean_input_model_dict)

        # Verify the model instances are equivalent
#        assert analytic_flow_bean_input_model == analytic_flow_bean_input_model2

        # Convert model instance back to dict and verify no loss of data
        analytic_flow_bean_input_model_json2 = analytic_flow_bean_input_model.to_dict()
        assert analytic_flow_bean_input_model_json2 == analytic_flow_bean_input_model_json

#-----------------------------------------------------------------------------
# Test Class for Annotator
#-----------------------------------------------------------------------------
class TestAnnotator():

    #--------------------------------------------------------
    # Test serialization/deserialization for Annotator
    #--------------------------------------------------------
    def test_annotator_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        configuration_entity_model = {} # ConfigurationEntity
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        # Construct a json representation of a Annotator model
        annotator_model_json = {}
        annotator_model_json['name'] = 'testString'
        annotator_model_json['parameters'] = {}
#        annotator_model_json['configurations'] = [configuration_entity_model]

        # Construct a model instance of Annotator by calling from_dict on the json representation
        annotator_model = Annotator.from_dict(annotator_model_json)
        assert annotator_model != False

        # Construct a model instance of Annotator by calling from_dict on the json representation
        annotator_model_dict = Annotator.from_dict(annotator_model_json).__dict__
        annotator_model2 = Annotator(**annotator_model_dict)

        # Verify the model instances are equivalent
        assert annotator_model == annotator_model2

        # Convert model instance back to dict and verify no loss of data
        annotator_model_json2 = annotator_model.to_dict()
        assert annotator_model_json2 == annotator_model_json

#-----------------------------------------------------------------------------
# Test Class for AnnotatorFlow
#-----------------------------------------------------------------------------
class TestAnnotatorFlow():

    #--------------------------------------------------------
    # Test serialization/deserialization for AnnotatorFlow
    #--------------------------------------------------------
    def test_annotator_flow_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        flow_entry_model = {} # FlowEntry

        configuration_entity_model = {} # ConfigurationEntity
        configuration_entity_model['id'] = 'testString'
        configuration_entity_model['type'] = 'testString'
        configuration_entity_model['uid'] = 26
        configuration_entity_model['mergeid'] = 26

        flow_model = {} # Flow
        flow_model['elements'] = [flow_entry_model]
        flow_model['async'] = True

        # Construct a json representation of a AnnotatorFlow model
        annotator_flow_model_json = {}
        annotator_flow_model_json['profile'] = 'testString'
        annotator_flow_model_json['flow'] = flow_model
        annotator_flow_model_json['id'] = 'testString'
        annotator_flow_model_json['type'] = 'testString'
        annotator_flow_model_json['data'] = {}
        annotator_flow_model_json['metadata'] = {}
#        annotator_flow_model_json['globalConfigurations'] = [configuration_entity_model]
        annotator_flow_model_json['uid'] = 26

        # Construct a model instance of AnnotatorFlow by calling from_dict on the json representation
        annotator_flow_model = AnnotatorFlow.from_dict(annotator_flow_model_json)
        assert annotator_flow_model != False

        # Construct a model instance of AnnotatorFlow by calling from_dict on the json representation
        annotator_flow_model_dict = AnnotatorFlow.from_dict(annotator_flow_model_json).__dict__
        annotator_flow_model2 = AnnotatorFlow(**annotator_flow_model_dict)

        # Verify the model instances are equivalent
        assert annotator_flow_model == annotator_flow_model2

        # Convert model instance back to dict and verify no loss of data
        annotator_flow_model_json2 = annotator_flow_model.to_dict()
        assert annotator_flow_model_json2 == annotator_flow_model_json

#-----------------------------------------------------------------------------
# Test Class for ConfigurationEntity
#-----------------------------------------------------------------------------
#class TestConfigurationEntity():

    #--------------------------------------------------------
    # Test serialization/deserialization for ConfigurationEntity
    #--------------------------------------------------------
#    def test_configuration_entity_serialization(self):

        # Construct a json representation of a ConfigurationEntity model
#        configuration_entity_model_json = {}
#        configuration_entity_model_json['id'] = 'testString'
#        configuration_entity_model_json['type'] = 'testString'
#        configuration_entity_model_json['uid'] = 26
#        configuration_entity_model_json['mergeid'] = 26

        # Construct a model instance of ConfigurationEntity by calling from_dict on the json representation
#        configuration_entity_model = ConfigurationEntity.from_dict(configuration_entity_model_json)
#        assert configuration_entity_model != False

        # Construct a model instance of ConfigurationEntity by calling from_dict on the json representation
#        configuration_entity_model_dict = ConfigurationEntity.from_dict(configuration_entity_model_json).__dict__
#        configuration_entity_model2 = ConfigurationEntity(**configuration_entity_model_dict)

        # Verify the model instances are equivalent
#        assert configuration_entity_model == configuration_entity_model2

        # Convert model instance back to dict and verify no loss of data
#        configuration_entity_model_json2 = configuration_entity_model.to_dict()
#        assert configuration_entity_model_json2 == configuration_entity_model_json

#-----------------------------------------------------------------------------
# Test Class for DeployCartridgeResponse
#-----------------------------------------------------------------------------
class TestDeployCartridgeResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeployCartridgeResponse
    #--------------------------------------------------------
    def test_deploy_cartridge_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        service_error_model = {} # ServiceError
        service_error_model['code'] = 38
        service_error_model['message'] = 'testString'
        service_error_model['level'] = 'ERROR'
        service_error_model['description'] = 'testString'
        service_error_model['moreInfo'] = 'testString'
        service_error_model['correlationId'] = 'testString'
        service_error_model['artifact'] = 'testString'
        service_error_model['href'] = 'testString'

        # Construct a json representation of a DeployCartridgeResponse model
        deploy_cartridge_response_model_json = {}
        deploy_cartridge_response_model_json['code'] = 38
        deploy_cartridge_response_model_json['artifactResponse'] = [service_error_model]

        # Construct a model instance of DeployCartridgeResponse by calling from_dict on the json representation
        deploy_cartridge_response_model = DeployCartridgeResponse.from_dict(deploy_cartridge_response_model_json)
        assert deploy_cartridge_response_model != False

        # Construct a model instance of DeployCartridgeResponse by calling from_dict on the json representation
        deploy_cartridge_response_model_dict = DeployCartridgeResponse.from_dict(deploy_cartridge_response_model_json).__dict__
        deploy_cartridge_response_model2 = DeployCartridgeResponse(**deploy_cartridge_response_model_dict)

        # Verify the model instances are equivalent
        assert deploy_cartridge_response_model == deploy_cartridge_response_model2

        # Convert model instance back to dict and verify no loss of data
        deploy_cartridge_response_model_json2 = deploy_cartridge_response_model.to_dict()
        assert deploy_cartridge_response_model_json2 == deploy_cartridge_response_model_json

#-----------------------------------------------------------------------------
# Test Class for Entity
#-----------------------------------------------------------------------------
class TestEntity():

    #--------------------------------------------------------
    # Test serialization/deserialization for Entity
    #--------------------------------------------------------
    def test_entity_serialization(self):

        # Construct a json representation of a Entity model
        entity_model_json = {}
        entity_model_json['id'] = 'testString'
        entity_model_json['type'] = 'testString'
        entity_model_json['uid'] = 26
        entity_model_json['mergeid'] = 26

        # Construct a model instance of Entity by calling from_dict on the json representation
        entity_model = Entity.from_dict(entity_model_json)
        assert entity_model != False

        # Construct a model instance of Entity by calling from_dict on the json representation
        entity_model_dict = Entity.from_dict(entity_model_json).__dict__
        entity_model2 = Entity(**entity_model_dict)

        # Verify the model instances are equivalent
        assert entity_model == entity_model2

        # Convert model instance back to dict and verify no loss of data
        entity_model_json2 = entity_model.to_dict()
        assert entity_model_json2 == entity_model_json

#-----------------------------------------------------------------------------
# Test Class for Flow
#-----------------------------------------------------------------------------
class TestFlow():

    #--------------------------------------------------------
    # Test serialization/deserialization for Flow
    #--------------------------------------------------------
    def test_flow_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        flow_entry_model = {} # FlowEntry

        # Construct a json representation of a Flow model
        flow_model_json = {}
        flow_model_json['elements'] = [flow_entry_model]
        flow_model_json['async'] = True

        # Construct a model instance of Flow by calling from_dict on the json representation
        flow_model = Flow.from_dict(flow_model_json)
        assert flow_model != False

        # Construct a model instance of Flow by calling from_dict on the json representation
        flow_model_dict = Flow.from_dict(flow_model_json).__dict__
        flow_model2 = Flow(**flow_model_dict)

        # Verify the model instances are equivalent
        assert flow_model == flow_model2

        # Convert model instance back to dict and verify no loss of data
        flow_model_json2 = flow_model.to_dict()
        assert flow_model_json2 == flow_model_json

#-----------------------------------------------------------------------------
# Test Class for FlowEntry
#-----------------------------------------------------------------------------
class TestFlowEntry():

    #--------------------------------------------------------
    # Test serialization/deserialization for FlowEntry
    #--------------------------------------------------------
    def test_flow_entry_serialization(self):

        # Construct a json representation of a FlowEntry model
        flow_entry_model_json = {}

        # Construct a model instance of FlowEntry by calling from_dict on the json representation
        flow_entry_model = FlowEntry.from_dict(flow_entry_model_json)
        assert flow_entry_model != False

        # Construct a model instance of FlowEntry by calling from_dict on the json representation
        flow_entry_model_dict = FlowEntry.from_dict(flow_entry_model_json).__dict__
        flow_entry_model2 = FlowEntry(**flow_entry_model_dict)

        # Verify the model instances are equivalent
        assert flow_entry_model == flow_entry_model2

        # Convert model instance back to dict and verify no loss of data
        flow_entry_model_json2 = flow_entry_model.to_dict()
        assert flow_entry_model_json2 == flow_entry_model_json

#-----------------------------------------------------------------------------
# Test Class for ListStringWrapper
#-----------------------------------------------------------------------------
class TestListStringWrapper():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListStringWrapper
    #--------------------------------------------------------
    def test_list_string_wrapper_serialization(self):

        # Construct a json representation of a ListStringWrapper model
        list_string_wrapper_model_json = {}
        list_string_wrapper_model_json['data'] = ['testString']

        # Construct a model instance of ListStringWrapper by calling from_dict on the json representation
        list_string_wrapper_model = ListStringWrapper.from_dict(list_string_wrapper_model_json)
        assert list_string_wrapper_model != False

        # Construct a model instance of ListStringWrapper by calling from_dict on the json representation
        list_string_wrapper_model_dict = ListStringWrapper.from_dict(list_string_wrapper_model_json).__dict__
        list_string_wrapper_model2 = ListStringWrapper(**list_string_wrapper_model_dict)

        # Verify the model instances are equivalent
        assert list_string_wrapper_model == list_string_wrapper_model2

        # Convert model instance back to dict and verify no loss of data
        list_string_wrapper_model_json2 = list_string_wrapper_model.to_dict()
        assert list_string_wrapper_model_json2 == list_string_wrapper_model_json

#-----------------------------------------------------------------------------
# Test Class for UnstructuredContainer
#-----------------------------------------------------------------------------
class TestUnstructuredContainer():

    #--------------------------------------------------------
    # Test serialization/deserialization for UnstructuredContainer
    #--------------------------------------------------------
    def test_unstructured_container_serialization(self):

        # Construct a json representation of a UnstructuredContainer model
        unstructured_container_model_json = {}
        unstructured_container_model_json['text'] = 'testString'
        unstructured_container_model_json['id'] = 'testString'
        unstructured_container_model_json['type'] = 'testString'
        unstructured_container_model_json['data'] = {}
        unstructured_container_model_json['metadata'] = {}
        unstructured_container_model_json['uid'] = 26

        # Construct a model instance of UnstructuredContainer by calling from_dict on the json representation
        unstructured_container_model = UnstructuredContainer.from_dict(unstructured_container_model_json)
        assert unstructured_container_model != False

        # Construct a model instance of UnstructuredContainer by calling from_dict on the json representation
        unstructured_container_model_dict = UnstructuredContainer.from_dict(unstructured_container_model_json).__dict__
        unstructured_container_model2 = UnstructuredContainer(**unstructured_container_model_dict)

        # Verify the model instances are equivalent
#        assert unstructured_container_model == unstructured_container_model2

        # Convert model instance back to dict and verify no loss of data
        unstructured_container_model_json2 = unstructured_container_model.to_dict()
#        assert unstructured_container_model_json2 == unstructured_container_model_json

#-----------------------------------------------------------------------------
# Test Class for Section
#-----------------------------------------------------------------------------
class TestSection():
    def test_section_validation(self):
        # Construct a basic Annotation and make sure it passes sanity test
        annotation_model = Section(begin=0, end=1, type='testType')
        test_section.TestSectionAnnotation.test_section_annotation(annotation_list=[annotation_model])

#-----------------------------------------------------------------------------
# Test Class for ServiceError
#-----------------------------------------------------------------------------
class TestServiceError():

    #--------------------------------------------------------
    # Test serialization/deserialization for ServiceError
    #--------------------------------------------------------
    def test_service_error_serialization(self):

        # Construct a json representation of a ServiceError model
        service_error_model_json = {}
        service_error_model_json['code'] = 38
        service_error_model_json['message'] = 'testString'
        service_error_model_json['level'] = 'ERROR'
        service_error_model_json['description'] = 'testString'
        service_error_model_json['moreInfo'] = 'testString'
        service_error_model_json['correlationId'] = 'testString'
        service_error_model_json['artifact'] = 'testString'
        service_error_model_json['href'] = 'testString'

        # Construct a model instance of ServiceError by calling from_dict on the json representation
        service_error_model = ServiceError.from_dict(service_error_model_json)
        assert service_error_model != False

        # Construct a model instance of ServiceError by calling from_dict on the json representation
        service_error_model_dict = ServiceError.from_dict(service_error_model_json).__dict__
        service_error_model2 = ServiceError(**service_error_model_dict)

        # Verify the model instances are equivalent
        assert service_error_model == service_error_model2

        # Convert model instance back to dict and verify no loss of data
        service_error_model_json2 = service_error_model.to_dict()
        assert service_error_model_json2 == service_error_model_json

#-----------------------------------------------------------------------------
# Test Class for ServiceStatus
#-----------------------------------------------------------------------------
class TestServiceStatus():

    #--------------------------------------------------------
    # Test serialization/deserialization for ServiceStatus
    #--------------------------------------------------------
    def test_service_status_serialization(self):

        # Construct a json representation of a ServiceStatus model
        service_status_model_json = {}
        service_status_model_json['serviceState'] = 'OK'
        service_status_model_json['stateDetails'] = 'testString'

        # Construct a model instance of ServiceStatus by calling from_dict on the json representation
        service_status_model = ServiceStatus.from_dict(service_status_model_json)
        assert service_status_model != False

        # Construct a model instance of ServiceStatus by calling from_dict on the json representation
        service_status_model_dict = ServiceStatus.from_dict(service_status_model_json).__dict__
        service_status_model2 = ServiceStatus(**service_status_model_dict)

        # Verify the model instances are equivalent
        assert service_status_model == service_status_model2

        # Convert model instance back to dict and verify no loss of data
        service_status_model_json2 = service_status_model.to_dict()
        assert service_status_model_json2 == service_status_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
