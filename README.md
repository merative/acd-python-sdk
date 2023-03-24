
# Merative Annotator for Clinical Data Python SDK Version 2.0.0

## Overview

This Python SDK allows developers to programmatically interact with the following service:

| Service Name | Imported Class Name |
|--------------|-------------|
| [Annotator for Clinical Data](https://merative.github.io/acd-containers/) | AnnotatorForClinicalDataV1 |

## Prerequisites

* Refer to the Annotation for Clinical Data documentation:
  * [Prerequisites](https://merative.github.io/acd-containers/installing/prereqs/)
  * [Software Development Kits](https://merative.github.io/acd-containers/usage/sdks/)
* Python 3.7 or above

## Installation

To install, use `pip`

```bash
pip install --upgrade acd-sdk
```

## Migrating from version 1.x.x

The 2.0 release of the Annotator for Clinical Data SDK introduces a Python package name change from `ibm_whcs_sdk` to `acd_sdk`.  For the migration from 1.x.x:

1. After running `pip install --upgrade acd-sdk`, confirm that you have version 2.0 installed by running `pip show acd-sdk`.
2. In your application files that have a dependency on `acd-sdk`, update any import declarations from `ibm_whcs_sdk` to `acd_sdk`.  

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

## Questions

For questions, refer to:
  * [Annotator for Clinical Data documentation](https://merative.github.io/acd-containers/)
  * [Annotator for Clinical Data Support page](https://merative.github.io/acd-containers/support/support/)

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/merative/whcs-python-sdk/issues).

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

The Annotator for Clinical Data Python SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE.md).
