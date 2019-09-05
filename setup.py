import os
from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='BruteBuster',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='The Python Packaging Authority', 
    description='BruteBuster is a simple, pluggable Django app that can help you protect against password bruteforcing attempts.',
    long_description="",
    url='https://github.com/gutyril/django-brutebuster',
    author='',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django'
        'Framework :: Django :: 1.8.2',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The Python Packaging Authority',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

