import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='summarizer_package',
    author='Anton Zabolotsky',
    author_email='bognev@mail.ru',
    description='Summarizer Package',
    keywords='summarizer, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bognev/summarizer_package',
    project_urls={
        'Documentation': 'https://github.com/bognev/summarizer_package',
        'Bug Reports':
        'https://github.com/bognev/summarizer_package/issues',
        'Source Code': 'https://github.com/bognev/summarizer_package',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    install_requires= ['argparse>=1.1',
                        'scikit-learn>=0.24.1',
                        'numpy>=1.19.2',
                        'tabulate',
                        'openpyxl',
                        'et_xmlfile>=1.0.1',
                        'jdcal>=1.4.1',
                        'pandas>=1.2.4',
                        'atomicwrites>=1.4.0',
                        'iniconfig>=1.1.1',
                        'more-itertools>=8.5.0',
                        'pluggy>=0.13.1',
                        'py>=1.9.0',
                        'pytest>=6.1.1',
                        'toml>=0.10.1'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
