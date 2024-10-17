from setuptools import setup
from io import open

# Define test requirements
test_requirements = ['pytest']

# Define additional requirements
extras = {'test': test_requirements}

with open('docs/README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spcol',
    version='0.1.0',  # Update with your package version
    license='GNU General Public License v3.0',
    url='https://github.com/AkshayK325/spcol',
    description='B-spline collocation matrix for B-spline basis and derivative computation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Akshay Kumar',
    author_email='akshaykumar@wisc.edu',
    packages=['spcol'],
    install_requires=[
        'numpy',  # Required dependency
    ],
    extras_require=extras,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',  # Specify Python versions supported
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': ['spcol = spcol.cli:main']  # Update with your CLI command if any
    },
    tests_require=test_requirements,
    keywords='B-spline, collocation matrix, basis functions, derivatives, numerical methods, interpolation, CAD',
)