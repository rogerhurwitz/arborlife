import numpy as np
from scipy import stats

from arborlife import config


class Tree:
    """Tree is the star of the show.

    Attributes:
        age (float): Age of tree in years (1 day is 1/365). Initial age of
            tree is set using scipy.stats.truncnorm with settings from
            arborlife.yml config file.
        alive (bool): True if tree is alive else false.  Initial state of
            tree set with tree alive value in arborlife.yml
        canopy_mass (float): TBD
    """

    def __init__(self):
        tree_cfg = config.cfg["tree"]

        self.age = self._calc_initial_age(
            tree_cfg["age_init_min"],
            tree_cfg["age_init_max"],
            tree_cfg["age_init_mean"],
            tree_cfg["age_init_sd"],
        )
        # 10 y/o tree canopy mass = 60kg, +/- 50kg each year away, min 10kg
        self.canopy_mass = max(10, 50 * self.age - 440)
        self.alive = True

    def _calc_initial_age(self, min_age, max_age, mean, sd):
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
        clip_b = np.inf if max_age is None else max_age
        clip_a = -np.inf if min_age is None else min_age
        return stats.truncnorm.rvs(
            a=(clip_a - mean) / sd, b=(clip_b - mean) / sd, loc=mean, scale=sd
        )
