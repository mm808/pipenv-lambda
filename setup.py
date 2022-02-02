from gettext import install
from platform import python_revision
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pipenv-lambda',
    version='0.1.0',
    author_email='matthewmmangione@gmail.com',
    description='try out pipenv to create a lambda',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    python_requires='>=3.6'
)