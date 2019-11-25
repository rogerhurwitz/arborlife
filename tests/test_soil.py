import pytest
from arborlife.soil import Soil


@pytest.mark.parametrize("field_capacity", [-1, 11])
def test_bad_initialization(field_capacity):
    """Test ValueError exception on illegal field_capacity initializer."""
    with pytest.raises(ValueError) as _:
        Soil(field_capacity)


def test_modifying_field_capacity():
    """Test field_capacity is a read-only property after initialization."""
    s = Soil()
    with pytest.raises(AttributeError) as _:
        s.field_capacity = 0


@pytest.mark.parametrize("field_capacity", [0, 10])
def test_good_initialization(field_capacity):
    """Test that field_capacity property set properly at initialization"""
    s = Soil(field_capacity)
    assert s.field_capacity == field_capacity


def test_moisture_overflow():
    s = Soil()
    max_moisture = s.field_capacity / 10 * Soil.FC_MOISTURE_FT3
    with pytest.raises(ValueError) as _:
        s.moisture = max_moisture + 10_000
