#!/usr/bin/env python

METADATA = dict(
    name='django-email-html',
    version='0.2',
    author='ramusus',
    description='Application for switching from Django plain-text emails to html emails with 2 bodies: html and plain-text, generated automatically from html',
    long_description=open('README').read(),
    packages=['email_html', 'email_html.templatetags'],
    url='http://github.com/ramusus/django-email-html',
    install_requires=[
        'beautifulsoup',
    ],
)

if __name__ == '__main__':
    try:
        import setuptools
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)
