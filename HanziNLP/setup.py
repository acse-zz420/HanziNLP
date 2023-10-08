# setup.py
from setuptools import setup, find_packages

setup(
    name='HanziNLP',
    version='0.1',
    packages=find_packages(),
    author='Zhan Shi',
    author_email='samzshi@sina.com',
    description='A NLP package specifically for Chinese',
    license='MIT',
    install_requires=[
        'jieba>=0.42.1',
        'matplotlib>=3.4.3'
        # add other dependencies as needed
    ],
    include_package_data=True,  # This includes all files in the package
    package_data={
        'HanziNLP': ['fonts/*.ttf',
                     'stopwords/*.txt'
                    ],  # Include all .otf files under the fonts directory
    },
)
