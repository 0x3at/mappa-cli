from setuptools import setup, find_packages
from pathlib import Path


VERSION = '0.0.1.0'
DESCRIPTION = 'The simplest way to quickly manipulate CSV and XLSX files via the command line.'

here = Path(__file__).parent
LONG_DESCRIPTION = (here / "README.md").read_text(encoding='utf-8')

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

setup(
    name="mappa-cli",
    version=VERSION,
    author="Dunder Dev",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    license = "GLWTS",
    license_files = "LICENSE.txt",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['mappa = mappa.cli:main']
    },
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
    keywords=['python', 'csv', 'remap', 'remap csv', 'rename headers', 'header keys', 'strip columns', 'lowercase headers'],
    url = "https://github.com/0x3at/mappa-cli",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)