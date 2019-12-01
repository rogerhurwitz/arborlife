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

        if not isinstance(max_moisture_ft3, mp.mpf):
            raise TypeError("max_moisture_ft3 must be an mpmath.dpf")

        self._max_moisture_ft3 = max_moisture_ft3
        self._moisture_ft3 = max_moisture_ft3

    @property
    def soil_moisture(self):
        """float: Available moisture in soil between 0 and 10 scale"""

        # soil_moisture calculated from moisture_ft3 to avoid synchronization
        return Soil.FIELD_CAPACITY * (self._moisture_ft3 / self._max_moisture_ft3)          # noqa: E501

    @soil_moisture.setter
    def soil_moisture(self, value):

        if not isinstance(value, mp.mpf):
            raise TypeError("soil_moisture must be an mpmath.mpf")

        if value > Soil.FIELD_CAPACITY or value < 0:
            raise ValueError(f"soil_moisture must be between 0 and {Soil.FIELD_CAPACITY}")  # noqa: E501

        # Changes moisture_ft3 - soil_moisture is always calculated
        self._moisture_ft3 = value * self._max_moisture_ft3 / Soil.FIELD_CAPACITY           # noqa: E501

    @property
    def moisture_ft3(self):
        """Current water level as molecules per cubic foot (mpmath.mpf)"""
        return self._moisture_ft3

    @moisture_ft3.setter
    def moisture_ft3(self, value):

        if not isinstance(value, mp.mpf):
            raise TypeError("moisture_ft3 must be an mpmath.dpf")

        if value > self._max_moisture_ft3 or value < 0:
            raise ValueError(
                f"moisture_ft3 must be between 0 and {self._max_moisture_ft3}"
            )

        self._moisture_ft3 = mp.mpf(value)
