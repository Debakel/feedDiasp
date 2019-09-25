# coding=utf-8

from setuptools import setup

setup(name='feeddiasp',
      version='0.2.0',
      description='Feed Diaspora with RSS-Feeds or Facebook',
      url='https://github.com/Debakel/feedDiasp/',
      author='Moritz Duchêne',
      author_email='',
      license='GPL',
      packages=['feeddiasp'],
      install_requires=['facepy', 'argparse', 'diaspy-api', 'feedparser', 'html2text', 'pypandoc', 'requests'],
      classifiers=["Programming Language :: Python :: 3"],
      keywords='diaspora facebook bot rss')
