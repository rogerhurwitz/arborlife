from arborlife.config import cfg
from scipy.stats import truncnorm


class Tree:
    """Tree is the star of the show.

    Attributes:
        age (float): Age of tree in years (1 day is 1/365). Initial age of
            tree is set using scipy.stats.truncnorm with settings from
            arborlife.yml config file.
        alive (bool): True if tree is alive else false.  Initial state of
            tree set with tree alive value in arborlife.yml
    """

    def __init__(self):
        tcfg = cfg["tree"]

        def compute_starting_age():
            # Uses truncnorm (versus norm) to bracket starting tree age range
            clip_a, clip_b = tcfg["age_init_min"], tcfg["age_init_max"]
            mean, std = tcfg["age_init_mean"], tcfg["age_init_std"]
            a, b = (clip_a - mean) / std, (clip_b - mean) / std
            return truncnorm.rvs(a=a, b=b, loc=mean, scale=std)

        def compute_starting_radius(age):
            # Uses truncnorm (versus norm) to bracket starting tree radius range
            # 10 y/o has r mean 4, sd 1. +/- 1 per year from 10 y/o mean, min mean 2.
            mean, std = max(2, age - 6), 1
            clip_a, clip_b = 2, tcfg["age_init_max"] - 6
            a, b = (clip_a - mean) / std, (clip_b - mean) / std
            return truncnorm.rvs(a=a, b=b, loc=mean, scale=std)

        self.age = compute_starting_age()
        self.radius = compute_starting_radius(self.age)
        self.alive = tcfg["alive"]
