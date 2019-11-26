import pytest
from arborlife.soil import Soil

#
# field_capacity tests
#


def test_field_capacity_overflow():
    with pytest.raises(ValueError) as _:
        Soil(10 + 1)


def test_field_capacity_underflow():
    with pytest.raises(ValueError) as _:
        Soil(0 - 1)


def test_field_capacity_immutability():
    s = Soil()
    with pytest.raises(AttributeError) as _:
        s.field_capacity = 0


def test_field_capacity_default_init():
    s = Soil()
    assert s.field_capacity == 10


def test_field_capacity_specified_init():
    s = Soil(5)
    assert s.field_capacity == 5


#
# moisture_gauge tests
#


@pytest.mark.parametrize("test_input,expected", [(1, 10), (0.5, 5), (0, 0)])
def test_moisture_guage(test_input, expected):
    s = Soil()
    s.moisture *= test_input
    assert s.moisture_gauge == expected


def test_moisture_gauge_immutability():
    s = Soil()
    with pytest.raises(AttributeError) as _:
        s.moisture_gauge = 0


@pytest.mark.skip(reason="Will fail with floating point implementation")
def test_moisture_overflow():
    s = Soil()
    max_moisture = s.field_capacity / 10 * Soil.FC_MOISTURE_FT3
    with pytest.raises(ValueError) as _:
        s.moisture = max_moisture + 1
