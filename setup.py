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


from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys
import pkg_resources

__version__ = '0.0.4'
PACKAGE_NAME = 'ibm_whcs_sdk'

#with open('requirements.txt') as f:
#    install_requires = [str(req) for req in pkg_resources.parse_requirements(f)]
#with open('requirements-dev.txt') as f:
#    tests_require = [str(req) for req in pkg_resources.parse_requirements(f)]

if sys.argv[-1] == 'publish':
    # test server
    os.system('python setup.py register -r pypitest')
    os.system('python setup.py sdist upload -r pypitest')

    # production server
    os.system('python setup.py register -r pypi')
    os.system('python setup.py sdist upload -r pypi')
    sys.exit()


# Convert README.md to README.rst for pypi
try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

    # read_md = lambda f: convert(f, 'rst')
except:
    print('warning: pypandoc module not found, '
          'could not convert Markdown to RST')

    def read_md(f):
        return open(f, 'rb').read().decode(encoding='utf-8')
    # read_md = lambda f: open(f, 'rb').read().decode(encoding='utf-8')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests/integration']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

class PyTestUnit(PyTest):
    def finalize_options(self):
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests/unit']

class PyTestIntegration(PyTest):
    def finalize_options(self):
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests/integration']

setup(name=PACKAGE_NAME,
      version=__version__,
      description='This is the Watson Health Cognitive Services Python SDK containing ACD and IML',
      license='Apache 2.0',
      install_requires=['requests>=2.0,<3.0', 'python_dateutil>=2.5.3', 'websocket_client>=0.48.0', 'ibm_cloud_sdk_core>=1.7.1'],
      tests_require=['pytest', 'responses', 'pylint', 'tox', 'coverage', 'codecov', 'pytest-cov', 'bumpversion'],
      cmdclass={'test': PyTest, 'test_unit': PyTestUnit, 'test_integration': PyTestIntegration},
      author='IBM',
      author_email='dcweber@us.ibm.com',
      long_description=read_md('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/IBM/whcs-python-sdk',
      packages=find_packages(),
      include_package_data=True,
      keywords='',
      classifiers=[
           'Programming Language :: Python',
           'Programming Language :: Python :: 3',
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: Apache Software License',
           'Operating System :: OS Independent',
           'Topic :: Software Development :: Libraries :: Python Modules',
           'Topic :: Software Development :: Libraries :: Application '
           'Frameworks',
      ],
      zip_safe=True
    )
