import pytest
from area import compute_area

def test_circle_area_pass():
    result = compute_area("circle", "3")
    assert result == pytest.approx(28.274333882308138)

def test_square_area_fail():
    result = compute_area("square", "s3")
    assert result == pytest.approx(9)
