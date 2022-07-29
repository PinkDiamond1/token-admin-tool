#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "bpx-blockchain@git+https://github.com/bpx-network/bpx-blockchain.git@main",
]

dev_dependencies = [
    "black==21.12b0",
    "pytest",
    "pytest-env",
]

setup(
    name="token_admin_tool",
    version="0.0.1",
    author="BPX Network",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "cats = cats.cats:main",
            "secure_the_bag = cats.secure_the_bag:main",
            "unwind_the_bag = cats.unwind_the_bag:main"
        ],
    },
    author_email="hello@bpxcoin.cc",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/bpx-network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Tools to administer issuance and redemption of a BPX blockchain tokens",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/bpx-network/token-admin-tool",
        "Source": "https://github.com/bpx-network/token-admin-tool",
    },
)
