# encoding: utf-8
# See http://packages.python.org/distribute/setuptools.html#namespace-packages

'''dr — namespace package'''

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
