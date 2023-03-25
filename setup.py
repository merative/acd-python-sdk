# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys
import pkg_resources

__version__ = '2.0.1'
PACKAGE_NAME = 'acd_sdk'
PACKAGE_DESC = 'This is the Annotator for Clinical Data Python SDK',

with open('requirements.txt') as f:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(f)]
with open('requirements-dev.txt') as f:
    tests_require = [str(req) for req in pkg_resources.parse_requirements(f)]

if sys.argv[-1] == 'publish':
    # test server
    os.system('python setup.py register -r pypitest')
    os.system('python setup.py sdist upload -r pypitest')

    # production server
    os.system('python setup.py register -r pypi')
    os.system('python setup.py sdist upload -r pypi')
    sys.exit()


with open("README.md", "r") as fh:
    readme = fh.read()

setup(name=PACKAGE_NAME.replace('_', '-'),
      version=__version__,
      description=PACKAGE_DESC,
      license='Apache 2.0',
      install_requires=install_requires,
      tests_require=tests_require,
      author='Merative',
      author_email='acddev@merative.com',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/Merative/whcs-python-sdk',
      packages=find_packages(),
      include_package_data=True,
      keywords='PACKAGE_NAME',
      classifiers=[
           'Programming Language :: Python',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 3.7',
           'Programming Language :: Python :: 3.8',
           'Programming Language :: Python :: 3.9',
           'Programming Language :: Python :: 3.10',
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: Apache Software License',
           'Operating System :: OS Independent',
           'Topic :: Software Development :: Libraries :: Python Modules',
           'Topic :: Software Development :: Libraries :: Application Frameworks',
      ],
      zip_safe=True
    )
