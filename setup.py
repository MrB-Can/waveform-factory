from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='waveform_factory',
    version='0.1.3',

    url='https://github.com/MrB-Can/waveform-factory',
    author='Paul Bennett',
    author_email='paul@lgis.ca',
    description='Wave form data generator',
    long_description='Waveform Factory is a python library that generates various types of waveform patterns. It is '
                'designed to aid in the creation, manipulation, and analysis of waveform data for various '
                'applications including music, signal processing, and more.',
    packages=find_packages(include=['waveform_factory', 'waveform_factory.*']),
    install_requires=required,
)
 