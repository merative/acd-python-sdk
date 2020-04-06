[![Build Status](https://travis.ibm.com/ibmcloud/platform-services-java-sdk.svg?token=eW5FVD71iyte6tTby8gr&branch=master)](https://travis.ibm.com/ibmcloud/platform-services-java-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# Watson Health Cognitive Services Python SDK Version 0.0.4

The IBM Watson Health Cognitive Services (WHCS) Python SDK allows developers to programmaticlly interact with the following WHCS services:

| Service Name | Artifact Id |
|--------------|-------------|
| [Annotator for Clinical data](https://cloud.ibm.com/apidocs/wh-acd) | annotator_for_clinical_data |
| [Insights for Medical Literature](https://cloud.ibm.com/apidocs/wh-iml) | insights_for_medical_literature |

NOTE:  You must be signed in to IBM Cloud to see the docs.

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

An [IBM Cloud](ibm-cloud-onboarding) account.
An IAM API key to allow the SDK to access your provisioned service instance.
Python 3.5 or above

## Installation

To install, use `pip`

```bash
pip install --upgrade ibm-whcs-sdk
```

## Authentication
The ibm-whcs-sdk project supports the following types of authentication:
- Identity and Access Management (IAM)

For more information about how to use authentication with your services click [here](Authentication.md)

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

## Examples
For SDK usage examples, please see the service API documentation.  There are code examples and sample responses for each service API
- [Annotator for Clinical data](https://cloud.ibm.com/apidocs/wh-acd)
- [Insights for Medical Literature](https://cloud.ibm.com/apidocs/wh-iml)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at [IBM Watson Health Support](https://ibmwatsonhealth.force.com/mysupport/s/)of [Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/whcs-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Logging

### Enable logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This would show output of the form:
```
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): iam.cloud.ibm.com:443
DEBUG:urllib3.connectionpool:https://iam.cloud.ibm.com:443 "POST /identity/token HTTP/1.1" 200 1809
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): gateway.watsonplatform.net:443
DEBUG:urllib3.connectionpool:https://gateway.watsonplatform.net:443 "POST /assistant/api/v1/workspaces?version=2018-07-10 HTTP/1.1" 201 None
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): gateway.watsonplatform.net:443
DEBUG:urllib3.connectionpool:https://gateway.watsonplatform.net:443 "GET /assistant/api/v1/workspaces/883a2a44-eb5f-4b1a-96b0-32a90b475ea8?version=2018-07-10&export=true HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): gateway.watsonplatform.net:443
DEBUG:urllib3.connectionpool:https://gateway.watsonplatform.net:443 "DELETE /assistant/api/v1/workspaces/883a2a44-eb5f-4b1a-96b0-32a90b475ea8?version=2018-07-10 HTTP/1.1" 200 28
```

### Low level request and response dump
To get low level information of the requests/ responses:

```python
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
```

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

The IBM Cloud MySDK Java SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).