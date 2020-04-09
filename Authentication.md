# Authentication

The whcs-python-sdk project supports the following types of authentication:
- Identity and Access Management (IAM)

The apikey for your service can be found by clicking the service instance of the resources list in the IBM Cloud dashboard.

## programming examples
```python
import ibm_whcs_sdk.annotator_for_clincial_data as acd


Service = acd('my_service_url', 'my_apikey', 'api_version')
```

```python
import ibm_whcs_sdk.insights_for_medical_literature as iml


Service = iml.InsightsFOrMedicalLiteratureServiceV1('my_service_url', 'my_apikey', 'api_version')
```
