from setuptools import setup, find_packages

setup(
    name='waveform-factory',
    version='0.1.0',
    url='https://github.com/MrB-Can/waveform-factory',
    author='Paul Bennett',
    author_email='paul@lgis.ca',
    description='Waveform Factory is a python library that generates various types of waveform patterns. It is '
                'designed to aid in the creation, manipulation, and analysis of waveform data for various '
                'applications including music, signal processing, and more.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)
