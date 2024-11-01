from setuptools import setup, find_packages
import os

setup(
    name="importfa",
    version="0.4",
    packages=find_packages(),
    install_requires=[],
    author="wywzxxz",
    author_email="wywzxxz@163.com",
    description="add parent/ancestor folder path into sys.path when import",
    license="MIT",
    keywords="sample setuptools development",
    url="https://github.com/wywzxxz/importfa",
    long_description=open(os.path.abspath(__file__ + "/../README.txt")).read(),
    long_description_content_type="text/markdown",
)
