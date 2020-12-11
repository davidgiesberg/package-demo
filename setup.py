from setuptools import setup

setup(name='demo_package',
      version='1.0',
      # list folders, not files
      packages=['demo_package',
                'demo_package.test1',
                'demo_package.test2'],
      )
