
import os
from setuptools import setup

from django_google_maps import VERSION

REQUIREMENTS = [
    'django',
    'mock',
]
README = os.path.join(os.path.dirname(__file__), 'README.md')
LONG_DESCRIPTION = open(README, 'r').read()
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]

setup(
    name="django-google-maps",
    version=VERSION,
    author="Aaron Madison",
    author_email="aaron.l.madison@gmail.com",
    description="Plugs google maps V3 api into Django admin.",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/madisona/django-google-maps",
    packages=("django_google_maps",),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
