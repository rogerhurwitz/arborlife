import numpy as np

from arborlife import config, utils

CANOPY_MASS_MAX = 99.0
CANOPY_MASS_MEAN = 60.0
CANOPY_MASS_MIN = 1.0
CANOPY_MASS_SD = 10.0
DBH_H_B0 = 3.84
DBH_H_B1 = 19.66
DBH_H_COEFFICENT = 0.38315
DBH_H_EXPONENT = 0.92045
HEIGHT_WIDTH_RATIO = 0.9
MAX_LEAF_CANOPY_PCT = 0.2
ROOT_CANOPY_PCT = 0.62
ROOT_CANOPY_PCT_MEAN = 0.60
WOOD_DENSITY_LB = 45.0


class Tree:
    """Tree is the star of the show.

    Attributes:
        age (float): Age of tree in years (1 day is 1/365). Initial age of
            tree is set using scipy.stats.truncnorm with settings from
            arborlife.yml config file.
        alive (bool): True if tree is alive else false.  Initial state of
            tree set with tree alive value in arborlife.yml
    """

    def __init__(self, age=None):
        tree_cfg = config.cfg["tree"]

        self.age = float(age) if age is not None else (
            utils.calc_truncnorm(
                mean=tree_cfg["age_init_mean"],
                sd=tree_cfg["age_init_sd"],
                clip_a=tree_cfg["age_init_min"],
                clip_b=tree_cfg["age_init_max"],
            )
        )
        # Trees don't shrink, but mass can, so need track max height
        self._height_max = 0

        # TODO: Need fxn to calculate canopy_mass steady state
        # 10 y/o tree canopy mass = 60kg, +/- 50kg each year away, min 10kg
        self.canopy_mass = max(10, 50 * self.age - 440)
        
        self.alive = True

    @property
    def green_weight(self):
        return self.canopy_mass + (MAX_LEAF_CANOPY_PCT * self.canopy_mass)

    @property
    def trunk_diameter(self):
        d2h = (self.green_weight / DBH_H_COEFFICENT) ** (1 / DBH_H_EXPONENT)
        return utils.calc_cubic(DBH_H_B1 / 12, DBH_H_B0 / 12, 0, -d2h)

    @property
    def height(self):
        self._height_max = max(
            self._height_max, (DBH_H_B0 + DBH_H_B1 * self.trunk_diameter) / 12)
        return self._height_max

    @property
    def bark_ft2(self):
        return self.height * 2 * np.pi * ((self.trunk_diameter / 12) / 2)

    @property
    def canopy_width(self):
        return HEIGHT_WIDTH_RATIO * self.height

    @property
    def root_mass(self):
        return ROOT_CANOPY_PCT * self.canopy_mass

    @property
    def root_radius(self):
        return ((self.root_mass / self.canopy_mass) / ROOT_CANOPY_PCT_MEAN) * self.canopy_width

    @property
    def root_area(self):
        return np.pi * self.root_radius ** 2

    @property
    def root_ft3(self):
        return self.root_mass / WOOD_DENSITY_LB

    @property
    def glucose_store(self):
        return self.canopy_mass * 1.85e25

    # @property
    # def canopy_mass(self):
    #     return utils.calc_truncnorm(
    #         CANOPY_MASS_MEAN, CANOPY_MASS_SD, CANOPY_MASS_MIN, CANOPY_MASS_MAX)
