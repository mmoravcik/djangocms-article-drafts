from setuptools import find_packages, setup

import djangocms_article_drafts

INSTALL_REQUIREMENTS = [
    'Django>=1.8,<2.0',
    'django-cms>=3.4.2',
    'djangocms_helper',
]

setup(
    name='djangocms-article-drafts',
    packages=find_packages(),
    include_package_data=True,
    version=djangocms_article_drafts.__version__,
    description=djangocms_article_drafts.__doc__,
    long_description=open('README.md').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author='Divio AG',
    author_email='info@divio.ch',
    url='http://github.com/foo/djangocms-article-drafts',
    license='BSD',
    test_suite='djangocms_article_drafts.tests.settings.run',
)
