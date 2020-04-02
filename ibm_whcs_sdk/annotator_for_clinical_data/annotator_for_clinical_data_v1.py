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

"""
Natural Language Processing (NLP) service featuring a set of medical domain annotators for use in deriving entities
and medical concepts from unstructured data. Multiple annotators may be invoked from a single request.
"""

import json
import logging
import urllib3
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import NoAuthAuthenticator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
from ibm_whcs_sdk.common import get_sdk_headers
urllib3.disable_warnings()

SERVICE_NAME = 'AnnotatorForClinicalData'
LOGGER = logging.getLogger(SERVICE_NAME)

##############################################################################
# Exception Handling
##############################################################################
class ACDException(Exception):
    """
    Custom exception class for errors returned from ACD APIs.

    :param int code: The HTTP status code returned.
    :param str message: A message describing the error.
    :param str correlationId: A code to associate to the ACD error
    """

    def __init__(self, code, message=None, correlation_id=None):
        self.message = message
        self.code = code
        self.correlation_id = correlation_id

    def __str__(self):
        msg = ('Error: ' + str(self.message) + ', Code: ' + str(self.code)
               + ', CorrelationId: ' + str(self.correlation_id))
        LOGGER.error(msg)
        return msg

##############################################################################
# ACD Client
##############################################################################
class AnnotatorForClinicalDataV1(BaseService):
    """
    Client for the Annotator for Clinical Data service.
    """

    default_url = ''
    latest_version = '2018-05-01'

    def __init__(self,
                 url=default_url,
                 iam_apikey=None,
                 iam_url=None,
                 version=latest_version,
                 logging_level=None,
                 disable_ssl_verification=False):
        """
        Construct a new client for the Annotator for Clinical Data service.

        :param str version: The API version date to use with the service, in
               "YYYY-MM-DD" format.
               The service uses the API version for the date you specify, or
               the most recent version before that date. Note that you should
               not programmatically specify the current date at runtime, in
               case the API has been updated since your application's release.
               Instead, specify a version date that is compatible with your
               application, and don't change it until your application is
               ready for a later version.

        :param str url: The base url to use when contacting the service (e.g.
               "https://us-south.wh-acd.cloud.ibm.com/wh-acd/api/").
        :param str iam_apikey: IAM key for service instance
        :param str iam_url: URL for IAM instance authentication.
        :param str logging_level: (optional)  Level of service API logging.  By default
                all error messages are logged.  Valid values are CRITICAL, ERROR, WARNING,
                INFO, DEBUG, and NOTSET
        :param bool disable_ssl_verification: (optional) Determines whethher SSL verification
                should be performed during service calls.  Default is False.  Setting to 
                True is not recommend for production environments.
        """

        if logging_level is not None:
            LOGGING_LEVEL = logging_level
        else:
            LOGGING_LEVEL = logging.ERROR
        logging.basicConfig(filename='acd_sdk.log', level=LOGGING_LEVEL, format='%(asctime)s %(message)s')

        if iam_apikey is None or len(iam_apikey) == 0:
            auth = NoAuthAuthenticator()
            disable_ssl_verification = True
        else:
            if iam_url is None or len(iam_url) == 0:
                LOGGER.debug('SSL disabled : ' + str(disable_ssl_verification))
                auth = IAMAuthenticator(iam_apikey, disable_ssl_verification=disable_ssl_verification)
            else:
                LOGGER.debug('Custom IAM service being used : ' + iam_url)
                LOGGER.debug('SSL disabled : ' + str(disable_ssl_verification))
                auth = IAMAuthenticator(apikey=iam_apikey, url=iam_url, disable_ssl_verification=disable_ssl_verification)

        if not url.endswith('/'):
            url = url + '/'

        super(AnnotatorForClinicalDataV1, self).__init__(
            service_url=url,
            authenticator=auth,
            disable_ssl_verification=disable_ssl_verification
        )

        self.version = version
        self.url = url

    #########################
    # Request ACD
    #########################

    def request_acd(self, request=None):
        """
        Build the request in preparation for invoking ACD.
        """

        try:
            response = self.send(request)
            if 200 <= response.status_code <= 299:
                return response
        except ApiException as api_except:
            final = api_except._get_error_message
            if api_except.message is not None:
                error_message = api_except.message
            else:
                error_message = "No error message available"
            if api_except.code is not None:
                status_code = api_except.code
            if api_except.global_transaction_id is not None:
                correlation_id = api_except.global_transaction_id
            else:
                correlation_id = "None"
            raise ACDException(status_code, error_message, correlation_id)

        return final

    # Name modified manually from analyze to analyze_org
    def analyze_org(self, unstructured=None, annotator_flows=None, **kwargs):
        """
        Detect entities & relations from unstructured data and return as 'dict'.

        <p>This API accepts a JSON request model featuring both the unstructured data to be analyzed as well as
        the desired annotator flow.<p/><p><b>Annotator Chaining</b><br/>Sample request invoking both the
        concept_detection and symptom_disease annotators asynchronously.</p><pre>{<br/>  \"annotatorFlows\":
        [<br/>    {<br/>      \"flow\": {<br/>        \"elements\": [<br/>          {<br/>
        \"annotator\": {<br/>              \"name\": \"concept_detection\"<br/>            }<br/>          },
        <br/>          {<br/>            \"annotator\": {<br/>              \"name\": \"symptom_disease\"<br/>
                    }<br/>          }<br/>        ],<br/>        \"async\": true<br/>      }<br/>    }<br/>  ],
                    <br/>  \"unstructured\": [<br/>    {<br/>      \"text\": \"Patient has lung cancer,
                    but did not smoke. She may consider chemotherapy as part of a treatment plan.\"<br/>    }
                    <br/>  ]<br/>}<br/></pre><p><b>Annotation Filtering</b><br/>
                    Sample request invoking concept_detection with a filter defined to exclude any annotations
                    derived from concept_detection where the semanticType field does not equal \"neop\".
                    </p><pre>{<br/>  \"annotatorFlows\": [<br/>    {<br/>      \"flow\": {<br/>
                    \"elements\": [<br/>          {<br/>            \"annotator\": {<br/>
                    \"name\": \"concept_detection\",<br/>              \"configurations\": [<br/>
                    {<br/>                  \"filter\": {<br/>
                    \"target\": \"unstructured.data.concepts\",<br/>                     \"condition\": {<br/>
                    \"type\": \"match\",<br/>  \"field\": \"semanticType\",<br/>
                    \"values\": [<br/>                           \"neop\"<br/>                         ],
                    <br/>                        \"not\": false,<br/>
                    \"caseInsensitive\": false,<br/>                        \"operator\": \"equals\"
                    <br/>                     }<br/>                  }<br/>                }<br/>
                    ]<br/>            }<br/>          }<br/>        ],<br/>       \"async\": false<br/>
                    }<br/>    }<br/>  ],<br/>  \"unstructured\": [<br/>    {<br/>
                    \"text\": \"Patient has lung cancer, but did not smoke. She may consider chemotherapy as
                    part of a treatment plan.\"<br/>    }<br/>  ]<br/>}<br/></pre><p><b>Annotators that support
                    annotation filtering:</b> allergy, bathing_assistance, cancer, concept_detection,
                    dressing_assistance, eating_assistance, ejection_fraction, lab_value, medication, named_entities,
                    procedure, seeing_assistance, smoking, symptom_disease, toileting_assistance, walking_assistance.
                    </p><hr/><p><b>Annotation Augmentation</b><br/>Sample request invoking the cancer annotator and
                    providing a whitelist entry for a new custom surface form: \"lungcancer\".</p><pre>{<br/>
                    \"annotatorFlows\": [<br/>    {<br/>     \"flow\": {<br/>       \"elements\": [<br/>
                    {<br/>           \"annotator\": {<br/>             \"name\": \"cancer\",<br/>
                    \"configurations\": [<br/>                {<br/>                 \"whitelist\": {<br/>
                    \"name\": \"cancer\",<br/>                   \"entries\": [<br/>
                    {<br/>                  \"surfaceForms\": [<br/>                   \"lungcancer\"<br/>
                    ],<br/>               \"features\": {<br/>                   \"normalizedName\":
                    \"lung cancer\",<br/>                   \"hccCode\": \"9\",<br/>
                    \"icd10Code\": \"C34.9\",<br/>                   \"ccsCode\": \"19\",<br/>
                    \"icd9Code\": \"162.9\",<br/>                   \"conceptId\": \"93880001\"<br/>
                    }<br/>                      }<br/>                    ]<br/>                  }<br/>
                    }<br/>              ]<br/>            }<br/>          }<br/>        ],<br/>
                    \"async\": false<br/>      }<br/>    }<br/>  ],<br/> \"unstructured\": [<br/>    {<br/>
                    \"text\": \"The patient was diagnosed with lungcancer, on Dec 23, 2011.\"<br/>    }<br/>
                    ]<br/>}<br/></pre><b>Annotators that support annotation augmentation:</b> allergy,
                    bathing_assistance, cancer, dressing_assistance, eating_assistance, ejection_fraction,
                    lab_value, medication, named_entities, procedure, seeing_assistance, smoking, symptom_disease,
                    toileting_assistance, walking_assistance.<br/>.

        :param list[UnstructuredContainer] unstructured:
        :param list[AnnotatorFlow] annotator_flows:
        :return: A `DetailedResponse` containing the result, headers and HTTP status code
        :rtype: DetailedResponse
        """
        if unstructured is not None:
            unstructured = [x._to_dict() if hasattr(x, "_to_dict") else x for x in unstructured]
        if annotator_flows is not None:
            annotator_flows = [x._to_dict() if hasattr(x, "_to_dict") else x for x in annotator_flows]

        headers = {'content-type': 'application/json'}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='analyze_org')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        data = {
            'unstructured': unstructured,
            'annotatorFlows': annotator_flows
        }
        url = 'v1/analyze'
        data = json.dumps(data)
        request = self.prepare_request(method='POST', url=url, headers=headers, params=params, data=data)
        response = self.request_acd(request)

        return response

    # Manually added method.
    def analyze(self, text, flow, **kwargs):
        """
        Detect entities & relations from unstructured data and return as 'ContainerGroup'.

        :param str or list[str] text: Text to be analyzed.
        :param Flow flow: The annotator flow definition.
        :return: A 'ContainerGroup' object
        :rtype: watson_health_cognitive_services.annotator_for_clinical_data_v1.ContainerAnnotation for single text
                or watson_health_cognitive_services.annotator_for_clincial_data_v1.ContainerGroup for test array
        """

        annotator_flow = AnnotatorFlow(flow=flow)
        list_annotator_flow = [annotator_flow]
        list_unstructure_container = []
        if isinstance(text, list):
            for item in text:
                unstructured_container = UnstructuredContainer(text=item)
                list_unstructure_container.append(unstructured_container)
            result = (ContainerGroup._from_dict(self.analyze_org(list_unstructure_container,
                                                                 list_annotator_flow, **kwargs).get_result()))
        else:
            unstructured_container = UnstructuredContainer(text=text)
            list_unstructure_container = [unstructured_container]
            result = (ContainerGroup._from_dict(self.analyze_org(list_unstructure_container,
                                                                 list_annotator_flow, **kwargs).get_result()).unstructured[0].data)

        return result

    # Name modified manually from analyze_with_flow to analyze_with_flow_org
    def analyze_with_flow_org(self, flow_id, request, content_type='text/plain', **kwargs):
        """
        Analyze with a persisted flow and return as a 'dict'.

        <p>This API accepts a flow identifier as well as a <emph>TEXT</emph> or a <emph>JSON</emph> request model
        featuring the unstructured text to be analyzed. <p/><p><b>JSON request model with unstructured text
        </b></p><pre>{<br/>  \"unstructured\": [<br/>    {<br/>      \"text\": \"Patient has lung cancer,
        but did not smoke. She may consider chemotherapy as part of a treatment plan.\"<br/>    }<br/>  ]
        <br/>}<br/></pre><p><b>JSON request model with existing annotations </b><br/></p><pre>{<br> \"unstructured\":
        [<br>    {<br>      \"text\": \"Patient will not start on cisplatin 80mg on 1/1/2018. Patient is also
        diabetic.\",<br>      \"data\": {<br>        \"concepts\": [<br>          {<br>            \"cui\":
        \"C0030705\",<br>            \"preferredName\": \"Patients\",<br>            \"semanticType\": \"podg\",
        <br>            \"source\": \"umls\",<br>            \"sourceVersion\": \"2017AA\",<br>            \"type\":
        \"umls.PatientOrDisabledGroup\",<br>            \"begin\": 0,<br>            \"end\": 7,<br>
        \"coveredText\": \"Patient\"<br>          }<br> ]<br>      }  <br>    } <br> ]<br>}<br></pre>.

        :param str flow_id: flow identifier .
        :param RequestContainer request: Input request data in TEXT or JSON format .
        :param str content_type: The type of the input: text/plain or application/json. A character encoding can be
        specified by including a `charset` parameter. For example, 'text/plain;charset=utf-8'.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code
        :rtype: Detailed Response
        """
        headers = {
            'content-type': content_type
        }

        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='analyze_with_flow_org')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        
        params = {
            'version': self.version
        }
        if content_type == 'application/json' and isinstance(request, dict):
            data = json.dumps(request)
        else:
            data = request
        url = 'v1/analyze/{0}'.format(flow_id)
        request = self.prepare_request(method='POST', url=url, headers=headers, params=params, data=data)
        response = self.request_acd(request)

        return response

    # Manually added method.
    def analyze_with_flow(self, flow_id, text, **kwargs):
        """
        Analyze with a persisted flow and return as a 'ContainerGroup'.

        :param str flow_id: The ID of a persisted flow.
        :param str or UnstructuredContainer or list[UnstructuredContainer] text: Text to be analyzed.
        :return: A 'ContainerGroup' object
        :rtype: watson_health_cognitive_services.annotator_for_clinical_data_v1.ContainerAnnotation
        """

        if isinstance(text, list):

            request_container = RequestContainer(text)
            result = self.analyze_with_flow_org(flow_id, request_container._to_dict(), 'application/json', **kwargs)
            result = ContainerGroup._from_dict(result.get_result())
        elif isinstance(text, UnstructuredContainer):

            list_unstructured_container = [text]
            request_container = RequestContainer(list_unstructured_container)
            result = self.analyze_with_flow_org(flow_id, request_container._to_dict(), 'application/json', **kwargs)
            result = ContainerGroup._from_dict(result.get_result()).unstructured[0].data
        else:

            result = self.analyze_with_flow_org(flow_id, text)
            result = ContainerGroup._from_dict(result.get_result()).unstructured[0].data

        return result

    def get_annotator(self, id, **kwargs):
        """
        Get details of a specific annotator.

        Get details of an annotator that can be used to derive information from unstructured data.

        :param str id: The ID the Service API was registered under.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedReponse with 'dict' representing an Annotator object.
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='get_annotator')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        url = 'v1/annotators/{0}'.format(id)
        request = self.prepare_request(method='GET', url=url, params=params)
        response = self.request_acd(request)

        return response

    def list_annotators(self, **kwargs):
        """
        Get list of available annotators.

        Get list of available annotators that can be leveraged to detect information from unstructured data.
        One or more annnotators can be leveraged within a single request to the service.

        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedReponse with 'dict'.
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='list_annotators')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        
        params = {
            'version': self.version
        }
        url = 'v1/annotators'
        request = self.prepare_request(method='GET', url=url, params=params)
        response = self.request_acd(request)

        return response

    #########################
    # Flows
    #########################

    def create_persisted_flow(self, new_id=None, new_name=None, new_description=None, new_annotator_flows=None, **kwargs):
        """
        Persist a new flow definition.

        This API persists a new flow.  A flow is identified by an ID.  This ID can optionally be specified as part
        of the request body when invoking <b>POST /v1/analyze</b> API.  A flow definition contains a list one or
        more annotators, and optionally can include annotator configuration, a profile ID, and/or flow sequence.
        <p>If a caller would choose to have the ID of the new flow generated on their behalf, then in the request
        body the \"id\" field of the flow definition should be an empty string (\"\").  The auto-generated ID
        would be a normalized form of the \"name\" field from the flow definition.<p><p><b>Sample Flow #1</b><br>
        A flow definition that includes two annotators.<br><pre>{<br>  \"id\": \"flow_simple\",<br>  \"name\":
        \"flow simple\",<br>  \"description\": \"A simple flow with two annotators\",<br>  \"annotatorFlows\":
        [<br>      {<br>       \"flow\": {<br>          \"elements\": [<br>             {<br>
        \"annotator\": {<br>                   \"name\": \"concept_detection\"<br>                }<br>
        },<br>             {<br>               \"annotator\": {<br>                   \"name\": \"symptom_disease\"
        <br>                }<br>             }<br>           ],<br>       \"async\": false<br>        }<br>
        }<br>   ]<br>}</pre><p><b>Sample Flow #2</b><br>A flow definition that includes the 'concept_detection'
        annotator and configuration details for the 'concept_detection' annotator.<br><pre>{<br>
        \"id\": \"flow_concept_detection_exclude_non_neop\",<br>  \"name\": \"flow concept detection exclude
        non neop\",<br>  \"description\": \"A flow excluding detected concepts that do not have 'neop' semantic
        type\",<br>  \"annotatorFlows\": [<br>      {<br>       \"flow\": {<br>          \"elements\": [<br>
        {<br>               \"annotator\": {<br>                   \"name\": \"concept_detection\",<br>
        \"configurations\": [<br>                      {<br>                        \"filter\": {<br>
        \"target\": \"unstructured.data.concepts\",<br>                           \"condition\": {<br>
        \"type\": \"match\",<br>                              \"field\": \"semanticType\",<br>
        \"values\": [<br>                                 \"neop\"<br>                                ],<br>
        \"not\": false,<br>                              \"caseInsensitive\": false,<br>
        \"operator\": \"equals\"<br>                            }<br>                         }<br>
        }<br>                    ]<br>                 }<br>              }<br>         ],<br>
        \"async\": false<br>        }<br>      }<br>   ]<br>}</pre>.

        :param str new_id:
        :param str new_name:
        :param str new_description:
        :param list[AnnotatorFlow] new_annotator_flows:
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        if new_annotator_flows is not None:
            new_annotator_flows = [x._to_dict() if hasattr(x, "_to_dict") else x for x in new_annotator_flows]

        headers = {'content-type': 'application/json'}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='create_persisted_flow')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        data = {
            'id': new_id,
            'name': new_name,
            'description': new_description,
            'annotatorFlows': new_annotator_flows
        }
        json_string = json.dumps(data)
        url = 'v1/flows'
        request = self.prepare_request(method='POST', url=url, headers=headers, params=params, data=json_string)
        response = self.request_acd(request)

        return response

    def delete_persisted_flow(self, id, **kwargs):
        """
        Delete a persisted flow.

        Using the specified Flow ID, deletes the flow from the list of persisted flows.

        :param str id: Flow ID.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='delete_persisted_flow')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        url = 'v1/flows/{0}'.format(id)
        request = self.prepare_request(method='DELETE', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response

    def get_flow(self, id, **kwargs):
        """
        Get details of a specific flow.

        Using the specified Flow ID, retrieves the flow definition.

        :param str id: Flow ID.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict' representing an AcdFlow object.
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='get_flow')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        url = 'v1/flows/{0}'.format(id)
        request = self.prepare_request(method='GET', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response


    def get_flows(self, **kwargs):
        """
        Get list of available persisted flows.

        Returns a summary including ID and description of the available persisted flows.

        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='get_flows')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        url = 'v1/flows'
        request = self.prepare_request(method='GET', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response


    def update_persisted_flow(self, flow_id=None, new_name=None, new_description=None, new_annotator_flows=None, **kwargs):
        """
        Update a persisted flow definition.

        Using the specified Flow ID, updates the persisted flow definition.  This is a complete replacement
        of the existing flow definition using the JSON object provided in the request body.

        :param str flow_id: Flow ID.
        :param str new_id:
        :param str new_name:
        :param str new_description:
        :param list[AnnotatorFlow] new_annotator_flows:
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        if new_annotator_flows is not None:
            new_annotator_flows = [x._to_dict() if hasattr(x, "_to_dict") else x for x in new_annotator_flows]

        headers = {'content-type': 'application/json'}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='update_persisted_flow')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'version': self.version
        }
        data = {
            'id': flow_id,
            'name': new_name,
            'description': new_description,
            'annotatorFlows': new_annotator_flows
        }
        json_string = json.dumps(data)
        url = 'v1/flows/{0}'.format(flow_id)
        request = self.prepare_request(method='PUT', url=url, headers=headers, params=params, data=json_string)
        response = self.request_acd(request)

        return response


    #########################
    # Profiles
    #########################

    def create_profile(self, new_id=None, new_name=None, new_description=None, new_annotators=None, **kwargs):
        """
        Persist a new profile.

        This API persists a new profile.  A profile is identified by an ID.  This ID can optionally be specified
        as part of the request body when invoking <b>POST /v1/analyze</b> API.  A profile contains annotator
        configuration information that will be applied to the annotators specified in the annotator flow.
        <p>If a caller would choose to have the ID of the new profile generated on their behalf, then in the request
        body the \"id\" field of the profile definition should be an empty string (\"\").  The auto-generated ID would
        be a normalized form of the \"name\" field from the profile definition.<p><b>Sample Profile #1</b><br>A profile
        definition that configures the 'concept_detection' annotator to use UMLS 2015AA library.<br><pre>{<br>
        \"id\": \"acd_profile_cd_umls2015\",<br>  \"name\": \"Profile for Concept Detection UMLS 2015 Library\",<br>
        \"description\": \"Provides configurations for running Concept Detection with the UMLS 2015 library\",<br>
        \"annotators\": [<br>    {<br>      \"name\": \"concept_detection\",<br>      \"parameters\": {<br>
        \"libraries\": [\"umls.2015AA\"]<br>       }<br>    }<br>  ]<br>}</pre><p><b>Sample Profile #2</b><br>
        A profile definition that configures the 'concept_detection' annotator to exclude any annotations where
        the semantic type does not equal 'neop'.<br><pre>{<br>  \"id\": \"acd_profile_cd_neop_only\",<br>
        \"name\": \"Profile for Concept Detection neop Semantic Type\",<br>  \"description\": \"Concept Detection
        configuration fitler to exclude annotations where semantic type does not equal 'neop'.\",<br>  \"annotators\":
        [<br>    {<br>       \"name\": \"concept_detection\",<br>       \"configurations\": [<br>         {<br>
        \"filter\": {<br>             \"target\": \"unstructured.data.concepts\",<br>             \"condition\":
        {<br>                \"type\": \"match\",<br>                \"field\": \"semanticType\",<br>
        \"values\": [<br>                   \"neop\"<br>                 ],<br>                \"not\": false,<br>
        \"caseInsensitive\": false,<br>                \"operator\": \"equals\"<br>              }<br>            }
        <br>         }<br>       ]<br>    }<br>  ]<br>}</pre>.

        :param str new_id:
        :param str new_name:
        :param str new_description:
        :param list[Annotator] new_annotators:
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        if new_annotators is not None:
            new_annotators = [x._to_dict() if hasattr(x, "_to_dict") else x for x in new_annotators]

        headers = {'content-type': 'application/json'}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='create_profile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }
        data = {
            'id': new_id,
            'name': new_name,
            'description': new_description,
            'annotators': new_annotators
        }
        data = json.dumps(data)
        url = 'v1/profiles'
        request = self.prepare_request(method='POST', url=url, headers=headers, params=params, data=data)
        response = self.request_acd(request)

        return response


    def delete_profile(self, id, **kwargs):
        """
        Delete a persisted profile.

        Using the specified profile ID, deletes the profile from the list of persisted profiles.

        :param str id: Profile ID.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='delete_profile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }
        url = 'v1/profiles/{0}'.format(id)
        request = self.prepare_request(method='DELETE', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response


    def get_profile(self, id, **kwargs):
        """
        Get details of a specific profile.

        Using the specified profile ID, retrieves the profile definition.

        :param str id: Profile ID.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict' representing an AcdProfile object.
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='get_profile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }
        url = 'v1/profiles/{0}'.format(id)
        request = self.prepare_request(method='GET', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response


    def get_profiles(self, **kwargs):
        """
        Get list of available persisted profiles.

        Returns a summary including ID and description of the available persisted profiles.

        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='get_profiles')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }
        url = 'v1/profiles'
        request = self.prepare_request(method='GET', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response


    def update_profile(self, id=None, new_name=None, new_description=None, new_annotators=None, **kwargs):
        """
        Update a persisted profile definition.

        Using the specified Profile ID, updates the profile definition.  This is a complete replacement of the
        existing profile definition using the JSON object provided in the request body.

        :param str id: Profile ID.
        :param str id:
        :param str new_name:
        :param str new_description:
        :param list[Annotator] new_annotators:
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetaileddReponse with 'dict'.
        """
        if new_annotators is not None:
            new_annotators = [x._to_dict() if hasattr(x, "_to_dict") else x for x in new_annotators]

        headers = {'content-type': 'application/json'}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='analyze_org')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }

        data = {
            'id': id,
            'name': new_name,
            'description': new_description,
            'annotators': new_annotators
        }
        data = json.dumps(data)
        url = 'v1/profiles/{0}'.format(id)
        request = self.prepare_request(method='PUT', url=url, headers=headers, params=params, data=data)
        response = self.request_acd(request)

        return response


    def delete_user_data(self, **kwargs):
        """
        The ACD service enables you to delete all data that is associated to a specific tenant.
        Every ACD request is, by default, associated with a tenant ID. A default tenant id is assigned
        if no tenant id is supplied in a request.

        The method has no effect if no data is associated with the tenant ID. This deletion operation is only
        allowed for a specific tenant id and is not permitted for a default tenant.

        :return nothing is returned if successful
        """
        headers = {}
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='analyze_org')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version
        }

        url = 'v1/user_data'
        request = self.prepare_request(method='DELETE', url=url, params=params, headers=headers)
        response = self.request_acd(request)

        return response

    #########################
    # Status
    #########################
    def get_health_check_status(self, accept=None, apikey=None, format=None, **kwargs):
        """
        Determine if service is running correctly.
        This resource differs from /status in that it will will always return a 500 error
        if the service state is not OK.  This makes it simpler for service front ends
        to detect a failed service.
        :param str accept: The type of the response: application/json or application/xml.
        :param str apikey: access key.
        :param str format: Override response format.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """


        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=SERVICE_NAME, service_version='V2', operation_id='analyze_org')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'apikey': apikey,
            'format': format
        }
        url = '/v1/status/health_check'
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)
        response = self.request_acd(request)
        return response

##############################################################################
# Models
##############################################################################


class AcdFlow(object):
    """
    AcdFlow.

    :attr str id: (optional)
    :attr str name: (optional)
    :attr str description: (optional)
    :attr list[AnnotatorFlow] annotator_flows: (optional)
    """

    def __init__(self, id=None, name=None, description=None, annotator_flows=None):
        """
        Initialize a AcdFlow object.

        :param str id: (optional)
        :param str name: (optional)
        :param str description: (optional)
        :param list[AnnotatorFlow] annotator_flows: (optional)
        """
        self.id = id
        self.name = name
        self.description = description
        self.annotator_flows = annotator_flows

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcdFlow object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict['id']
        if 'name' in _dict:
            args['name'] = _dict['name']
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'annotatorFlows' in _dict:
            args['annotator_flows'] = [AnnotatorFlow._from_dict(x) for x in _dict['annotatorFlows']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'annotator_flows') and self.annotator_flows is not None:
            _dict['annotatorFlows'] = [x._to_dict() for x in self.annotator_flows]
        return _dict

    def __str__(self):
        """Return a `str` version of this AcdFlow object."""
        return json.dumps(self._to_dict(), indent=2)


class AcdProfile(object):
    """
    AcdProfile.

    :attr str id: (optional)
    :attr str name: (optional)
    :attr str description: (optional)
    :attr list[Annotator] annotators: (optional)
    """

    def __init__(self, id=None, name=None, description=None, annotators=None):
        """
        Initialize a AcdProfile object.

        :param str id: (optional)
        :param str name: (optional)
        :param str description: (optional)
        :param list[Annotator] annotators: (optional)
        """
        self.id = id
        self.name = name
        self.description = description
        self.annotators = annotators

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcdProfile object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict['id']
        if 'name' in _dict:
            args['name'] = _dict['name']
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'annotators' in _dict:
            args['annotators'] = [Annotator._from_dict(x) for x in _dict['annotators']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'annotators') and self.annotators is not None:
            _dict['annotators'] = [x._to_dict() for x in self.annotators]
        return _dict

    def __str__(self):
        """Return a `str` version of this AcdProfile object."""
        return json.dumps(self._to_dict(), indent=2)


class AnnotatorFlow(object):
    """
    AnnotatorFlow.

    :attr str profile: (optional)
    :attr Flow flow: (optional)
    """

    def __init__(self, profile=None, flow=None):
        """
        Initialize a AnnotatorFlow object.

        :param str profile: (optional)
        :param Flow flow: (optional)
        """
        self.profile = profile
        self.flow = flow

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnnotatorFlow object from a json dictionary."""
        args = {}
        if 'profile' in _dict:
            args['profile'] = _dict['profile']
        if 'flow' in _dict:
            args['flow'] = Flow._from_dict(_dict['flow'])
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'profile') and self.profile is not None:
            _dict['profile'] = self.profile
        if hasattr(self, 'flow') and self.flow is not None:
            _dict['flow'] = self.flow._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this AnnotatorFlow object."""
        return json.dumps(self._to_dict(), indent=2)


class ConfigurationEntity(object):
    """
    ConfigurationEntity.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    """

    def __init__(self, id=None, type=None, uid=None):
        """
        Initialize a ConfigurationEntity object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        """
        self.id = id
        self.type = type
        self.uid = uid

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigurationEntity object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        return _dict

    def __str__(self):
        """Return a `str` version of this ConfigurationEntity object."""
        return json.dumps(self._to_dict(), indent=2)


class ContainerAnnotation(object):
    """
    ContainerAnnotation.

    :attr list[Annotation] allergy_ind: (optional)
    :attr list[Annotation] allergy_medication_ind: (optional)
    :attr list[AttributeValueAnnotation] attribute_values: (optional)
    :attr list[AssistanceAnnotation] bathing_assistance_ind: (optional)
    :attr list[CancerDiagnosis] ica_cancer_diagnosis_ind: (optional)
    :attr list[Concept] concepts: (optional)
    :attr list[ConceptValue] concept_values: (optional)
    :attr list[AssistanceAnnotation] dressing_assistance_ind: (optional)
    :attr list[AssistanceAnnotation] eating_assistance_ind: (optional)
    :attr list[EjectionFractionAnnotation] ejection_fraction_ind: (optional)
    :attr list[Annotation] hypothetical_spans: (optional)
    :attr list[LabValueAnnotation] lab_value_ind: (optional)
    :attr list[MedicationAnnotation] medication_ind: (optional)
    :attr list[Annotation] email_address_ind: (optional)
    :attr list[Annotation] location_ind: (optional)
    :attr list[Annotation] person_ind: (optional)
    :attr list[Annotation] u_s_phone_number_ind: (optional)
    :attr list[Annotation] medical_institution_ind: (optional)
    :attr list[Annotation] organization_ind: (optional)
    :attr list[NegatedSpan] negated_spans: (optional)
    :attr list[Procedure] procedure_ind: (optional)
    :attr list[AssistanceAnnotation] seeing_assistance_ind: (optional)
    :attr list[Smoking] smoking_ind: (optional)
    :attr list[SymptomDisease] symptom_disease_ind: (optional)
    :attr list[AssistanceAnnotation] toileting_assistance_ind: (optional)
    :attr list[AssistanceAnnotation] walking_assistance_ind: (optional)
    :attr list[Section] sections: (optional)
    :attr list[NluEntities] nlu_entities: (optional)
    :attr list[Relations] relations: (optional)
    :attr list[SpellingCorrection]: (optional)
    :attr list[SpellCorrectedText] spell_corrected_text: (optional)
    """

    def __init__(self, allergy_ind=None, allergy_medication_ind=None, attribute_values=None,
                 bathing_assistance_ind=None, ica_cancer_diagnosis_ind=None, concepts=None,
                 concept_values=None, dressing_assistance_ind=None, eating_assistance_ind=None,
                 ejection_fraction_ind=None, hypothetical_spans=None, lab_value_ind=None, medication_ind=None,
                 email_address_ind=None, location_ind=None, person_ind=None, u_s_phone_number_ind=None,
                 medical_institution_ind=None, organization_ind=None, negated_spans=None, procedure_ind=None,
                 seeing_assistance_ind=None, smoking_ind=None, symptom_disease_ind=None, toileting_assistance_ind=None,
                 walking_assistance_ind=None, sections=None, nlu_entities=None, relations=None,
                 spelling_corrections=None, spell_corrected_text=None):
        """
        Initialize a ContainerAnnotation object.

        :param list[Annotation] allergy_ind: (optional)
        :param list[Annotation] allergy_medication_ind: (optional)
        :param list[AttributeValueAnnotation] attribute_values: (optional)
        :param list[AssistanceAnnotation] bathing_assistance_ind: (optional)
        :param list[CancerDiagnosis] ica_cancer_diagnosis_ind: (optional)
        :param list[Concept] concepts: (optional)
        :param list[ConceptValue] concept_values: (optional)
        :param list[AssistanceAnnotation] dressing_assistance_ind: (optional)
        :param list[AssistanceAnnotation] eating_assistance_ind: (optional)
        :param list[EjectionFractionAnnotation] ejection_fraction_ind: (optional)
        :param list[Annotation] hypothetical_spans: (optional)
        :param list[LabValueAnnotation] lab_value_ind: (optional)
        :param list[MedicationAnnotation] medication_ind: (optional)
        :param list[Annotation] email_address_ind: (optional)
        :param list[Annotation] location_ind: (optional)
        :param list[Annotation] person_ind: (optional)
        :param list[Annotation] u_s_phone_number_ind: (optional)
        :param list[Annotation] medical_institution_ind: (optional)
        :param list[Annotation] organization_ind: (optional)
        :param list[NegatedSpan] negated_spans: (optional)
        :param list[Procedure] procedure_ind: (optional)
        :param list[AssistanceAnnotation] seeing_assistance_ind: (optional)
        :param list[Smoking] smoking_ind: (optional)
        :param list[SymptomDisease] symptom_disease_ind: (optional)
        :param list[AssistanceAnnotation] toileting_assistance_ind: (optional)
        :param list[AssistanceAnnotation] walking_assistance_ind: (optional)
        :param list[Section] sections: (optional)
        :param list[NluEntities] nlu_entities: (optional)
        :param list[Relations] relations: (optional)
        :param list[SpellingCorrection] spelling_correction: (optional)
        :param list[SpellCorrectedText] spell_corrected_text: (optional)
        """
        self.allergy_ind = allergy_ind
        self.allergy_medication_ind = allergy_medication_ind
        self.attribute_values = attribute_values
        self.bathing_assistance_ind = bathing_assistance_ind
        self.ica_cancer_diagnosis_ind = ica_cancer_diagnosis_ind
        self.concepts = concepts
        self.concept_values = concept_values
        self.dressing_assistance_ind = dressing_assistance_ind
        self.eating_assistance_ind = eating_assistance_ind
        self.ejection_fraction_ind = ejection_fraction_ind
        self.hypothetical_spans = hypothetical_spans
        self.lab_value_ind = lab_value_ind
        self.medication_ind = medication_ind
        self.email_address_ind = email_address_ind
        self.location_ind = location_ind
        self.person_ind = person_ind
        self.u_s_phone_number_ind = u_s_phone_number_ind
        self.medical_institution_ind = medical_institution_ind
        self.organization_ind = organization_ind
        self.negated_spans = negated_spans
        self.procedure_ind = procedure_ind
        self.seeing_assistance_ind = seeing_assistance_ind
        self.smoking_ind = smoking_ind
        self.symptom_disease_ind = symptom_disease_ind
        self.toileting_assistance_ind = toileting_assistance_ind
        self.walking_assistance_ind = walking_assistance_ind
        self.sections = sections
        self.nlu_entities = nlu_entities
        self.relations = relations
        self.spelling_corrections = spelling_corrections
        self.spell_corrected_text = spell_corrected_text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerAnnotation object from a json dictionary."""
        args = {}
        if 'AllergyMedicationInd' in _dict:
            args['allergy_medication_ind'] = [Annotation._from_dict(x) for x in _dict['AllergyMedicationInd']]
        if 'AllergyInd' in _dict:
            args['allergy_ind'] = [Annotation._from_dict(x) for x in _dict['AllergyInd']]
        if 'attributeValues' in _dict:
            args['attribute_values'] = [AttributeValueAnnotation._from_dict(x) for x in _dict['attributeValues']]
        if 'BathingAssistanceInd' in _dict:
            args['bathing_assistance_ind'] = ([AssistanceAnnotation._from_dict(x)
                                               for x in _dict['BathingAssistanceInd']])
        if 'IcaCancerDiagnosisInd' in _dict:
            args['ica_cancer_diagnosis_ind'] = [CancerDiagnosis._from_dict(x) for x in _dict['IcaCancerDiagnosisInd']]
        if 'concepts' in _dict:
            args['concepts'] = [Concept._from_dict(x) for x in _dict['concepts']]
        if 'conceptValues' in _dict:
            args['concept_values'] = [ConceptValue._from_dict(x) for x in _dict['conceptValues']]
        if 'DressingAssistanceInd' in _dict:
            args['dressing_assistance_ind'] = ([AssistanceAnnotation._from_dict(x)
                                                for x in _dict['DressingAssistanceInd']])
        if 'EatingAssistanceInd' in _dict:
            args['eating_assistance_ind'] = [AssistanceAnnotation._from_dict(x) for x in _dict['EatingAssistanceInd']]
        if 'EjectionFractionInd' in _dict:
            args['ejection_fraction_ind'] = ([EjectionFractionAnnotation._from_dict(x)
                                              for x in _dict['EjectionFractionInd']])
        if 'hypotheticalSpans' in _dict:
            args['hypothetical_spans'] = [Annotation._from_dict(x) for x in _dict['hypotheticalSpans']]
        if 'LabValueInd' in _dict:
            args['lab_value_ind'] = [LabValueAnnotation._from_dict(x) for x in _dict['LabValueInd']]
        if 'MedicationInd' in _dict:
            args['medication_ind'] = [MedicationAnnotation._from_dict(x) for x in _dict['MedicationInd']]
        if 'EmailAddressInd' in _dict:
            args['email_address_ind'] = [Annotation._from_dict(x) for x in _dict['EmailAddressInd']]
        if 'LocationInd' in _dict:
            args['location_ind'] = [Annotation._from_dict(x) for x in _dict['LocationInd']]
        if 'PersonInd' in _dict:
            args['person_ind'] = [Annotation._from_dict(x) for x in _dict['PersonInd']]
        if 'US_PhoneNumberInd' in _dict:
            args['u_s_phone_number_ind'] = [Annotation._from_dict(x) for x in _dict['US_PhoneNumberInd']]
        if 'MedicalInstitutionInd' in _dict:
            args['medical_institution_ind'] = [Annotation._from_dict(x) for x in _dict['MedicalInstitutionInd']]
        if 'OrganizationInd' in _dict:
            args['organization_ind'] = [Annotation._from_dict(x) for x in _dict['OrganizationInd']]
        if 'negatedSpans' in _dict:
            args['negated_spans'] = [NegatedSpan._from_dict(x) for x in _dict['negatedSpans']]
        if 'ProcedureInd' in _dict:
            args['procedure_ind'] = [Procedure._from_dict(x) for x in _dict['ProcedureInd']]
        if 'SeeingAssistanceInd' in _dict:
            args['seeing_assistance_ind'] = [AssistanceAnnotation._from_dict(x) for x in _dict['SeeingAssistanceInd']]
        if 'SmokingInd' in _dict:
            args['smoking_ind'] = [Smoking._from_dict(x) for x in _dict['SmokingInd']]
        if 'SymptomDiseaseInd' in _dict:
            args['symptom_disease_ind'] = [SymptomDisease._from_dict(x) for x in _dict['SymptomDiseaseInd']]
        if 'ToiletingAssistanceInd' in _dict:
            args['toileting_assistance_ind'] = ([AssistanceAnnotation._from_dict(x)
                                                 for x in _dict['ToiletingAssistanceInd']])
        if 'WalkingAssistanceInd' in _dict:
            args['walking_assistance_ind'] = ([AssistanceAnnotation._from_dict(x)
                                               for x in _dict['WalkingAssistanceInd']])
        if 'sections' in _dict:
            args['sections'] = [Section._from_dict(x) for x in _dict['sections']]
        if 'nluEntities' in _dict:
            args['nlu_entities'] = [NluEntities._from_dict(x) for x in _dict['nluEntities']]
        if 'relations' in _dict:
            args['relations'] = [Relations._from_dict(x) for x in _dict['relations']]
        if 'spellingCorrections' in _dict:
            args['spelling_corrections'] = [SpellingCorrection._from_dict(x) for x in _dict['spellingCorrections']]
        if 'spellCorrectedText' in _dict:
            args['spell_corrected_text'] = [SpellCorrectedText._from_dict(x) for x in _dict['spellCorrectedText']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allergy_medication_ind') and self.allergy_medication_ind is not None:
            _dict['AllergyMedicationInd'] = [x._to_dict() for x in self.allergy_medication_ind]
        if hasattr(self, 'allergy_ind') and self.allergy_ind is not None:
            _dict['AllergyInd'] = [x._to_dict() for x in self.allergy_ind]
        if hasattr(self, 'attribute_values') and self.attribute_values is not None:
            _dict['attributeValues'] = [x._to_dict() for x in self.attribute_values]
        if hasattr(self, 'bathing_assistance_ind') and self.bathing_assistance_ind is not None:
            _dict['BathingAssistanceInd'] = [x._to_dict() for x in self.bathing_assistance_ind]
        if hasattr(self, 'ica_cancer_diagnosis_ind') and self.ica_cancer_diagnosis_ind is not None:
            _dict['IcaCancerDiagnosisInd'] = [x._to_dict() for x in self.ica_cancer_diagnosis_ind]
        if hasattr(self, 'concepts') and self.concepts is not None:
            _dict['concepts'] = [x._to_dict() for x in self.concepts]
        if hasattr(self, 'concept_values') and self.concept_values is not None:
            _dict['conceptValues'] = [x._to_dict() for x in self.concept_values]
        if hasattr(self, 'dressing_assistance_ind') and self.dressing_assistance_ind is not None:
            _dict['DressingAssistanceInd'] = [x._to_dict() for x in self.dressing_assistance_ind]
        if hasattr(self, 'eating_assistance_ind') and self.eating_assistance_ind is not None:
            _dict['EatingAssistanceInd'] = [x._to_dict() for x in self.eating_assistance_ind]
        if hasattr(self, 'ejection_fraction_ind') and self.ejection_fraction_ind is not None:
            _dict['EjectionFractionInd'] = [x._to_dict() for x in self.ejection_fraction_ind]
        if hasattr(self, 'hypothetical_spans') and self.hypothetical_spans is not None:
            _dict['hypotheticalSpans'] = [x._to_dict() for x in self.hypothetical_spans]
        if hasattr(self, 'lab_value_ind') and self.lab_value_ind is not None:
            _dict['LabValueInd'] = [x._to_dict() for x in self.lab_value_ind]
        if hasattr(self, 'medication_ind') and self.medication_ind is not None:
            _dict['MedicationInd'] = [x._to_dict() for x in self.medication_ind]
        if hasattr(self, 'email_address_ind') and self.email_address_ind is not None:
            _dict['EmailAddressInd'] = [x._to_dict() for x in self.email_address_ind]
        if hasattr(self, 'location_ind') and self.location_ind is not None:
            _dict['LocationInd'] = [x._to_dict() for x in self.location_ind]
        if hasattr(self, 'person_ind') and self.person_ind is not None:
            _dict['PersonInd'] = [x._to_dict() for x in self.person_ind]
        if hasattr(self, 'u_s_phone_number_ind') and self.u_s_phone_number_ind is not None:
            _dict['US_PhoneNumberInd'] = [x._to_dict() for x in self.u_s_phone_number_ind]
        if hasattr(self, 'medical_institution_ind') and self.medical_institution_ind is not None:
            _dict['MedicalInstitutionInd'] = [x._to_dict() for x in self.medical_institution_ind]
        if hasattr(self, 'organization_ind') and self.organization_ind is not None:
            _dict['OrganizationInd'] = [x._to_dict() for x in self.organization_ind]
        if hasattr(self, 'negated_spans') and self.negated_spans is not None:
            _dict['negatedSpans'] = [x._to_dict() for x in self.negated_spans]
        if hasattr(self, 'procedure_ind') and self.procedure_ind is not None:
            _dict['ProcedureInd'] = [x._to_dict() for x in self.procedure_ind]
        if hasattr(self, 'seeing_assistance_ind') and self.seeing_assistance_ind is not None:
            _dict['SeeingAssistanceInd'] = [x._to_dict() for x in self.seeing_assistance_ind]
        if hasattr(self, 'smoking_ind') and self.smoking_ind is not None:
            _dict['SmokingInd'] = [x._to_dict() for x in self.smoking_ind]
        if hasattr(self, 'symptom_disease_ind') and self.symptom_disease_ind is not None:
            _dict['SymptomDiseaseInd'] = [x._to_dict() for x in self.symptom_disease_ind]
        if hasattr(self, 'toileting_assistance_ind') and self.toileting_assistance_ind is not None:
            _dict['ToiletingAssistanceInd'] = [x._to_dict() for x in self.toileting_assistance_ind]
        if hasattr(self, 'walking_assistance_ind') and self.walking_assistance_ind is not None:
            _dict['WalkingAssistanceInd'] = [x._to_dict() for x in self.walking_assistance_ind]
        if hasattr(self, 'sections') and self.sections is not None:
            _dict['sections'] = [x._to_dict() for x in self.sections]
        if hasattr(self, 'nlu_entities') and self.nlu_entities is not None:
            _dict['nluEntities'] = [x._to_dict() for x in self.nlu_entities]
        if hasattr(self, 'relations') and self.relations is not None:
            _dict['relations'] = [x._to_dict() for x in self.relations]
        if hasattr(self, 'spelling_corrections') and self.spelling_corrections is not None:
            _dict['spellingCorrections'] = [x._to_dict() for x in self.spelling_corrections]
        if hasattr(self, 'spell_corrected_text') and self.spell_corrected_text is not None:
            _dict['spellCorrectedText'] = [x._to_dict() for x in self.spell_corrected_text]
        return _dict

    def __str__(self):
        """Return a `str` version of this ContainerAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)

class ContainerGroup(object):
    """
    ContainerGroup.
    :attr list[UnstructuredContainer] unstructured: (optional)
    :attr list[AnnotatorFlow] annotator_flows: (optional)
    """

    def __init__(self, unstructured=None, annotator_flows=None):
        """
        Initialize a ContainerGroup object.
        :param list[UnstructuredContainer] unstructured: (optional)
        :param list[AnnotatorFlow] annotator_flows: (optional)
        """
        self.unstructured = unstructured
        self.annotator_flows = annotator_flows


    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerGroup object from a json dictionary."""
        args = {}
        if 'unstructured' in _dict:
            args['unstructured'] = [UnstructuredContainer._from_dict(x) for x in _dict['unstructured']]
        if 'annotatorFlows' in _dict:
            args['annotator_flows'] = [AnnotatorFlow._from_dict(x) for x in _dict['annotatorFlows']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'unstructured') and self.unstructured is not None:
            _dict['unstructured'] = [x._to_dict() for x in self.unstructured]
        if hasattr(self, 'annotator_flows') and self.annotator_flows is not None:
            _dict['annotatorFlows'] = [x._to_dict() for x in self.annotator_flows]
        return _dict

class Disambiguation(object):
    """
    Disambiguation.

    :attr str validity: (optional)
    """

    def __init__(self, validity=None):
        """
        Initialize a Disambiguation object.

        :param str validity: (optional)
        """
        self.validity = validity

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Disambiguation object from a json dictionary."""
        args = {}
        if 'validity' in _dict:
            args['validity'] = _dict['validity']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'validity') and self.validity is not None:
            _dict['validity'] = self.validity
        return _dict

    def __str__(self):
        """Return a `str` version of this Disambiguation object."""
        return json.dumps(self._to_dict(), indent=2)


class Flow(object):
    """
    Flow.

    :attr list[FlowEntry] elements: (optional)
    :attr bool async: (optional)
    """

    def __init__(self, elements=None, async_=None):
        """
        Initialize a Flow object.

        :param list[FlowEntry] elements: (optional)
        :param bool async: (optional)
        """
        self.elements = elements
        self.async_ = async_

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Flow object from a json dictionary."""
        args = {}
        if 'elements' in _dict:
            args['elements'] = [FlowEntry._from_dict(x) for x in _dict['elements']]
        if 'async' in _dict:
            args['async_'] = _dict['async']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'elements') and self.elements is not None:
            _dict['elements'] = [x._to_dict() for x in self.elements]
        if hasattr(self, 'async_') and self.async_ is not None:
            _dict['async'] = self.async_
        return _dict

    def __str__(self):
        """Return a `str` version of this Flow object."""
        return json.dumps(self._to_dict(), indent=2)


class FlowEntry(object):
    """
    FlowEntry.

    :attr Annotator annotator: (optional)
    :attr Flow flow: (optional)
    """

    def __init__(self, annotator=None, flow=None):
        """
        Initialize a FlowEntry object.

        :param Annotator annotator: (optional)
        :param Flow flow: (optional)
        """
        self.annotator = annotator
        self.flow = flow

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FlowEntry object from a json dictionary."""
        args = {}
        if 'annotator' in _dict:
            args['annotator'] = Annotator._from_dict(_dict['annotator'])
        if 'flow' in _dict:
            args['flow'] = Flow._from_dict(_dict['flow'])
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'annotator') and self.annotator is not None:
            _dict['annotator'] = self.annotator._to_dict()
        if hasattr(self, 'flow') and self.flow is not None:
            _dict['flow'] = self.flow._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this FlowEntry object."""
        return json.dumps(self._to_dict(), indent=2)


class ListStringWrapper(object):
    """
    ListStringWrapper.

    :attr list[str] data: (optional)
    """

    def __init__(self, data=None):
        """
        Initialize a ListStringWrapper object.

        :param list[str] data: (optional)
        """
        self.data = data

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListStringWrapper object from a json dictionary."""
        args = {}
        if 'data' in _dict:
            args['data'] = _dict['data']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def __str__(self):
        """Return a `str` version of this ListStringWrapper object."""
        return json.dumps(self._to_dict(), indent=2)


class RequestContainer(object):
    """
    RequestContainer.

    :attr list[UnstructuredContainer] unstructured: (optional)
    :attr list[AnnotatorFlow] annotator_flows: (optional)
    """

    def __init__(self, unstructured=None, annotator_flows=None):
        """
        Initialize a RequestContainer object.

        :param list[UnstructuredContainer] unstructured: (optional)
        :param list[AnnotatorFlow] annotator_flows: (optional)
        """
        self.unstructured = unstructured
        self.annotator_flows = annotator_flows

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequestContainer object from a json dictionary."""
        args = {}
        if 'unstructured' in _dict:
            args['unstructured'] = [UnstructuredContainer._from_dict(x) for x in _dict['unstructured']]
        if 'annotatorFlows' in _dict:
            args['annotator_flows'] = [AnnotatorFlow._from_dict(x) for x in _dict['annotatorFlows']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'unstructured') and self.unstructured is not None:
            _dict['unstructured'] = [x._to_dict() for x in self.unstructured]
        if hasattr(self, 'annotator_flows') and self.annotator_flows is not None:
            _dict['annotatorFlows'] = [x._to_dict() for x in self.annotator_flows]
        return _dict

    def __str__(self):
        """Return a `str` version of this RequestContainer object."""
        return json.dumps(self._to_dict(), indent=2)


class UnstructuredContainer(object):
    """
    UnstructuredContainer.

    :attr str text: (optional)
    :attr str id: (optional)
    :attr str type: (optional)
    :attr ContainerAnnotation data: (optional)
    :attr dict metadata: (optional)
    :attr int uid: (optional)
    """

    def __init__(self, text=None, id=None, type=None, data=None, metadata=None, uid=None):
        """
        Initialize a UnstructuredContainer object.

        :param str text: (optional)
        :param str id: (optional)
        :param str type: (optional)
        :param ContainerAnnotation data: (optional)
        :param dict metadata: (optional)
        :param int uid: (optional)
        """
        self.text = text
        self.id = id
        self.type = type
        self.data = data
        self.metadata = metadata
        self.uid = uid

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UnstructuredContainer object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
        if 'id' in _dict:
            args['id'] = _dict['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
        if 'data' in _dict:
            args['data'] = ContainerAnnotation._from_dict(_dict['data'])
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data._to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        return _dict

    def __str__(self):
        """Return a `str` version of this UnstructuredContainer object."""
        return json.dumps(self._to_dict(), indent=2)


class AllergyMedication(object):
    """
    AllergyMedication.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    :attr MedicationAnnotation medication: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, section_normalized_name=None, section_surface_form=None, medication=None,
                 **kwargs):
        """
        Initialize a AllergyMedication object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param MedicationAnnotation medication: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        self.medication = medication
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllergyMedication object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'medication' in _dict:
            args['medication'] = [MedicationAnnotation._from_dict(v) for v in _dict['medication']]
            del xtra['medication']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'medication') and self.medication is not None:
            _dict['medication'] = [v._to_dict() for v in self.medication]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'section_normalized_name', 'section_surface_form', 'medication'})
        if not hasattr(self, '_additionalProperties'):
            super(AllergyMedication, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(AllergyMedication, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this AllergyMedication object."""
        return json.dumps(self._to_dict(), indent=2)


class Annotation(object):
    """
    Annotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, section_normalized_name=None, section_surface_form=None, **kwargs):
        """
        Initialize a Annotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Annotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'section_normalized_name', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(Annotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Annotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Annotation object."""
        return json.dumps(self._to_dict(), indent=2)


class Annotator(object):
    """
    Annotator.

    :attr Annotator annotator: (optional)
    :attr Flow flow: (optional)
    :attr str name: (optional)
    :attr str description: (optional)
    :attr object parameters: (optional)
    :attr list[ConfigurationEntity] configurations: (optional)
    """

    def __init__(self, name=None, annotator=None, flow=None, description=None, parameters=None, configurations=None):
        """
        Initialize a Annotator object.

        :param str name: (optional)
        :param Annotator annotator: (optional)
        :param Flow flow: (optional)
        :param str description: (optional)
        :param object parameters: (optional)
        :param list[ConfigurationEntity] configurations: (optional)
        """
        self.annotator = annotator
        self.flow = flow
        self.name = name
        self.description = description
        self.parameters = parameters
        self.configurations = configurations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Annotator object from a json dictionary."""
        args = {}
        if 'annotator' in _dict:
            args['annotator'] = Annotator._from_dict(_dict['annotator'])
        if 'flow' in _dict:
            args['flow'] = Flow._from_dict(_dict['flow'])
        if 'name' in _dict:
            args['name'] = _dict['name']
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'parameters' in _dict:
            args['parameters'] = _dict['parameters']
        if 'configurations' in _dict:
            args['configurations'] = [ConfigurationEntity._from_dict(x) for x in _dict['configurations']]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'annotator') and self.annotator is not None:
            _dict['annotator'] = self.annotator._to_dict()
        if hasattr(self, 'flow') and self.flow is not None:
            _dict['flow'] = self.flow._to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'configurations') and self.configurations is not None:
            _dict['configurations'] = [x._to_dict() for x in self.configurations]
        return _dict

    def __str__(self):
        """Return a `str` version of this Annotator object."""
        return json.dumps(self._to_dict(), indent=2)

class Name(object):
    # allergy.
    ALLERGY = "allergy"
    # attribute_detection.
    ATTRIBUTE_DETECTION = "attribute_detection"
    # bathing_assistance.
    BATHING_ASSISTANCE = "bathing_assistance"
    # cancer.
    CANCER = "cancer"
    # concept_detection.
    CONCEPT_DETECTION = "concept_detection"
    # concept_value.
    CONCEPT_VALUE = "concept_value"
    # disambiguation.
    DISAMBIGUATION = "disambiguation"
    # dressing_assistance.
    DRESSING_ASSISTANCE = "dressing_assistance"
    # eating_assistance.
    EATING_ASSISTANCE = "eating_assistance"
    # ejection_fraction.
    EJECTION_FRACTION = "ejection_fraction"
    # hypothetical.
    HYPOTHETICAL = "hypothetical"
    # lab_value.
    LAB_VALUE = "lab_value"
    # medication.
    MEDICATION = "medication"
    # named_entities.
    NAMED_ENTITIES = "named_entities"
    # negation.
    NEGATION = "negation"
    # procedure.
    PROCEDURE = "procedure"
    # relation.
    RELATION = "relation"
    # seeing_assistance.
    SEEING_ASSISTANCE = "seeing_assistance"
    # smoking.
    SMOKING = "smoking"
    # spell checker
    SPELL_CHECKER = "spell_checker"
    # symptom_disease.
    SYMPTOM_DISEASE = "symptom_disease"
    # toileting_assistance.
    TOILETING_ASSISTANCE = "toileting_assistance"
    # walking_assistance.
    WALKING_ASSISTANCE = "walking_assistance"
    # section.
    SECTION = "section"
    # nlu.
    NLU = "nlu"


class AssistanceAnnotation(object):
    """
    AssistanceAnnotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str primary_action_normalized_name: (optional)
    :attr str modality: (optional)
    :attr str primary_action_surface_form: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, primary_action_normalized_name=None, modality=None,
                 primary_action_surface_form=None, section_normalized_name=None, section_surface_form=None,
                 **kwargs):
        """
        Initialize a AssistanceAnnotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str primary_action_normalized_name: (optional)
        :param str modality: (optional)
        :param str primary_action_surface_form: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.primary_action_normalized_name = primary_action_normalized_name
        self.modality = modality
        self.primary_action_surface_form = primary_action_surface_form
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssistanceAnnotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'primaryActionNormalizedName' in _dict:
            args['primary_action_normalized_name'] = _dict['primaryActionNormalizedName']
            del xtra['primaryActionNormalizedName']
        if 'modality' in _dict:
            args['modality'] = _dict['modality']
            del xtra['modality']
        if 'primaryActionSurfaceForm' in _dict:
            args['primary_action_surface_form'] = _dict['primaryActionSurfaceForm']
            del xtra['primaryActionSurfaceForm']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'primary_action_normalized_name') and self.primary_action_normalized_name is not None:
            _dict['primaryActionNormalizedName'] = self.primary_action_normalized_name
        if hasattr(self, 'modality') and self.modality is not None:
            _dict['modality'] = self.modality
        if hasattr(self, 'primary_action_surface_form') and self.primary_action_surface_form is not None:
            _dict['primaryActionSurfaceForm'] = self.primary_action_surface_form
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'primary_action_normalized_name', 'modality', 'primary_action_surface_form',
                       'section_normalized_name', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(AssistanceAnnotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(AssistanceAnnotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this AssistanceAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)

class AttributeValueEntry(object):
    """
    AttributeValueEntry.

    :attr str value: (optional)
    :attr str unit: (optional)
    :attr str frequency: (optional)
    :attr str duration: (optional)
    :attr str dimension: (optional)
    """

    def __init__(self, value=None, unit=None, frequency=None, duration=None, dimension=None, **kwargs):
        """
        Initialize a AttributeValueEntry object.

        :param str value: (optional)
        :param str unit: (optional)
        :param str frequency: (optional)
        :param str duration: (optional)
        :param str dimension: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.value = value
        self.unit = unit
        self.frequency = frequency
        self.duration = duration
        self.dimension = dimension
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    def __getitem__(self, key):
        """This class was originally exposed to users as a dict, so to preserve backwards compatibility,
            we'll make this class function as a dict as well as a class.
        """
        return self.__dict__[key]

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttributeValueEntry object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'value' in _dict:
            args['value'] = _dict['value']
            del xtra['value']
        if 'unit' in _dict:
            args['unit'] = _dict['unit']
            del xtra['unit']
        if 'frequency' in _dict:
            args['frequency'] = _dict['frequency']
            del xtra['frequency']
        if 'duration' in _dict:
            args['duration'] = _dict['duration']
            del xtra['duration']
        if 'dimension' in _dict:
            args['dimension'] = _dict['dimension']
            del xtra['dimension']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'dimension') and self.dimension is not None:
            _dict['dimension'] = self.dimension
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'value', 'unit', 'frequency', 'duration', 'dimension'}
        if not hasattr(self, '_additionalProperties'):
            super(AttributeValueEntry, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(AttributeValueEntry, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this AttributeValueEntry object."""
        return json.dumps(self._to_dict(), indent=2)

class AttributeValueAnnotation(object):
    """
    AttributeValueAnnotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str preferred_name: (optional)
    :attr list[object] values: (optional)
    :attr str source: (optional)
    :attr str source_version: (optional)
    :attr Concept concept: (optional)
    :attr str name: (optional)
    :attr str icd9_code: (optional)
    :attr str icd10_code: (optional)
    :attr str nci_code: (optional)
    :attr str snomed_concept_id: (optional)
    :attr str mesh_id: (optional)
    :attr str rx_norm_id: (optional)
    :attr str loinc_id: (optional)
    :attr str vocabs: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    :attr str cpt_code: (optional)
    :attr Disambiguation disambiguation_data: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, preferred_name=None, values=None, source=None, source_version=None,
                 concept=None, name=None, icd9_code=None, icd10_code=None, nci_code=None, snomed_concept_id=None,
                 mesh_id=None, rx_norm_id=None, loinc_id=None, vocabs=None, section_normalized_name=None,
                 section_surface_form=None, cpt_code=None, disambiguation_data=None, **kwargs):
        """
        Initialize a AttributeValueAnnotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str preferred_name: (optional)
        :param list[object] values: (optional)
        :param str source: (optional)
        :param str source_version: (optional)
        :param Concept concept: (optional)
        :param str name: (optional)
        :param str icd9_code: (optional)
        :param str icd10_code: (optional)
        :param str nci_code: (optional)
        :param str snomed_concept_id: (optional)
        :param str mesh_id: (optional)
        :param str rx_norm_id: (optional)
        :param str loinc_id: (optional)
        :param str vocabs: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param str cpt_code: (optional)
        :param Disambiguation disambiguation_data: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.preferred_name = preferred_name
        self.values = values
        self.source = source
        self.source_version = source_version
        self.concept = concept
        self.name = name
        self.icd9_code = icd9_code
        self.icd10_code = icd10_code
        self.nci_code = nci_code
        self.snomed_concept_id = snomed_concept_id
        self.mesh_id = mesh_id
        self.rx_norm_id = rx_norm_id
        self.loinc_id = loinc_id
        self.vocabs = vocabs
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        self.cpt_code = cpt_code
        self.disambiguation_data = disambiguation_data
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttributeValueAnnotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'preferredName' in _dict:
            args['preferred_name'] = _dict['preferredName']
            del xtra['preferredName']
        if 'values' in _dict:
            args['values'] = [AttributeValueEntry._from_dict(entry) for entry in _dict['values']]
            del xtra['values']
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'sourceVersion' in _dict:
            args['source_version'] = _dict['sourceVersion']
            del xtra['sourceVersion']
        if 'concept' in _dict:
            args['concept'] = Concept._from_dict(_dict['concept'])
            del xtra['concept']
        if 'name' in _dict:
            args['name'] = _dict['name']
            del xtra['name']
        if 'icd9Code' in _dict:
            args['icd9_code'] = _dict['icd9Code']
            del xtra['icd9Code']
        if 'icd10Code' in _dict:
            args['icd10_code'] = _dict['icd10Code']
            del xtra['icd10Code']
        if 'nciCode' in _dict:
            args['nci_code'] = _dict['nciCode']
            del xtra['nciCode']
        if 'snomedConceptId' in _dict:
            args['snomed_concept_id'] = _dict['snomedConceptId']
            del xtra['snomedConceptId']
        if 'meshId' in _dict:
            args['mesh_id'] = _dict['meshId']
            del xtra['meshId']
        if 'rxNormId' in _dict:
            args['rx_norm_id'] = _dict['rxNormId']
            del xtra['rxNormId']
        # Normalize alternative capitalization (rxNormID)
        if 'rxNormID' in _dict:
            args['rx_norm_id'] = _dict['rxNormID']
            del xtra['rxNormID']
        if 'loincId' in _dict:
            args['loinc_id'] = _dict['loincId']
            del xtra['loincId']
        if 'vocabs' in _dict:
            args['vocabs'] = _dict['vocabs']
            del xtra['vocabs']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'cptCode' in _dict:
            args['cpt_code'] = _dict['cptCode']
            del xtra['cptCode']
        if 'disambiguationData' in _dict:
            args['disambiguation_data'] = Disambiguation._from_dict(_dict['disambiguationData'])
            del xtra['disambiguationData']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'preferred_name') and self.preferred_name is not None:
            _dict['preferredName'] = self.preferred_name
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [entry._to_dict() for entry in self.values]
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'source_version') and self.source_version is not None:
            _dict['sourceVersion'] = self.source_version
        if hasattr(self, 'concept') and self.concept is not None:
            _dict['concept'] = self.concept._to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'icd9_code') and self.icd9_code is not None:
            _dict['icd9Code'] = self.icd9_code
        if hasattr(self, 'icd10_code') and self.icd10_code is not None:
            _dict['icd10Code'] = self.icd10_code
        if hasattr(self, 'nci_code') and self.nci_code is not None:
            _dict['nciCode'] = self.nci_code
        if hasattr(self, 'snomed_concept_id') and self.snomed_concept_id is not None:
            _dict['snomedConceptId'] = self.snomed_concept_id
        if hasattr(self, 'mesh_id') and self.mesh_id is not None:
            _dict['meshId'] = self.mesh_id
        if hasattr(self, 'rx_norm_id') and self.rx_norm_id is not None:
            _dict['rxNormId'] = self.rx_norm_id
        if hasattr(self, 'loinc_id') and self.loinc_id is not None:
            _dict['loincId'] = self.loinc_id
        if hasattr(self, 'vocabs') and self.vocabs is not None:
            _dict['vocabs'] = self.vocabs
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'cpt_code') and self.cpt_code is not None:
            _dict['cptCode'] = self.cpt_code
        if hasattr(self, 'disambiguation_data') and self.disambiguation_data is not None:
            _dict['disambiguationData'] = self.disambiguation_data._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'preferred_name',
                       'values', 'source', 'source_version', 'concept', 'name', 'icd9_code', 'icd10_code', 'nci_code',
                       'snomed_concept_id', 'mesh_id', 'rx_norm_id', 'loinc_id', 'vocabs', 'section_normalized_name',
                       'section_surface_form', 'cpt_code', 'disambiguation_data'})
        if not hasattr(self, '_additionalProperties'):
            super(AttributeValueAnnotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(AttributeValueAnnotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this AttributeValueAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)


class CancerDiagnosis(object):
    """
    CancerDiagnosis.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr int cui: (optional)
    :attr str section_normalized_name: (optional)
    :attr str modality: (optional)
    :attr str section_surface_form: (optional)
    :attr Disambiguation disambiguation_data: (optional)
    :attr list[object] cancer: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, cui=None, section_normalized_name=None, modality=None,
                 section_surface_form=None, disambiguation_data=None, cancer=None, **kwargs):
        """
        Initialize a CancerDiagnosis object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param int cui: (optional)
        :param str section_normalized_name: (optional)
        :param str modality: (optional)
        :param str section_surface_form: (optional)
        :param Disambiguation disambiguation_data: (optional)
        :param list[object] cancer: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.cui = cui
        self.section_normalized_name = section_normalized_name
        self.modality = modality
        self.section_surface_form = section_surface_form
        self.disambiguation_data = disambiguation_data
        self.cancer = cancer
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CancerDiagnosis object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'modality' in _dict:
            args['modality'] = _dict['modality']
            del xtra['modality']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'disambiguationData' in _dict:
            args['disambiguation_data'] = Disambiguation._from_dict(_dict['disambiguationData'])
            del xtra['disambiguationData']
        if 'cancer' in _dict:
            args['cancer'] = _dict['cancer']
            del xtra['cancer']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'modality') and self.modality is not None:
            _dict['modality'] = self.modality
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'disambiguation_data') and self.disambiguation_data is not None:
            _dict['disambiguationData'] = self.disambiguation_data._to_dict()
        if hasattr(self, 'cancer') and self.cancer is not None:
            _dict['cancer'] = self.cancer
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'cui',
                       'section_normalized_name', 'modality', 'section_surface_form', 'disambiguation_data', 'cancer'})
        if not hasattr(self, '_additionalProperties'):
            super(CancerDiagnosis, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(CancerDiagnosis, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this CancerDiagnosis object."""
        return json.dumps(self._to_dict(), indent=2)

class SpellingCorrection(object):
    """
    Spelling Correction.

    :attr int begin:
    :attr int end:
    :attr str covered_text:
    :attr list[Suggestion] suggestions
    """
    def __init__(self, begin=None, end=None, covered_text=None, suggestions=None, **kwargs):
        """
        Initializes a spelling correction

        :param int begin:
        :param int end:
        :param str covered_text:
        :param list[Suggestion] suggestions:

        """
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.suggestions = suggestions
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpellingCorrection object from a json dictionary."""
        args = {}
        xtra = _dict.copy()

        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'suggestions' in _dict:
            args['suggestions'] = [Suggestion._from_dict(entry) for entry in _dict['suggestions']]
            del xtra['suggestions']

        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this spelling correction model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'suggestions') and self.suggestions is not None:
            _dict['suggestions'] = [entry._to_dict() for entry in self.suggestions]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'begin', 'end', 'covered_text', 'suggestions'}
        if not hasattr(self, '_additionalProperties'):
            super(SpellingCorrection, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(SpellingCorrection, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Spelling Correction object."""
        return json.dumps(self._to_dict(), indent=2)

class Suggestion(object):
    """
    :attr str text
    :attr float confidence
    :attr bool applied
    :attr list[str] semtypes: (optional)
    """

    def __init__(self, text=None, confidence=None, applied=None, semtypes=None, **kwargs):
        """
        Initializes a spelling suggestion

        :param str text
        :param float confidence
        :param bool applied
        :param list[str] semtypes: (optional)
        """
        self.text = text
        self.confidence = confidence
        self.applied = applied
        self.semtypes = semtypes
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a spelling suggestion object from a json dictionary."""
        args = {}
        xtra = _dict.copy()

        if 'text' in _dict:
            args['text'] = _dict['text']
            del xtra['text']
        if 'confidence' in _dict:
            args['confidence'] = _dict['confidence']
            del xtra['confidence']
        if 'applied' in _dict:
            args['applied'] = _dict['applied']
            del xtra['applied']
        if 'semtypes' in _dict:
            args['semtypes'] = _dict['semtypes']
            del xtra['semtypes']

        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this spelling suggestion."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'applied') and self.applied is not None:
            _dict['applied'] = self.applied
        if hasattr(self, 'semtypes') and self.semtypes is not None:
            _dict['semtypes'] = self.semtypes
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'text', 'confidence', 'applied', 'semtypes'}
        if not hasattr(self, '_additionalProperties'):
            super(Suggestion, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Suggestion, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this spelling suggestion object."""
        return json.dumps(self._to_dict(), indent=2)

class SpellCorrectedText(object):
    """
    :attr str corrected_text
    :attr str debug_text: (optional)
    """
    def __init__(self, corrected_text=None, debug_text=None, **kwargs):
        """
        Initializes a Spell corrected text

        :param str corrected_text
        :param str debug_text: (optional)
        """
        self.corrected_text = corrected_text
        self.debug_text = debug_text
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a spelling corrected text object from a json dictionary."""
        args = {}
        xtra = _dict.copy()

        if 'correctedText' in _dict:
            args['corrected_text'] = _dict['correctedText']
            del xtra['correctedText']
        if 'debugText' in _dict:
            args['debug_text'] = _dict['debugText']
            del xtra['debugText']

        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this spell corrected text"""
        _dict = {}
        if hasattr(self, 'corrected_text') and self.corrected_text is not None:
            _dict['correctedText'] = self.corrected_text
        if hasattr(self, 'debug_text') and self.debug_text is not None:
            _dict['debugText'] = self.debug_text

        return _dict

    def __setattr__(self, name, value):
        properties = {'corrected_text', 'debug_text'}
        if not hasattr(self, '_additionalProperties'):
            super(SpellCorrectedText, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(SpellCorrectedText, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this spelling suggestion object."""
        return json.dumps(self._to_dict(), indent=2)


class Concept(object):
    """
    Concept.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr int cui: (optional)
    :attr str preferred_name: (optional)
    :attr str semantic_type: (optional)
    :attr str source: (optional)
    :attr str source_version: (optional)
    :attr Disambiguation disambiguation_data: (optional)
    :attr str icd9_code: (optional)
    :attr str icd10_code: (optional)
    :attr str nci_code: (optional)
    :attr str snomed_concept_id: (optional)
    :attr str mesh_id: (optional)
    :attr str rx_norm_id: (optional)
    :attr str loinc_id: (optional)
    :attr str vocabs: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    :attr str cpt_code: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, cui=None, preferred_name=None, semantic_type=None, source=None,
                 source_version=None, disambiguation_data=None, icd9_code=None, icd10_code=None, nci_code=None,
                 snomed_concept_id=None, mesh_id=None, rx_norm_id=None, loinc_id=None, vocabs=None,
                 section_normalized_name=None, section_surface_form=None, cpt_code=None, **kwargs):
        """
        Initialize a Concept object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param int cui: (optional)
        :param str preferred_name: (optional)
        :param str semantic_type: (optional)
        :param str source: (optional)
        :param str source_version: (optional)
        :param Disambiguation disambiguation_data: (optional)
        :param str icd9_code: (optional)
        :param str icd10_code: (optional)
        :param str nci_code: (optional)
        :param str snomed_concept_id: (optional)
        :param str mesh_id: (optional)
        :param str rx_norm_id: (optional)
        :param str loinc_id: (optional)
        :param str vocabs: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param str cpt_code: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.cui = cui
        self.preferred_name = preferred_name
        self.semantic_type = semantic_type
        self.source = source
        self.source_version = source_version
        self.disambiguation_data = disambiguation_data
        self.icd9_code = icd9_code
        self.icd10_code = icd10_code
        self.nci_code = nci_code
        self.snomed_concept_id = snomed_concept_id
        self.mesh_id = mesh_id
        self.rx_norm_id = rx_norm_id
        self.loinc_id = loinc_id
        self.vocabs = vocabs
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        self.cpt_code = cpt_code
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Concept object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'preferredName' in _dict:
            args['preferred_name'] = _dict['preferredName']
            del xtra['preferredName']
        if 'semanticType' in _dict:
            args['semantic_type'] = _dict['semanticType']
            del xtra['semanticType']
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'sourceVersion' in _dict:
            args['source_version'] = _dict['sourceVersion']
            del xtra['sourceVersion']
        if 'disambiguationData' in _dict:
            args['disambiguation_data'] = Disambiguation._from_dict(_dict['disambiguationData'])
            del xtra['disambiguationData']
        if 'icd9Code' in _dict:
            args['icd9_code'] = _dict['icd9Code']
            del xtra['icd9Code']
        if 'icd10Code' in _dict:
            args['icd10_code'] = _dict['icd10Code']
            del xtra['icd10Code']
        if 'nciCode' in _dict:
            args['nci_code'] = _dict['nciCode']
            del xtra['nciCode']
        if 'snomedConceptId' in _dict:
            args['snomed_concept_id'] = _dict['snomedConceptId']
            del xtra['snomedConceptId']
        if 'meshId' in _dict:
            args['mesh_id'] = _dict['meshId']
            del xtra['meshId']
        if 'rxNormId' in _dict:
            args['rx_norm_id'] = _dict['rxNormId']
            del xtra['rxNormId']
        # Normalize alternative capitalization (rxNormID)
        if 'rxNormID' in _dict:
            args['rx_norm_id'] = _dict['rxNormID']
            del xtra['rxNormID']
        if 'loincId' in _dict:
            args['loinc_id'] = _dict['loincId']
            del xtra['loincId']
        if 'vocabs' in _dict:
            args['vocabs'] = _dict['vocabs']
            del xtra['vocabs']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'cptCode' in _dict:
            args['cpt_code'] = _dict['cptCode']
            del xtra['cptCode']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'preferred_name') and self.preferred_name is not None:
            _dict['preferredName'] = self.preferred_name
        if hasattr(self, 'semantic_type') and self.semantic_type is not None:
            _dict['semanticType'] = self.semantic_type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'source_version') and self.source_version is not None:
            _dict['sourceVersion'] = self.source_version
        if hasattr(self, 'disambiguation_data') and self.disambiguation_data is not None:
            _dict['disambiguationData'] = self.disambiguation_data._to_dict()
        if hasattr(self, 'icd9_code') and self.icd9_code is not None:
            _dict['icd9Code'] = self.icd9_code
        if hasattr(self, 'icd10_code') and self.icd10_code is not None:
            _dict['icd10Code'] = self.icd10_code
        if hasattr(self, 'nci_code') and self.nci_code is not None:
            _dict['nciCode'] = self.nci_code
        if hasattr(self, 'snomed_concept_id') and self.snomed_concept_id is not None:
            _dict['snomedConceptId'] = self.snomed_concept_id
        if hasattr(self, 'mesh_id') and self.mesh_id is not None:
            _dict['meshId'] = self.mesh_id
        if hasattr(self, 'rx_norm_id') and self.rx_norm_id is not None:
            _dict['rxNormId'] = self.rx_norm_id
        if hasattr(self, 'loinc_id') and self.loinc_id is not None:
            _dict['loincId'] = self.loinc_id
        if hasattr(self, 'vocabs') and self.vocabs is not None:
            _dict['vocabs'] = self.vocabs
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'cpt_code') and self.cpt_code is not None:
            _dict['cptCode'] = self.cpt_code
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'cui',
                       'preferred_name', 'semantic_type', 'source', 'source_version', 'disambiguation_data',
                       'icd9_code', 'icd10_code', 'nci_code', 'snomed_concept_id', 'mesh_id', 'rx_norm_id',
                       'loinc_id', 'vocabs', 'section_normalized_name', 'section_surface_form', 'cpt_code'})
        if not hasattr(self, '_additionalProperties'):
            super(Concept, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Concept, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Concept object."""
        return json.dumps(self._to_dict(), indent=2)


class ConceptValue(object):
    """
    ConceptValue.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr int cui: (optional)
    :attr str dimension: (optional)
    :attr str preferred_name: (optional)
    :attr str trigger: (optional)
    :attr str source: (optional)
    :attr str value: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, cui=None, dimension=None, preferred_name=None, trigger=None, source=None,
                 value=None, section_normalized_name=None, section_surface_form=None, **kwargs):
        """
        Initialize a ConceptValue object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param int cui: (optional)
        :param str dimension: (optional)
        :param str preferred_name: (optional)
        :param str trigger: (optional)
        :param str source: (optional)
        :param str value: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.cui = cui
        self.dimension = dimension
        self.preferred_name = preferred_name
        self.trigger = trigger
        self.source = source
        self.value = value
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptValue object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'dimension' in _dict:
            args['dimension'] = _dict['dimension']
            del xtra['dimension']
        if 'preferredName' in _dict:
            args['preferred_name'] = _dict['preferredName']
            del xtra['preferredName']
        if 'trigger' in _dict:
            args['trigger'] = _dict['trigger']
            del xtra['trigger']
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'value' in _dict:
            args['value'] = _dict['value']
            del xtra['value']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'dimension') and self.dimension is not None:
            _dict['dimension'] = self.dimension
        if hasattr(self, 'preferred_name') and self.preferred_name is not None:
            _dict['preferredName'] = self.preferred_name
        if hasattr(self, 'trigger') and self.trigger is not None:
            _dict['trigger'] = self.trigger
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'cui',
                       'dimension', 'preferred_name', 'trigger', 'source', 'value', 'section_normalized_name',
                       'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(ConceptValue, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(ConceptValue, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this ConceptValue object."""
        return json.dumps(self._to_dict(), indent=2)


class EjectionFractionAnnotation(object):
    """
    EjectionFractionAnnotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str first_value: (optional)
    :attr str ef_alphabetic_value_surface_form: (optional)
    :attr str second_value: (optional)
    :attr str ef_term_surface_form: (optional)
    :attr str ef_suffix_surface_form: (optional)
    :attr str ef_suffix_normalized_name: (optional)
    :attr str ef_alphabetic_value_normalized_name: (optional)
    :attr str ef_term_normalized_name: (optional)
    :attr str is_range: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, first_value=None, ef_alphabetic_value_surface_form=None, second_value=None,
                 ef_term_surface_form=None, ef_suffix_surface_form=None, ef_suffix_normalized_name=None,
                 ef_alphabetic_value_normalized_name=None, ef_term_normalized_name=None, is_range=None,
                 section_normalized_name=None, section_surface_form=None, **kwargs):
        """
        Initialize a EjectionFractionAnnotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str first_value: (optional)
        :param str ef_alphabetic_value_surface_form: (optional)
        :param str second_value: (optional)
        :param str ef_term_surface_form: (optional)
        :param str ef_suffix_surface_form: (optional)
        :param str ef_suffix_normalized_name: (optional)
        :param str ef_alphabetic_value_normalized_name: (optional)
        :param str ef_term_normalized_name: (optional)
        :param str is_range: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.first_value = first_value
        self.ef_alphabetic_value_surface_form = ef_alphabetic_value_surface_form
        self.second_value = second_value
        self.ef_term_surface_form = ef_term_surface_form
        self.ef_suffix_surface_form = ef_suffix_surface_form
        self.ef_suffix_normalized_name = ef_suffix_normalized_name
        self.ef_alphabetic_value_normalized_name = ef_alphabetic_value_normalized_name
        self.ef_term_normalized_name = ef_term_normalized_name
        self.is_range = is_range
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EjectionFractionAnnotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'firstValue' in _dict:
            args['first_value'] = _dict['firstValue']
            del xtra['firstValue']
        if 'efAlphabeticValueSurfaceForm' in _dict:
            args['ef_alphabetic_value_surface_form'] = _dict['efAlphabeticValueSurfaceForm']
            del xtra['efAlphabeticValueSurfaceForm']
        if 'secondValue' in _dict:
            args['second_value'] = _dict['secondValue']
            del xtra['secondValue']
        if 'efTermSurfaceForm' in _dict:
            args['ef_term_surface_form'] = _dict['efTermSurfaceForm']
            del xtra['efTermSurfaceForm']
        if 'efSuffixSurfaceForm' in _dict:
            args['ef_suffix_surface_form'] = _dict['efSuffixSurfaceForm']
            del xtra['efSuffixSurfaceForm']
        if 'efSuffixNormalizedName' in _dict:
            args['ef_suffix_normalized_name'] = _dict['efSuffixNormalizedName']
            del xtra['efSuffixNormalizedName']
        if 'efAlphabeticValueNormalizedName' in _dict:
            args['ef_alphabetic_value_normalized_name'] = _dict['efAlphabeticValueNormalizedName']
            del xtra['efAlphabeticValueNormalizedName']
        if 'efTermNormalizedName' in _dict:
            args['ef_term_normalized_name'] = _dict['efTermNormalizedName']
            del xtra['efTermNormalizedName']
        if 'isRange' in _dict:
            args['is_range'] = _dict['isRange']
            del xtra['isRange']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'first_value') and self.first_value is not None:
            _dict['firstValue'] = self.first_value
        if hasattr(self, 'ef_alphabetic_value_surface_form') and self.ef_alphabetic_value_surface_form is not None:
            _dict['efAlphabeticValueSurfaceForm'] = self.ef_alphabetic_value_surface_form
        if hasattr(self, 'second_value') and self.second_value is not None:
            _dict['secondValue'] = self.second_value
        if hasattr(self, 'ef_term_surface_form') and self.ef_term_surface_form is not None:
            _dict['efTermSurfaceForm'] = self.ef_term_surface_form
        if hasattr(self, 'ef_suffix_surface_form') and self.ef_suffix_surface_form is not None:
            _dict['efSuffixSurfaceForm'] = self.ef_suffix_surface_form
        if hasattr(self, 'ef_suffix_normalized_name') and self.ef_suffix_normalized_name is not None:
            _dict['efSuffixNormalizedName'] = self.ef_suffix_normalized_name
        if hasattr(self, 'ef_alphabetic_value_normalized_name') and self.ef_alphabetic_value_normalized_name is not None:
            _dict['efAlphabeticValueNormalizedName'] = self.ef_alphabetic_value_normalized_name
        if hasattr(self, 'ef_term_normalized_name') and self.ef_term_normalized_name is not None:
            _dict['efTermNormalizedName'] = self.ef_term_normalized_name
        if hasattr(self, 'is_range') and self.is_range is not None:
            _dict['isRange'] = self.is_range
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'first_value',
                       'ef_alphabetic_value_surface_form', 'second_value', 'ef_term_surface_form',
                       'ef_suffix_surface_form', 'ef_suffix_normalized_name', 'ef_alphabetic_value_normalized_name',
                       'ef_term_normalized_name', 'is_range', 'section_normalized_name', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(EjectionFractionAnnotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(EjectionFractionAnnotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this EjectionFractionAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)


class LabValueAnnotation(object):
    """
    LabValueAnnotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str loinc_id: (optional)
    :attr str low_value: (optional)
    :attr str date_in_milliseconds: (optional)
    :attr str lab_type_surface_form: (optional)
    :attr str lab_type_normalized_name: (optional)
    :attr str lab_value: (optional)
    :attr str section_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, loinc_id=None, low_value=None, date_in_milliseconds=None,
                 lab_type_surface_form=None, lab_type_normalized_name=None, lab_value=None,
                 section_normalized_name=None, section_surface_form=None, **kwargs):
        """
        Initialize a LabValueAnnotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str loinc_id: (optional)
        :param str low_value: (optional)
        :param str date_in_milliseconds: (optional)
        :param str lab_type_surface_form: (optional)
        :param str lab_type_normalized_name: (optional)
        :param str lab_value: (optional)
        :param str section_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.loinc_id = loinc_id
        self.low_value = low_value
        self.date_in_milliseconds = date_in_milliseconds
        self.lab_type_surface_form = lab_type_surface_form
        self.lab_type_normalized_name = lab_type_normalized_name
        self.lab_value = lab_value
        self.section_normalized_name = section_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LabValueAnnotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'loincId' in _dict:
            args['loinc_id'] = _dict['loincId']
            del xtra['loincId']
        if 'lowValue' in _dict:
            args['low_value'] = _dict['lowValue']
            del xtra['lowValue']
        if 'dateInMilliseconds' in _dict:
            args['date_in_milliseconds'] = _dict['dateInMilliseconds']
            del xtra['dateInMilliseconds']
        if 'labTypeSurfaceForm' in _dict:
            args['lab_type_surface_form'] = _dict['labTypeSurfaceForm']
            del xtra['labTypeSurfaceForm']
        if 'labTypeNormalizedName' in _dict:
            args['lab_type_normalized_name'] = _dict['labTypeNormalizedName']
            del xtra['labTypeNormalizedName']
        if 'labValue' in _dict:
            args['lab_value'] = _dict['labValue']
            del xtra['labValue']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'loinc_id') and self.loinc_id is not None:
            _dict['loincId'] = self.loinc_id
        if hasattr(self, 'low_value') and self.low_value is not None:
            _dict['lowValue'] = self.low_value
        if hasattr(self, 'date_in_milliseconds') and self.date_in_milliseconds is not None:
            _dict['dateInMilliseconds'] = self.date_in_milliseconds
        if hasattr(self, 'lab_type_surface_form') and self.lab_type_surface_form is not None:
            _dict['labTypeSurfaceForm'] = self.lab_type_surface_form
        if hasattr(self, 'lab_type_normalized_name') and self.lab_type_normalized_name is not None:
            _dict['labTypeNormalizedName'] = self.lab_type_normalized_name
        if hasattr(self, 'lab_value') and self.lab_value is not None:
            _dict['labValue'] = self.lab_value
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'loinc_id', 'low_value', 'date_in_milliseconds', 'lab_type_surface_form',
                       'lab_type_normalized_name', 'lab_value', 'section_normalized_name', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(LabValueAnnotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(LabValueAnnotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this LabValueAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)


class MedicationAnnotation(object):
    """
    MedicationAnnotation.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str section_normalized_name: (optional)
    :attr str cui: (optional)
    :attr list[object] drug: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, section_normalized_name=None, cui=None, drug=None, section_surface_form=None,
                 **kwargs):
        """
        Initialize a MedicationAnnotation object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str section_normalized_name: (optional)
        :param str cui: (optional)
        :param list[object] drug: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.section_normalized_name = section_normalized_name
        self.cui = cui
        self.drug = drug
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MedicationAnnotation object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'drug' in _dict:
            args['drug'] = _dict['drug']
            del xtra['drug']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'drug') and self.drug is not None:
            _dict['drug'] = self.drug
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'section_normalized_name', 'cui', 'drug', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(MedicationAnnotation, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(MedicationAnnotation, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this MedicationAnnotation object."""
        return json.dumps(self._to_dict(), indent=2)


class NegatedSpan(object):
    """
    NegatedSpan.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr object trigger: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, trigger=None, **kwargs):
        """
        Initialize a NegatedSpan object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param object trigger: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.trigger = trigger
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NegatedSpan object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'trigger' in _dict:
            args['trigger'] = _dict['trigger']
            del xtra['trigger']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'trigger') and self.trigger is not None:
            _dict['trigger'] = self.trigger
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'trigger'}
        if not hasattr(self, '_additionalProperties'):
            super(NegatedSpan, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(NegatedSpan, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this NegatedSpan object."""
        return json.dumps(self._to_dict(), indent=2)


class Procedure(object):
    """
    Procedure.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str cui: (optional)
    :attr str section_normalized_name: (optional)
    :attr str date_in_milliseconds: (optional)
    :attr str snomed_concept_id: (optional)
    :attr str procedure_surface_form: (optional)
    :attr str procedure_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    :attr Disambiguation disambiguation_data: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, cui=None, section_normalized_name=None, date_in_milliseconds=None,
                 snomed_concept_id=None, procedure_surface_form=None, procedure_normalized_name=None,
                 section_surface_form=None, disambiguation_data=None, **kwargs):
        """
        Initialize a Procedure object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str cui: (optional)
        :param str section_normalized_name: (optional)
        :param str date_in_milliseconds: (optional)
        :param str snomed_concept_id: (optional)
        :param str procedure_surface_form: (optional)
        :param str procedure_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param Disambiguation disambiguation_data: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.cui = cui
        self.section_normalized_name = section_normalized_name
        self.date_in_milliseconds = date_in_milliseconds
        self.snomed_concept_id = snomed_concept_id
        self.procedure_surface_form = procedure_surface_form
        self.procedure_normalized_name = procedure_normalized_name
        self.section_surface_form = section_surface_form
        self.disambiguation_data = disambiguation_data
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Procedure object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'dateInMilliseconds' in _dict:
            args['date_in_milliseconds'] = _dict['dateInMilliseconds']
            del xtra['dateInMilliseconds']
        if 'snomedConceptId' in _dict:
            args['snomed_concept_id'] = _dict['snomedConceptId']
            del xtra['snomedConceptId']
        if 'procedureSurfaceForm' in _dict:
            args['procedure_surface_form'] = _dict['procedureSurfaceForm']
            del xtra['procedureSurfaceForm']
        if 'procedureNormalizedName' in _dict:
            args['procedure_normalized_name'] = _dict['procedureNormalizedName']
            del xtra['procedureNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'disambiguationData' in _dict:
            args['disambiguation_data'] = Disambiguation._from_dict(_dict['disambiguationData'])
            del xtra['disambiguationData']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'date_in_milliseconds') and self.date_in_milliseconds is not None:
            _dict['dateInMilliseconds'] = self.date_in_milliseconds
        if hasattr(self, 'snomed_concept_id') and self.snomed_concept_id is not None:
            _dict['snomedConceptId'] = self.snomed_concept_id
        if hasattr(self, 'procedure_surface_form') and self.procedure_surface_form is not None:
            _dict['procedureSurfaceForm'] = self.procedure_surface_form
        if hasattr(self, 'procedure_normalized_name') and self.procedure_normalized_name is not None:
            _dict['procedureNormalizedName'] = self.procedure_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'disambiguation_data') and self.disambiguation_data is not None:
            _dict['disambiguationData'] = self.disambiguation_data._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'cui',
                       'section_normalized_name', 'date_in_milliseconds', 'snomed_concept_id', 'procedure_surface_form',
                       'procedure_normalized_name', 'section_surface_form', 'disambiguation_data'})
        if not hasattr(self, '_additionalProperties'):
            super(Procedure, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Procedure, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Procedure object."""
        return json.dumps(self._to_dict(), indent=2)


class Smoking(object):
    """
    Smoking.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str participation: (optional)
    :attr str section_normalized_name: (optional)
    :attr str modality: (optional)
    :attr str current: (optional)
    :attr str smoke_term_surface_form: (optional)
    :attr str smoke_term_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, participation=None, section_normalized_name=None, modality=None, current=None,
                 smoke_term_surface_form=None, smoke_term_normalized_name=None, section_surface_form=None, **kwargs):
        """
        Initialize a Smoking object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str participation: (optional)
        :param str section_normalized_name: (optional)
        :param str modality: (optional)
        :param str current: (optional)
        :param str smoke_term_surface_form: (optional)
        :param str smoke_term_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.participation = participation
        self.section_normalized_name = section_normalized_name
        self.modality = modality
        self.current = current
        self.smoke_term_surface_form = smoke_term_surface_form
        self.smoke_term_normalized_name = smoke_term_normalized_name
        self.section_surface_form = section_surface_form
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Smoking object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'participation' in _dict:
            args['participation'] = _dict['participation']
            del xtra['participation']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'modality' in _dict:
            args['modality'] = _dict['modality']
            del xtra['modality']
        if 'current' in _dict:
            args['current'] = _dict['current']
            del xtra['current']
        if 'smokeTermSurfaceForm' in _dict:
            args['smoke_term_surface_form'] = _dict['smokeTermSurfaceForm']
            del xtra['smokeTermSurfaceForm']
        if 'smokeTermNormalizedName' in _dict:
            args['smoke_term_normalized_name'] = _dict['smokeTermNormalizedName']
            del xtra['smokeTermNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'participation') and self.participation is not None:
            _dict['participation'] = self.participation
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'modality') and self.modality is not None:
            _dict['modality'] = self.modality
        if hasattr(self, 'current') and self.current is not None:
            _dict['current'] = self.current
        if hasattr(self, 'smoke_term_surface_form') and self.smoke_term_surface_form is not None:
            _dict['smokeTermSurfaceForm'] = self.smoke_term_surface_form
        if hasattr(self, 'smoke_term_normalized_name') and self.smoke_term_normalized_name is not None:
            _dict['smokeTermNormalizedName'] = self.smoke_term_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical',
                       'participation', 'section_normalized_name', 'modality', 'current',
                       'smoke_term_surface_form', 'smoke_term_normalized_name', 'section_surface_form'})
        if not hasattr(self, '_additionalProperties'):
            super(Smoking, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Smoking, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Smoking object."""
        return json.dumps(self._to_dict(), indent=2)


class SymptomDisease(object):
    """
    SymptomDisease.

    :attr str id: (optional)
    :attr str type: (optional)
    :attr int uid: (optional)
    :attr int begin: (optional)
    :attr int end: (optional)
    :attr str covered_text: (optional)
    :attr bool negated: (optional)
    :attr bool hypothetical: (optional)
    :attr str cui: (optional)
    :attr str icd10_code: (optional)
    :attr str section_normalized_name: (optional)
    :attr str modality: (optional)
    :attr str symptom_disease_surface_form: (optional)
    :attr str date_in_milliseconds: (optional)
    :attr str snomed_concept_id: (optional)
    :attr str ccs_code: (optional)
    :attr str symptom_disease_normalized_name: (optional)
    :attr str section_surface_form: (optional)
    :attr str icd9_code: (optional)
    :attr str hcc_code: (optional)
    :attr Disambiguation disambiguation_data: (optional)
    """

    def __init__(self, id=None, type=None, uid=None, begin=None, end=None, covered_text=None, negated=None,
                 hypothetical=None, cui=None, icd10_code=None, section_normalized_name=None, modality=None,
                 symptom_disease_surface_form=None, date_in_milliseconds=None, snomed_concept_id=None, ccs_code=None,
                 symptom_disease_normalized_name=None, section_surface_form=None, icd9_code=None, hcc_code=None,
                 disambiguation_data=None, **kwargs):
        """
        Initialize a SymptomDisease object.

        :param str id: (optional)
        :param str type: (optional)
        :param int uid: (optional)
        :param int begin: (optional)
        :param int end: (optional)
        :param str covered_text: (optional)
        :param bool negated: (optional)
        :param bool hypothetical: (optional)
        :param str cui: (optional)
        :param str icd10_code: (optional)
        :param str section_normalized_name: (optional)
        :param str modality: (optional)
        :param str symptom_disease_surface_form: (optional)
        :param str date_in_milliseconds: (optional)
        :param str snomed_concept_id: (optional)
        :param str ccs_code: (optional)
        :param str symptom_disease_normalized_name: (optional)
        :param str section_surface_form: (optional)
        :param str icd9_code: (optional)
        :param str hcc_code: (optional)
        :param Disambiguation disambiguation_data: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.type = type
        self.uid = uid
        self.begin = begin
        self.end = end
        self.covered_text = covered_text
        self.negated = negated
        self.hypothetical = hypothetical
        self.cui = cui
        self.icd10_code = icd10_code
        self.section_normalized_name = section_normalized_name
        self.modality = modality
        self.symptom_disease_surface_form = symptom_disease_surface_form
        self.date_in_milliseconds = date_in_milliseconds
        self.snomed_concept_id = snomed_concept_id
        self.ccs_code = ccs_code
        self.symptom_disease_normalized_name = symptom_disease_normalized_name
        self.section_surface_form = section_surface_form
        self.icd9_code = icd9_code
        self.hcc_code = hcc_code
        self.disambiguation_data = disambiguation_data
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SymptomDisease object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict['id']
            del xtra['id']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'negated' in _dict:
            args['negated'] = _dict['negated']
            del xtra['negated']
        if 'hypothetical' in _dict:
            args['hypothetical'] = _dict['hypothetical']
            del xtra['hypothetical']
        if 'cui' in _dict:
            args['cui'] = _dict['cui']
            del xtra['cui']
        if 'icd10Code' in _dict:
            args['icd10_code'] = _dict['icd10Code']
            del xtra['icd10Code']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'modality' in _dict:
            args['modality'] = _dict['modality']
            del xtra['modality']
        if 'symptomDiseaseSurfaceForm' in _dict:
            args['symptom_disease_surface_form'] = _dict['symptomDiseaseSurfaceForm']
            del xtra['symptomDiseaseSurfaceForm']
        if 'dateInMilliseconds' in _dict:
            args['date_in_milliseconds'] = _dict['dateInMilliseconds']
            del xtra['dateInMilliseconds']
        if 'snomedConceptId' in _dict:
            args['snomed_concept_id'] = _dict['snomedConceptId']
            del xtra['snomedConceptId']
        if 'ccsCode' in _dict:
            args['ccs_code'] = _dict['ccsCode']
            del xtra['ccsCode']
        if 'symptomDiseaseNormalizedName' in _dict:
            args['symptom_disease_normalized_name'] = _dict['symptomDiseaseNormalizedName']
            del xtra['symptomDiseaseNormalizedName']
        if 'sectionSurfaceForm' in _dict:
            args['section_surface_form'] = _dict['sectionSurfaceForm']
            del xtra['sectionSurfaceForm']
        if 'icd9Code' in _dict:
            args['icd9_code'] = _dict['icd9Code']
            del xtra['icd9Code']
        if 'hccCode' in _dict:
            args['hcc_code'] = _dict['hccCode']
            del xtra['hccCode']
        if 'disambiguationData' in _dict:
            args['disambiguation_data'] = Disambiguation._from_dict(_dict['disambiguationData'])
            del xtra['disambiguationData']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'negated') and self.negated is not None:
            _dict['negated'] = self.negated
        if hasattr(self, 'hypothetical') and self.hypothetical is not None:
            _dict['hypothetical'] = self.hypothetical
        if hasattr(self, 'cui') and self.cui is not None:
            _dict['cui'] = self.cui
        if hasattr(self, 'icd10_code') and self.icd10_code is not None:
            _dict['icd10Code'] = self.icd10_code
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'modality') and self.modality is not None:
            _dict['modality'] = self.modality
        if hasattr(self, 'symptom_disease_surface_form') and self.symptom_disease_surface_form is not None:
            _dict['symptomDiseaseSurfaceForm'] = self.symptom_disease_surface_form
        if hasattr(self, 'date_in_milliseconds') and self.date_in_milliseconds is not None:
            _dict['dateInMilliseconds'] = self.date_in_milliseconds
        if hasattr(self, 'snomed_concept_id') and self.snomed_concept_id is not None:
            _dict['snomedConceptId'] = self.snomed_concept_id
        if hasattr(self, 'ccs_code') and self.ccs_code is not None:
            _dict['ccsCode'] = self.ccs_code
        if hasattr(self, 'symptom_disease_normalized_name') and self.symptom_disease_normalized_name is not None:
            _dict['symptomDiseaseNormalizedName'] = self.symptom_disease_normalized_name
        if hasattr(self, 'section_surface_form') and self.section_surface_form is not None:
            _dict['sectionSurfaceForm'] = self.section_surface_form
        if hasattr(self, 'icd9_code') and self.icd9_code is not None:
            _dict['icd9Code'] = self.icd9_code
        if hasattr(self, 'hcc_code') and self.hcc_code is not None:
            _dict['hccCode'] = self.hcc_code
        if hasattr(self, 'disambiguation_data') and self.disambiguation_data is not None:
            _dict['disambiguationData'] = self.disambiguation_data._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = ({'id', 'type', 'uid', 'begin', 'end', 'covered_text', 'negated', 'hypothetical', 'cui',
                       'icd10_code', 'section_normalized_name', 'modality', 'symptom_disease_surface_form',
                       'date_in_milliseconds', 'snomed_concept_id', 'ccs_code', 'symptom_disease_normalized_name',
                       'section_surface_form', 'icd9_code', 'hcc_code', 'disambiguation_data'})
        if not hasattr(self, '_additionalProperties'):
            super(SymptomDisease, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(SymptomDisease, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this SymptomDisease object."""
        return json.dumps(self._to_dict(), indent=2)

class SectionTrigger(object):
    """
    SectionTrigger.

    :attr int begin: (optional)
    :attr str covered_text: (optional)
    :attr int end: (optional)
    :attr str section_normalized_name: (optional)
    :attr str source: (optional)
    :attr str type: (optional)
    """

    def __init__(self, begin=None, covered_text=None, end=None, section_normalized_name=None, source=None,
                 type=None, **kwargs):
        """
        Initialize a SectionTrigger object.

        :param int begin: (optional)
        :param str covered_text: (optional)
        :param int end: (optional)
        :param str section_normalized_name: (optional)
        :param str source: (optional)
        :param str type: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.begin = begin
        self.covered_text = covered_text
        self.end = end
        self.section_normalized_name = section_normalized_name
        self.source = source
        self.type = type
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SectionTrigger object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'sectionNormalizedName' in _dict:
            args['section_normalized_name'] = _dict['sectionNormalizedName']
            del xtra['sectionNormalizedName']
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'section_normalized_name') and self.section_normalized_name is not None:
            _dict['sectionNormalizedName'] = self.section_normalized_name
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'begin', 'covered_text', 'end', 'section_normalized_name', 'source', 'type'}
        if not hasattr(self, '_additionalProperties'):
            super(SectionTrigger, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(SectionTrigger, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this SectionTrigger object."""
        return json.dumps(self._to_dict(), indent=2)


class Section(object):
    """
    Section.

    :attr int begin: (optional)
    :attr str covered_text: (optional)
    :attr int end: (optional)
    :attr str type: (optional)
    :attr str section_type: (optional)
    :attr SectionTrigger trigger: (optional)
    """

    def __init__(self, begin=None, covered_text=None, end=None, type=None, section_type=None, trigger=None, **kwargs):
        """
        Initialize a Section object.

        :param int begin: (optional)
        :param str covered_text: (optional)
        :param int end: (optional)
        :param str type: (optional)
        :param str section_type: (optional)
        :param SectionTrigger trigger: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.begin = begin
        self.covered_text = covered_text
        self.end = end
        self.type = type
        self.section_type = section_type
        self.trigger = trigger
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Section object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'sectionType' in _dict:
            args['section_type'] = _dict['sectionType']
            del xtra['sectionType']
        if 'trigger' in _dict:
            args['trigger'] = SectionTrigger._from_dict(_dict['trigger'])
            del xtra['trigger']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'section_type') and self.section_type is not None:
            _dict['sectionType'] = self.section_type
        if hasattr(self, 'trigger') and self.trigger is not None:
            _dict['trigger'] = self.trigger._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'begin', 'covered_text', 'end', 'type', 'section_type', 'trigger'}
        if not hasattr(self, '_additionalProperties'):
            super(Section, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Section, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Section object."""
        return json.dumps(self._to_dict(), indent=2)

class NluEntities(object):
    """
    NLU Entities.

    :attr int begin: (optional)
    :attr str covered_text: (optional)
    :attr int end: (optional)
    :attr str type: (optional)
    :attr str source: (optional)
    :attr float relevance: (optional)
    :attr int uid
    """

    def __init__(self, begin=None, covered_text=None, end=None, type=None, source=None, relevance=None,
                 uid=None, **kwargs):
        """
        Initialize an NLU Entities object.

        :param int begin: (optional)
        :param str covered_text: (optional)
        :param int end: (optional)
        :param str type: (optional)
        :param str source: (optional)
        :param float relevance: (optional)
        :param int uid: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.begin = begin
        self.covered_text = covered_text
        self.end = end
        self.type = type
        self.source = source
        self.relevance = relevance
        self.uid = uid
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize an NLU Entities object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'begin' in _dict:
            args['begin'] = _dict['begin']
            del xtra['begin']
        if 'coveredText' in _dict:
            args['covered_text'] = _dict['coveredText']
            del xtra['coveredText']
        if 'end' in _dict:
            args['end'] = _dict['end']
            del xtra['end']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'relevance' in _dict:
            args['relevance'] = _dict['relevance']
            del xtra['relevance']
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'covered_text') and self.covered_text is not None:
            _dict['coveredText'] = self.covered_text
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'begin', 'covered_text', 'end', 'type', 'source', 'relevance', 'uid'}
        if not hasattr(self, '_additionalProperties'):
            super(NluEntities, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(NluEntities, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this NluEntities object."""
        return json.dumps(self._to_dict(), indent=2)

class NodeEntity(object):
    """
    NLU Relations Node Entity.

    :attr int uid: (optional)
    """

    def __init__(self, uid, **kwargs):
        """
        Initialize a NLU Relations Node Entity object.

        :param int uid: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.uid = uid
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize an NLU Relations Node Entity object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'uid' in _dict:
            args['uid'] = _dict['uid']
            del xtra['uid']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'uid'}
        if not hasattr(self, '_additionalProperties'):
            super(Node, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Node, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this NLU Relations Node Entity object."""
        return json.dumps(self._to_dict(), indent=2)

class Node(object):
    """
    NLU Relations Node.

    :attr NodeEntity entity: (optional)
    """

    def __init__(self, entity, **kwargs):
        """
        Initialize a NLU Relations Node object.

        :param NodeEntity entity: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.entity = entity
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize an NLU Relations Node  object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'entity' in _dict:
            args['entity'] = _dict['entity']
            del xtra['entity']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'entity'}
        if not hasattr(self, '_additionalProperties'):
            super(Node, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Node, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this NLU Relations Node object."""
        return json.dumps(self._to_dict(), indent=2)

class Relations(object):
    """
    NLU Relations.

    :attr str source: (optional)
    :attr float score: (optional)
    :attr list[Node] nodes: (optional)
    :attr str type: (optional)
    """

    def __init__(self, source=None, score=None, nodes=None, type=None, **kwargs):
        """
        Initialize an NLU Relations object.

        :param str source: (optional)
        :param float score: (optional)
        :param list[Node] nodes: (optional)
        :param str type: (optional)
        :param **kwargs: (optional) Any additional properties.
        """
        self.source = source
        self.score = score
        self.nodes = nodes
        self.type = type
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize an NLU Relations object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'source' in _dict:
            args['source'] = _dict['source']
            del xtra['source']
        if 'score' in _dict:
            args['score'] = _dict['score']
            del xtra['score']
        if 'nodes' in _dict:
            args['nodes'] = [Node._from_dict(entry) for entry in _dict['nodes']]
            del xtra['nodes']
        if 'type' in _dict:
            args['type'] = _dict['type']
            del xtra['type']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'nodes') and self.nodes is not None:
            _dict['nodes'] = [entry._to_dict() for entry in self.nodes]
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'source', 'score', 'nodes', 'type'}
        if not hasattr(self, '_additionalProperties'):
            super(Relations, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Relations, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Relations object."""
        return json.dumps(self._to_dict(), indent=2)
