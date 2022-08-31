from setuptools import setup

__version__ = 0.2


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='nf-launcher',
    version=__version__,
    author='Jordi Deu-Pons',
    description='Installs the Nextflow launcher',
    scripts=['launcher/nextflow'],
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MPL-2",
    keywords=["pipeline", "workflow", "nextflow"],
    install_requires=[],
    classifiers=[]
)
