import pytest

from arborlife.soil import Soil


def test_default_init_good():
    s = Soil()
    assert s._max_moisture_ft3 == Soil.MAX_MOISTURE_FT3
    assert s.moisture_ft3 == Soil.MAX_MOISTURE_FT3


def test_specified_init_good():
    s = Soil(max_moisture_ft3=Soil.MAX_MOISTURE_FT3 / 2)
    assert s._max_moisture_ft3 == Soil.MAX_MOISTURE_FT3 / 2
    assert s.moisture_ft3 == Soil.MAX_MOISTURE_FT3 / 2


@pytest.mark.parametrize("mm_ft3,expected", [
    (-1, 0), (Soil.MAX_MOISTURE_FT3 * 2, Soil.MAX_MOISTURE_FT3)])
def test_specified_init_clamp(mm_ft3, expected):
    s = Soil(max_moisture_ft3=mm_ft3)
    assert s.moisture_ft3 == expected


def test_moisture_overflow():
    s = Soil()
    s.moisture_ft3 = s.moisture_ft3 + 1
    assert s.moisture_ft3 == s._max_moisture_ft3


def test_moisture_underflow():
    s = Soil()
    s.moisture_ft3 = -1
    assert s.moisture_ft3 == 0


def test_sm_overflow():
    s = Soil()
    s.soil_moisture = s.soil_moisture + 1
    assert s.soil_moisture == Soil.FIELD_CAPACITY


def test_sm_underflow():
    s = Soil()
    s.soil_moisture = -1
    assert s.soil_moisture == 0


@pytest.mark.parametrize("moisture_pct,soil_moisture", [(1.0, 10), (0.5, 5), (0, 0)])
def test_sm_from_moisture(moisture_pct, soil_moisture):
    s = Soil()
    s.moisture_ft3 *= moisture_pct
    assert s.soil_moisture == soil_moisture


@pytest.mark.parametrize("soil_moisture,moisture_pct", [(10, 1), (5.5, 0.55), (0, 0)])
def test_moisture_from_sm(soil_moisture, moisture_pct):
    s = Soil()
    s.soil_moisture = soil_moisture
    assert s.moisture_ft3 == s._max_moisture_ft3 * moisture_pct
    assert round(s.soil_moisture, 4) == soil_moisture
