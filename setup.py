# -*- coding: utf-8 -*-
# Copyright 2020 PyePAL authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model agnostic Python implementation of the epsilon-PAL algorithm"""

from distutils.core import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext

import versioneer

with open("requirements.txt", "r") as fh:
    REQUIREMENTS = fh.readlines()


with open("README.md", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

eqeq_module = Pybind11Extension(
    "pyeqeq_eqeq", ["src/main.cpp"], include_dirs=["src"], extra_compile_args=["-O3"]
)


setup(
    name="pyeqeq",
    version=versioneer.get_version(),
    description="Charge equilibration method for crystal structures.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["pyeqeq"],
    url="https://github.com/danieleongari/eqeq",
    # license="Apache 2.0",
    install_requires=["pybind11"],
    ext_modules=[eqeq_module],
    entry_points={"console_scripts": ["eqeq=pyeqeq.cli:cli"]},
    extras_require={
        "testing": ["pytest==6.*", "pytest-cov==2.*"],
        "docs": [
            "sphinx==3.*",
            "sphinx-book-theme==0.*",
            "sphinx-autodoc-typehints==1.*",
            "sphinx-copybutton==0.*",
        ],
        "pre-commit": ["pre-commit==2.*", "pylint==2.*", "isort==5.*",],
        "dev": ["versioneer==0.*", "black==20.*",],
    },
    author="EqEq authors",
    author_email="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={"build_ext": build_ext},
    package_data={"": ["data/*.dat"]},
    include_package_data=True,
)
