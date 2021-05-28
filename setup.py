from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().split()


setup(
    name='nanites',
    version='0.1.0',
    packages=['nanites'],
    url='https://github.com/IMMM-SFA/msd_uncertainty_ebook',
    license='BSD 2-Clause',
    author='Chris R. Vernon',
    author_email='chris.vernon@pnnl.gov',
    description='Jupyter notebook support for the purpose of sensitivity analysis and uncertainty quantification education',
    long_description=readme(),
    python_requires='>=3.6.0',
    include_package_data=True,
    install_requires=get_requirements()
)
