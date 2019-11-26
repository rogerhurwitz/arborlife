from decimal import Decimal  # noqa: F401


class Soil:
    """Soil takes in and gives out resources within its capacity limits.

    Constants:
        FC_MOISTURE_FT3 -- Represents the maximum number of molecules of water
            per cubic foot that soil can hold assuming maximum field_capacity.

    Attributes:
        field_capacity -- A dimensionless number between 0 and 10 representing
            the most saturated the soil can be (10 = 100%).  Defaults to 10.
        moisture -- Current amount of soil moisture.  Must be between 0 and
            maximum capacity defined as field_capacity / 10 * FC_MOISTURE_FT3
        moisture_gauge -- A read-only value between 0 and 10 representing the
            the ratio of current moisture to moisture capacity:
            moisture_gauge = field_capacity * (moisture / FC_MOISTURE_FT3)
    """

    FC_MOISTURE_FT3 = 1.18 * 10e26
    MIN_FC, MAX_FC = 0, 10

    # TODO: Close w/ Neil on whether we need enhanced precision/accuracy
    # FC_MOISTURE_FT3 = Decimal("1.18") * Decimal("10e26")

    def __init__(self, field_capacity=MAX_FC):

        if field_capacity < Soil.MIN_FC or field_capacity > Soil.MAX_FC:
            raise ValueError(f"field_capacity must be between {Soil.MIN_FC}"
                             f" and {Soil.MAX_FC}.")

        self._field_capacity = field_capacity

        # TODO: Close w/ Neil on allowing specified moisture initialization
        self._moisture = field_capacity / Soil.MAX_FC * Soil.FC_MOISTURE_FT3

    @property
    def field_capacity(self):
        return self._field_capacity

    @property
    def moisture_gauge(self):
        return self._field_capacity * (self._moisture / Soil.FC_MOISTURE_FT3)

    @property
    def moisture(self):
        return self._moisture

    @moisture.setter
    def moisture(self, value):
        max_moisture = (self._field_capacity / Soil.MAX_FC *
                        Soil.FC_MOISTURE_FT3)

        if value > max_moisture or value < 0:
            raise ValueError(f"Attempt to set moisture below 0 or above"
                             f" {max_moisture}.")

        self._moisture = value
