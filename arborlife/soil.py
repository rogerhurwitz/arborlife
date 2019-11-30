import mpmath as mp


class Soil:
    """Soil takes in and gives out moisture within its capacity limits."""

    # Ensures decimal precision of mpmath sufficient for all uses
    mp.mp.dps = 30

    # mpf is decimal-accurate floating point used by mpmath
    MAX_MOISTURE_FT3 = mp.mpf("1.18") * mp.mpf("10e26")

    FC = 10

    def __init__(self, max_moisture_ft3=MAX_MOISTURE_FT3):

        if not isinstance(max_moisture_ft3, mp.mpf):
            raise TypeError("max_moisture_ft3 must be an mpmath.dpf")

        self._max_moisture_ft3 = max_moisture_ft3
        self._moisture_ft3 = max_moisture_ft3

    @property
    def soil_moisture(self):
        """Degree of moisture in soil on a 0-10 scale (mpmath.mpf)"""

        # soil_moisture calculated from moisture_ft3 to avoid synchronization
        return Soil.FC * (self._moisture_ft3 / self._max_moisture_ft3)

    @soil_moisture.setter
    def soil_moisture(self, value):

        if not isinstance(value, mp.mpf):
            raise TypeError("soil_moisture must be an mpmath.mpf")

        if value > Soil.FC or value < 0:
            raise ValueError(f"soil_moisture must be between 0 and {Soil.FC}")

        # Changes moisture_ft3 - soil_moisture is always calculated
        self._moisture_ft3 = value * self._max_moisture_ft3 / Soil.FC

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
