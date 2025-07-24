from setuptools import setup, find_packages

setup(
    name='flair',
    version='0.0.2',
    packages=find_packages(),
    author='blu',
    description='<flair description>',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'flet==0.25.0'
    ]
)
