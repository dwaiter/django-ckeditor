import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

setup(
    name='django-ckeditor',
    version='0.0.1',
    description='A small Django application which makes it easy to use '
                'CKEditor for form textareas.',
    long_description=open(README_PATH).read(),
    author='Dumbwaiter Design',
    author_email='dev@dwaiter.com',
    url='https://dwaiter.codebasehq.com/util/django-ckeditor/',
    packages=['ckeditor'],
)
