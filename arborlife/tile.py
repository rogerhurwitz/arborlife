import math
import arborlife as al


class Tile:
    """The lowest level addressable container within a forest.

    Tiles are created in the process of creating the Forest and represent an
    x/y grid location within it.  Furthermore, tiles are containers for
    entities within the forest at the specified location such as an instance of
    Soil and (possibly) an instance of Tree.

    Attributes:
        x, y (int): Coordinate location of a tile within the forest.
        tree (Tree): A tree may or may not be present within a tile.
    """

    def __init__(self, x, y, tree=None):
        self.x = x
        self.y = y
        self.tree = tree
        self.soil = al.Soil()

    def find_distance(self, other, math_hypot=math.hypot):
        """Finds the distance between this tile and another tile in the forest.

        Args:
            other (Tile): The tile to which the distance is to be measured.
            math_hypot (function): Ignore: for lookup optimization purposes.
        """
        return math_hypot(self.x - other.x, self.y - other.y)
