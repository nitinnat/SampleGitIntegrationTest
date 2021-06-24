# from setuptools import setup
#
# setup(setup_requires='packit', packit=True)

from setuptools import setup
import time
import os
from os import environ, getcwd

user_name = environ["USERNAME"] if "C:" in getcwd() else environ["USER"]

version_path = os.path.join(os.path.dirname(__file__), 'version.txt')
version_str = 'UNSPECIFIED_VERSION'
if os.path.exists(version_path):
    with open(version_path, 'r') as f:
        version_str = f.readline()

version_desc = 'deployed on {} by {}'.format(time.strftime("%Y-%m-%d-%H-%M-%S"), user_name)
print(version_desc)

setup(name='SampleTest',
      version=version_str,
      description=version_desc,
      packages=[],
      py_modules=['math_calcs.py']
      include_package_data=True,
      package_data={})
