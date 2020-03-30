# Authentication

The whcs-python-sdk project supports the following types of authentication:
- Identity and Access Management (IAM)

The apikey for your service can be found by clicking the service instance of the resources list in the IBM Cloud dashboard.

## programming examples
```python
import watson_health_cognitive_services as whys


Service = whcs.AnnotatorForClinicalDataV1('my_service_url', 'my_apikey', 'api_version')
```

```python
import watson_health_cognitive_services as whys


Service = whcs.InsightsFOrMedicalLiteratureServiceV1('my_service_url', 'my_apikey', 'api_version')
```