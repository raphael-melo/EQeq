import pytest

from pyeqeq import run_on_cif


def test_run_on_cif(get_hkust):
    res = run_on_cif(get_hkust)
    assert len(res) == 624
    assert pytest.approx(sum(res), 0.0001) == 0.0
