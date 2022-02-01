from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='try-pipenv',
    version='0.1.0',
    author_email='matthewmmangione@gmail.com',
    description='try out pipenv and create a jsnon file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src')
)