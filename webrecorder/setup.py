#!/usr/bin/env python
# vim: set sw=4 et:

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os

from webrecorder import __version__


# Fix for TypeError: 'NoneType' object is not callable" error
# when running 'python setup.py test'
try:
    import multiprocessing
except ImportError:
    pass


#long_description = open('README.rst').read()
long_description = ''


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        # should work with setuptools <18, 18 18.5
        self.test_suite = ' '

    def run_tests(self):
        import pytest
        import sys
        import os
        cmdline = ' --cov-config .coveragerc --cov ./webrecorder/ -vv ./test/'
        errcode = pytest.main(cmdline)
        sys.exit(errcode)


setup(
    name='webrecorder',
    version=__version__,
    url='https://webrecorder.io',
    author='rhizome.org',
    author_email='support@webrecorder.io',
    description='Webrecorder Archiving Platform',
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    provides=[
        'webrecorder',
        'webrecorder.rec',
        'webrecorder.load',
    ],
    package_data={
        'webrecorder': ['config/*',
                        'static/*.*',
                        'static/bundle/*',
                        'templates/*.*',
                        'templates/recordings/*',
                        'static/external/bootstrap/fonts/*'],
    },
    install_requires=[
        'youtube_dl',
        'itsdangerous',
        'bottle',
        'uwsgi',
        'gevent==1.1.2',
        'boto',
        'requests>=2.9.1',
        'bottle-cork==0.12.0',
        'marshmallow',
        'werkzeug',
        'urllib3',
        'pywb>=0.50.0',
        'webassets==0.12.0',
        'karellen-geventws'
    ],
    dependency_links=[
        'git+https://github.com/ikreymer/pywb.git@new-pywb#egg=pywb-0.50.0',
        'git+https://github.com/ikreymer/webassets.git@pyinstaller#egg=webassets-0.12.0',
    ],
    tests_require=[
        'pytest',
        'WebTest',
        'pytest-cov',
        'fakeredis',
        'mock',
       ],
    cmdclass={'test': PyTest},
    test_suite='',
    entry_points="""
        [console_scripts]
        webrecorder = webrecorder.standalone.standalone:main
    """
)
