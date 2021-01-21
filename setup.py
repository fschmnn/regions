
long_description = f"""
define regions in the sky

... 

"""

from setuptools import setup, find_namespace_packages

setup(name='region',
      version='0.1',
      author='Fabian Scheuermann',
      author_email='f.scheuermann@uni-heidelberg.de',
      license='MIT',
      package_dir={"": "src"},
      packages=find_namespace_packages(where="src"),
      description='regions in the sky',
      long_description = long_description)