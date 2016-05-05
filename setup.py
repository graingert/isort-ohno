from __future__ import generator_stop

from setuptools import find_packages, setup

# readme = open('README.rst').read()
# history = open('CHANGES.rst').read().replace('.. :changelog:', ')

setup(
    name='isort-ohno',
    version='0.1.0',
    description='Ohno',
    # long_description=readme + '\n\n' + history,
    author='Thomas Grainger',
    author_email='isort-ohno@graingert.co.uk',
    license="MIT",
    url='https://bitbucket.com/graingert/isort-ohno',
    packages=find_packages('src', exclude='tests'),
    package_dir={'': 'src/'},
    install_requires=[],
    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
