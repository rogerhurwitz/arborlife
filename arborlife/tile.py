from arborlife import Soil
from math import hypot


class Tile:
    """The smallest addressable unit within a forest.

    Tiles are created in the process of creating the Forest and represent an
    x/y grid location within the Forest.  Furthermore, tiles are containers
    for entities that reside in the forest at the specified location such as an
    instance of Soil and (possibly) an instance of Tree.

    Attributes:
        soil (Soil): Common denominator for all tiles.  Defaults to Soil().
        tree (Tree): May or may not be present within a tile.  Defaults to None.
        x, y (ints): Coordinate location within a forest.  Each defaults to 0.
    """

    def __init__(self, soil=Soil(), tree=None, x=0, y=0):
        self.soil = soil
        self.tree = tree
        self.x = x
        self.y = y

    def find_distance(self, other):
        """Finds the distance between this tile and another tile in the forest"""
        dx = self.x - other.x
        dy = self.y - other.y
        return hypot(dx, dy)
