import yaml


class Tree:
    """Tree is the star of the show.

    Attributes:
        age (float): Age of tree in years (1 day is 1/365).
        alive (bool): True if tree is alive else false.
    """

    # TODO: Think long and hard about using YAML this way
    with open("config/tree.yml") as ymlfile:
        cfgd = yaml.safe_load(ymlfile)

    def __init__(self, starting_age=cfgd["starting_age"], alive=cfgd["alive"]):

        self.age = starting_age
        self.alive = alive
