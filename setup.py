import re
from setuptools import setup, find_packages


def readme():
    """Return the contents of the project README file."""
    with open('README.md') as f:
        return f.read()


def get_requirements():
    """Return a list of package requirements from the requirements.txt file."""
    with open('requirements.txt') as f:
        return f.read().split()


version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", open('msdbook/__init__.py').read(), re.M).group(1)


setup(
    name='msdbook',
    version=version,
    packages=find_packages(),
    url='https://github.com/IMMM-SFA/msd_uncertainty_ebook',
    license='BSD-2-Clause',
    author='Chris R. Vernon',
    author_email='chris.vernon@pnnl.gov',
    description='Jupyter notebook support for the MSD ebook',
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6.*, <4',
    include_package_data=True,
    install_requires=[
        "numpy>=1.14",
        "SALib>=1.3.11",
        "statsmodels>=0.12.1",
        "pandas>=1.1.4",
        "matplotlib>=3.3.3",
        "seaborn>=0.11.1"
    ],
    extras_require={
        'dev': [
            'build~=0.5.1',
            'nbsphinx~=0.8.6',
            'setuptools~=57.0.0',
            'sphinx~=4.0.2',
            'sphinx-rtd-theme~=0.5.2',
            'twine~=3.4.1'
        ]
    }
)