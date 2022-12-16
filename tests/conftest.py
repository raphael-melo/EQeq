import os

import pytest

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def get_hkust():
    return os.path.join(_THIS_DIR, "test_files", "HKUST-1.cif")
