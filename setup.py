from setuptools import setup, find_packages
import os

version = '0.7.dev0'

setup(name='collective.z3cform.datagridfield_demo',
      version=version,
      description="Version of DataGridField for use with Dexterity / z3c.form - Demo views",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone, Dexterity, z3c.form',
      author='Kevin Gill',
      author_email='kevin@movieextras.ie',
      url='https://github.com/collective/collective.z3cform.datagridfield_demo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.z3cform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'five.grok',
          'plone.directives.form',
          'plone.app.z3cform',
          'collective.z3cform.datagridfield',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
