import mpmath as mp
import pytest

from arborlife.soil import Soil


def test_default_init_good():
    s = Soil()
    assert s.moisture_ft3 == Soil.MAX_MOISTURE_FT3
    assert isinstance(s.moisture_ft3, mp.mpf)


def test_specified_init_bad():
    with pytest.raises(ValueError) as _:
        Soil("Hello, world.")


def test_specified_init_good():
    s = Soil(Soil.MAX_MOISTURE_FT3 / 2)
    assert s.moisture_ft3 == Soil.MAX_MOISTURE_FT3 / 2
    assert isinstance(s.moisture_ft3, mp.mpf)


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


@pytest.mark.parametrize(
    "moisture_pct,soil_moisture",
    [(mp.mpf('1.0'), mp.mpf('10')), (mp.mpf('0.5'), mp.mpf('5')), (mp.mpf('0'), mp.mpf('0'))]
)
def test_sm_from_moisture(moisture_pct, soil_moisture):
    s = Soil()
    s.moisture_ft3 *= moisture_pct
    assert s.soil_moisture == soil_moisture


@pytest.mark.parametrize(
    "soil_moisture,moisture_pct",
    [(mp.mpf('10'), mp.mpf('1.0')), (mp.mpf('5.5'), mp.mpf('0.55')), (mp.mpf('0'), mp.mpf('0'))]
)
def test_moisture_from_sm(soil_moisture, moisture_pct):
    s = Soil()
    s.soil_moisture = soil_moisture
    assert s.moisture_ft3 == s._max_moisture_ft3 * mp.mpf(str(moisture_pct))
    assert s.soil_moisture == soil_moisture
