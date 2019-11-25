from decimal import Decimal


class Soil:
    """Soil takes in and gives out moisture within its capacity limits.

    Constants:
    FC_MOISTURE_FT3 -- Represents the maximum number of molecules of water
        per square foot that soil can hold assuming maximum field_capacity.

    Attributes:
        field_capacity -- A dimensionless number between 0 and 10 representing
            the most saturated the soil can be (10 = 100%).  Defaults to 10.
        moisture -- Current amount of soil moisture.  Must be between 0 and
            maximum capacity defined as field_capacity / 10 * FC_MOISTURE_FT3
    """

    FC_MOISTURE_FT3 = Decimal("1.18") * Decimal("10e26")

    def __init__(self, field_capacity=10):

        if field_capacity < 0 or field_capacity > 10:
            raise ValueError("field_capacity must be between 0 and 10.")

        self._field_capacity = field_capacity

        # Initialize moisture to the saturation point for the soil
        self._moisture = field_capacity / 10 * Soil.FC_MOISTURE_FT3

    @property
    def field_capacity(self):
        return self._field_capacity

    @property
    def moisture(self):
        return self._moisture

    @moisture.setter
    def moisture(self, value):
        max_moisture = self._field_capacity / 10 * Soil.FC_MOISTURE_FT3

        if value > max_moisture or value < 0:
            raise ValueError(f"Attempt to set moisture below 0 or above"
                             f" {max_moisture}.")

        self._moisture = value
