import os
from setuptools import setup, find_packages

install_requires = []
try:
    import json
except ImportError, e:
    install_requires.append('simplejson')

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

description = 'A small Django application that makes it easy to use CKEditor for form textareas.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

ckeditor_dir = 'ckeditor'

for dirpath, dirnames, filenames in os.walk(ckeditor_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split(os.sep)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

#print data_files

setup(
    name='django-ckeditor',
    version='0.9.5',
    install_requires=install_requires,
    description=description,
    long_description=long_description,
    author='Dumbwaiter Design',
    author_email='dev@dwaiter.com',
    url='http://bitbucket.org/dwaiter/django-ckeditor/',
    packages=packages,
    data_files=data_files,
)
