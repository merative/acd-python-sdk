# Questions

If you are having problems using the SDK or have a question about the Annotator for Clinical Data service,
refer here:
* [README](README.md)
* [Annotator for Clinical Data documentation](https://merative.github.io/acd-containers/)
* [Annotator for Clinical Data Support page](https://merative.github.io/acd-containers/support/support/)

# Issues

If you encounter an issue with the project, you are welcome to submit a 
[bug report](https://github.com/merative/whcs-python-sdk/issues).

# Contributing in General

Our project welcomes external contributions.

To contribute code or documentation, please submit a [pull request](https://github.com/merative/acd-python-sdk/pulls).

A good way to familiarize yourself with the codebase and contribution process is
to look for and tackle low-hanging fruit in the [issue tracker](https://github.com/merative/acd-python-sdk/issues).
Before embarking on a more ambitious contribution, please reach out to acddev@merative.com.

**Note: We appreciate your effort, and want to avoid a situation where a contribution
requires extensive rework (by you or by us), sits in backlog for a long time, or
cannot be accepted at all!**

## Proposing new features

If you would like to implement a new feature, please [raise an issue](https://github.com/merative/acd-python-sdk/issues)
before sending a pull request so the feature can be discussed. This is to avoid
you wasting your valuable time working on a feature that the project developers
are not interested in accepting into the code base.

## Fixing bugs

If you would like to fix a bug, please [raise an issue](https://github.com/merative/acd-python-sdk/issues) before sending a
pull request so it can be tracked.

## Coding style

This SDK follows a coding style based on the [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/),
with the following modifications:
- four spaces instead of tabs for indentation

All non-trivial methods should have docstrings.
Docstrings should follow the [PEP257 guidelines](https://www.python.org/dev/peps/pep-0257/).
For more examples, see the [Google style guide](https://google.github.io/styleguide/pyguide.html#381-docstrings)
regarding docstrings.

Use [PyLint](https://www.pylint.org/) to adhere to these guidelines.

## Commit messages

Commit messages should follow the [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-guidelines).
This is because our release tool - [semantic-release](https://github.com/semantic-release/semantic-release) -
uses this format for determining release versions and generating changelogs.
Tools such as [commitizen](https://github.com/commitizen/cz-cli) or [commitlint](https://github.com/conventional-changelog/commitlint)
can be used to help contributors and enforce commit messages.

Here are some examples of acceptable commit messages, along with the release type that would be done based on the commit message:

| Commit message                                                                                                                                                              | Release type               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| `fix(<optional scope>): <fix message details>`                                                                                                 | ~~Patch~~ Fix Release      |
| `feat(<optional scope>): <feature message details>`                                                                                            | ~~Minor~~ Feature Release  |
| `feat(<optional scope>): <feature message details>`<br><br>`BREAKING CHANGE: <message details>`                                                | ~~Major~~ Breaking Release <br/> (Note that the `BREAKING CHANGE: ` token must be in the footer of the commit) |

## Pull requests

If you want to contribute to the repository, here's a quick guide:
  1. Fork the repository and clone your fork to your local environment
  2. (recommended) Install and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html):
     * `python -m venv <venv-dir>`, where `<venv-dir>` indicates where to install the virtual environment
     * `. <venv-dir>/bin/activate`
  3. Install the project as an editable package using the current source:
     * `python -m pip install -e .`
  4. Install dependencies:
      * `python -m pip install -r requirements.txt`
      * `python -m pip install -r requirements-dev.txt`
  5. Develop and test your code changes:
      * Please add one or more tests to validate your changes.
      * To run all the tests: `python -m pytest`
      * You can find more details about running the tests below.
  6. Check and fix code style: `./pylint.sh`
  7. Make sure everything builds/tests cleanly
  8. Commit your changes
     * Make sure your commit messages follow the Angular Commit Message Guidelines (see below).
  9. Push to your fork and submit a pull request to the **main** branch

## Running the Tests

To run all of the tests (both unit and integration tests):
* `python -m pytest`

Note that integration tests require credentials - see below.

You can run a specific test like this:
* `python -m pytest <path-to-test>/mytest.py`

### Unit tests

Unit tests use a mock service endpoint, so they do not need any credentials.
To run the unit tests:
* `python -m pytest test/unit`

### Integration tests
Integration tests use an actual service endpoint, so you need to provide credentials to the integration test framework.

To run only the integration tests:
* `python -m pytest test/integration`

To provide credentials for the integration tests, add credentials to your ACD Python SDK installation's <your_install_path>/acd-sdk/annotator_for_clinical_data/tests/config.ini file.  Configure your credentials based on your Anotator for Clinical Data service authentication method.

If using IAM authentication:

```
[settings]
base_url = <your ACD endpoint URL>
key = <your ACD endpoint API key>
iam_url = <optional>
version = <ACD API version YYYY-MM-DD>
bearer_token =
disable_ssl = <True or False (False is recommended)>
flow = <optional name of ACD flow persisted to your ACD endpoint>
profile = <optional name of ACD profile persisted to your ACD endpoint>
```

If using Bearer Token authentication:

```
[settings] 
base_url = <your ACD endpoint URL> 
key =
iam_url =
bearer_token = <your ACD endpoint bearer token>
version = <ACD API version YYYY-MM-DD>
disable_ssl = <True or False (False is recommended)>
flow = <optional name of ACD flow persisted to your ACD endpoint>
profile = <optional name of ACD profile persisted to your ACD endpoint>
```

## Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
   have the right to submit it under the open source license
   indicated in the file; or

(b) The contribution is based upon previous work that, to the best
   of my knowledge, is covered under an appropriate open source
   license and I have the right under that license to submit that
   work with modifications, whether created in whole or in part
   by me, under the same open source license (unless I am
   permitted to submit under a different license), as indicated
   in the file; or

(c) The contribution was provided directly to me by some other
   person who certified (a), (b) or (c) and I have not modified
   it.

(d) I understand and agree that this project and the contribution
   are public and that a record of the contribution (including all
   personal information I submit with it, including my sign-off) is
   maintained indefinitely and may be redistributed consistent with
   this project or the open source license(s) involved.
