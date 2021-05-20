# -*- coding: utf-8 -*-

from ._version import get_versions
import pkg_resources

__version__ = get_versions()["version"]
del get_versions

IONIZATION_DATA_PATH = pkg_resources.resource_filename(
    "pyeqeq", "data/ionizationdata.dat"
)
CHARGE_DATA_PATH = pkg_resources.resource_filename("pyeqeq", "data/chargecenters.dat")

