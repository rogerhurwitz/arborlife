import mpmath as mp


class Soil:
    """Soil takes in and gives out moisture within its capacity limits."""

    # Ensures decimal precision of mpmath sufficient for all uses
    mp.mp.dps = 30

    MAX_MOISTURE_FT3 = mp.mpf("1.18") * mp.mpf("10e26")
    """mpf: Default maximum moisture capacity of soil in molecules"""

    FIELD_CAPACITY = 10
    """int: Maximum moisture capacity of soil on a 0 to 10 scale"""

    def __init__(self, max_moisture_ft3=MAX_MOISTURE_FT3):

        # Convert specified value into an mpf if possible
        if not isinstance(max_moisture_ft3, mp.mpf):
            max_moisture_ft3 = mp.mpf(max_moisture_ft3)

        self._max_moisture_ft3 = max_moisture_ft3

        # Available moisture is assumed to be at maximum initially
        self._moisture_ft3 = max_moisture_ft3

    @property
    def soil_moisture(self):
        """mpf: Available moisture in soil on a scale between 0.0 and 10.0"""

        # Calculated from moisture_ft3 to avoid synchronization overhead
        return Soil.FIELD_CAPACITY * (self._moisture_ft3 / self._max_moisture_ft3)          # noqa: E501

    @soil_moisture.setter
    def soil_moisture(self, new_sm):

        # Convert specified value into an mpf if possible
        if not isinstance(new_sm, mp.mpf):
            new_sm = mp.mpf(new_sm)

        # Clamp value between boundary values if out of range
        if new_sm < 0 or new_sm > Soil.FIELD_CAPACITY:
            new_sm = mp.mpf(max(0, min(new_sm, Soil.FIELD_CAPACITY)))

        # Changes _moisture_ft3 then used by soil_moisture property getter
        self._moisture_ft3 = new_sm * self._max_moisture_ft3 / Soil.FIELD_CAPACITY           # noqa: E501

    @property
    def moisture_ft3(self):
        """mpf: Current water level as molecules per cubic foot"""
        return self._moisture_ft3

    @moisture_ft3.setter
    def moisture_ft3(self, new_m_ft3):

        # Convert specified value into an mpf if possible
        if not isinstance(new_m_ft3, mp.mpf):
            new_m_ft3 = mp.mpf(new_m_ft3)

        # Clamp value between boundary values if out of range
        if new_m_ft3 > self._max_moisture_ft3 or new_m_ft3 < 0:
            new_m_ft3 = mp.mpf(max(0, min(new_m_ft3, self._max_moisture_ft3)))

        self._moisture_ft3 = new_m_ft3
