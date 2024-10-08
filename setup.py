from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.0.1'
DESCRIPTION = 'The simplest way to quickly manipulate CSV and XLSX files via the command line.'

# Setting up
setup(
    name="mappa-cli",
    version=VERSION,
    author="0x3at",
    author_email="<ethan.lrose@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['mappa = mappa.cli:main']
    },
    install_requires=[
    'click==8.1.7',
    'colorama==0.4.6',
    'et-xmlfile==1.1.0',
    'numpy==2.1.2',
    'openpyxl==3.1.5',
    'pandas==2.2.3',
    'pyarrow==17.0.0',
    'python-dateutil==2.9.0.post0',
    'pytz==2024.2',
    'setuptools==75.1.0',
    'six==1.16.0',
    'tzdata==2024.2'
    ],
    python_requires='>=3.6',
    keywords=['python', 'csv', 'remap', 'remap csv', 'rename headers', 'header keys', 'strip columns', 'lowercase headers'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)