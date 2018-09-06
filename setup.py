import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_require = {
    # Test dependencies
    'tests': [
        'pylint < 1.7.0',  # TODO: Why a maximum?
        'pytest-cov >= 1.8.0',
        'dnslib >= 0.9.7',
        'requests-mock >= 1.0.0',
    ]
}

# Generate minimum dependencies
extras_require['tests-min'] = [dep.replace('>=', '==') for dep in extras_require['tests']]

setuptools.setup(
    name="certcentral",
    version="0.1",
    author="Alex Monk",
    author_email="krenair@gmail.com",
    description="Python application to request certificates from ACME servers and distribute to authorised clients.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://phabricator.wikimedia.org/diffusion/OSCC/",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'certcentral-backend = certcentral.certcentral:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'acme >= 0.25.1, < 0.26.0',  # TODO: Why a maximum?
        'cryptography >= 1.7.1',
        'dnspython >= 1.15.0',
        'flask >= 0.12.1, < 1.0.0',  # TODO: Why a maximum?
        'josepy >= 1.0.1',
        'pyOpenSSL >= 16.2.0',
        'requests >= 2.18.4',
        'pyyaml >= 3.12'
    ],
    extras_require=extras_require
)