# -*- coding:utf8 -*-

# Distributed under the MIT license, see LICENSE

from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='simplesite',
    version=0.1,
    description="""
      Django app to create simple websites with a basic Page model which can
      create generic relations with any other model to get its full queryset
    """,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django==1.11.10',
        'pillow==5.0.0',
        'django-summernote==0.8.8.6',
    ],
    zip_safe=False,
    author='marcopuccio',
    url='https://github.com/marcopuccio/simple-site',
    classifiers=[
        'Enviroment :: Web Enviroment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT Licence',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)
