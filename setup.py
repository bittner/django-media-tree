# encoding=utf8
import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
REQS = [str(ir.req) for ir in install_reqs]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = "django-media-tree",
    version = "0.9.0",

    url = 'http://github.com/samluescher/django-media-tree',
    license = 'BSD',
    description = "Django Media Tree is a Django app for managing your website's media files in a folder tree, and using them in your own applications.",
    long_description = README,

    author = u'Samuel Luescher',
    author_email = 'sam at samluescher dot net',

    packages = find_packages(),
    include_package_data=True,
    install_requires=REQS,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
