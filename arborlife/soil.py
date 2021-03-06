import logging

log = logging.getLogger(__name__)


class Soil:
    """Soil takes in and gives out moisture within its capacity limits."""

    MAX_MOISTURE_FT3 = 1.18 * 10e26
    """float: Default maximum moisture capacity of soil in molecules"""

    RAIN_INCH_FT3 = 7.89 * 10e25
    """"""

    FIELD_CAPACITY = 10
    """int: Maximum moisture capacity of soil on a 0 to 10 scale"""

    def __init__(self, max_moisture_ft3=MAX_MOISTURE_FT3):

        if max_moisture_ft3 < 0 or max_moisture_ft3 > Soil.MAX_MOISTURE_FT3:
            log.warning(f"soil.__init__ called w/ out of bounds value: {max_moisture_ft3}")

        # Clamp max_moisture_ft3 between boundary values if out of range
        self._max_moisture_ft3 = max(0, min(max_moisture_ft3, Soil.MAX_MOISTURE_FT3))

        # Available moisture is assumed to be at maximum initially
        self._moisture_ft3 = self._max_moisture_ft3

    @property
    def soil_moisture(self):
        """float: Available moisture in soil on a scale between 0.0 and 10.0"""

        # Calculated from moisture_ft3 to avoid synchronization complexity
        return Soil.FIELD_CAPACITY * (self._moisture_ft3 / self._max_moisture_ft3)

    @soil_moisture.setter
    def soil_moisture(self, new_sm):

        # Clamp value between boundary values if out of range
        if new_sm < 0 or new_sm > Soil.FIELD_CAPACITY:
            log.warning(f"soil_moisture.setter called w/ out of bounds value: {new_sm}")
            new_sm = max(0, min(new_sm, Soil.FIELD_CAPACITY))

        # Changes _moisture_ft3 then used by soil_moisture property getter
        self._moisture_ft3 = new_sm * self._max_moisture_ft3 / Soil.FIELD_CAPACITY           # noqa: E501

    @property
    def moisture_ft3(self):
        """float: Current water level as molecules per cubic foot"""
        return self._moisture_ft3

    @moisture_ft3.setter
    def moisture_ft3(self, new_m_ft3):

        if new_m_ft3 > self._max_moisture_ft3 or new_m_ft3 < 0:
            log.warning(f"moisture_ft3.setter called w/ out of bounds value: {new_m_ft3}")

        # Clamp value between boundary values if out of range
        self._moisture_ft3 = max(0, min(new_m_ft3, self._max_moisture_ft3))
