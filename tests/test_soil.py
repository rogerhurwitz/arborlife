import mpmath as mp
import pytest

from arborlife.soil import Soil


def test_default_init():
    s = Soil()
    assert s.moisture_ft3 == Soil.DEF_MAX_MOISTURE_FT3
    assert isinstance(s.moisture_ft3, mp.mpf)


def test_specified_init_bad():
    with pytest.raises(TypeError) as _:
        Soil(1.18 * 10e26)


def test_specified_init_good():
    s = Soil(Soil.DEF_MAX_MOISTURE_FT3 / 2)
    assert s.moisture_ft3 == Soil.DEF_MAX_MOISTURE_FT3 / 2
    assert isinstance(s.moisture_ft3, mp.mpf)


def test_moisture_overflow():
    s = Soil()
    with pytest.raises(ValueError) as _:
        s.moisture_ft3 = s.moisture_ft3 + 1


def test_moisture_underflow():
    s = Soil()
    with pytest.raises(ValueError) as _:
        s.moisture_ft3 = -1


def test_sm_overflow():
    s = Soil()
    with pytest.raises(ValueError) as _:
        s.soil_moisture = s.soil_moisture + 1


def test_sm_underflow():
    s = Soil()
    with pytest.raises(ValueError) as _:
        s.soil_moisture = -1


@pytest.mark.parametrize(
    "moisture_pct,soil_moisture",
    [(1.0, 10), (0.5, 5), (0, 0)]
)
def test_sm_from_moisture(moisture_pct, soil_moisture):
    s = Soil()
    s.moisture_ft3 *= moisture_pct
    assert s.soil_moisture == soil_moisture


@pytest.mark.parametrize(
    "soil_moisture,moisture_pct",
    [(10, 1.0), (5.5, 0.55), (0, 0)]
)
def test_moisture_from_sm(soil_moisture, moisture_pct):
    s = Soil()
    s.soil_moisture = soil_moisture
    assert s.moisture_ft3 == s._max_moisture_ft3 * mp.mpf(str(moisture_pct))
    assert s.soil_moisture == soil_moisture
