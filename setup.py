# encoding: utf-8

import os.path
from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

# Package data
# ------------

_name            = 'dr.who'
_version         = '0.0.0'
_description     = 'Package Reservation'
_url             = 'http://pypi.python.org/pypi/dr.who'
_author          = 'Sean Kelly'
_authorEmail     = 'kelly@seankelly.biz'
_maintainer      = 'Sean Kelly'
_maintainerEmail = 'kelly@seankelly.biz'
_license         = 'ALv2'
_namespaces      = ['dr']
_zipSafe         = True
_keywords        = 'placeholder'
_testSuite       = 'dr.who.tests.test_suite'
_entryPoints     = {}
_requirements    = ['setuptools']
_extras          = {'test': []}
_classifiers     = [
    'Development Status :: 1 - Planning',
    'Environment :: Other Environment',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
]

# Setup Metadata
# --------------

def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDescription = _header + '\n\n' + _read('README.rst') + '\n\n' + _read('docs', 'INSTALL.txt') + '\n\n' \
    + _read('docs', 'HISTORY.txt') + '\n\n' + _read('docs', 'LICENSE.txt')
open('doc.txt', 'w').write(_longDescription)

setup(
    author=_author,
    author_email=_authorEmail,
    classifiers=_classifiers,
    description=_description,
    entry_points=_entryPoints,
    extras_require=_extras,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_longDescription,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages('src', exclude=['ez_setup', 'distribute_setup', 'bootstrap']),
    package_dir={'': 'src'},
    url=_url,
    version=_version,
    zip_safe=_zipSafe,
)
