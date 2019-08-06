import os
from setuptools import setup, find_packages

package_dir = os.path.join("PyFlow", "Packages")
packages = find_packages(package_dir)
packages = [os.path.join(package_dir, pkg) for pkg in packages]


setup(name='pyflow.maya',
      version="0.0.1",
      packages=packages,
      maintainer="WonderWorks Software",
      maintainer_email="wonderworks.software@gmail.com",
      url="https://github.com/wonderworks-software/PyFlowMaya",
      description="maya nodes for pyflow",
      include_package_data=True)
