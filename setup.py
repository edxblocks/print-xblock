"""Setup for printxblock XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='print-xblock',
    version='1.0',
    description='An xblock to simplify printing of Open edX pages',
    license='AGPL v3',
    packages=[
        'printxblock',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils'
    ],
    entry_points={
        'xblock.v1': [
            'printxblock = printxblock:PrintXBlock',
        ]
    },
    package_data=package_data("printxblock", ["static", "public"]),
)
