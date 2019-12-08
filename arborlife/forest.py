import math
from random import random

import arborlife as al
import arborlife.config as config


class Forest:
    """Maintains state of all objects within an adressable cartesian space.

    Attributes:
        xdim(int): Read only extent of the forest along its x axis.
        ydim(int): Read only extent of the forest along its y axis
        density(float): Read only percentage of forest tiles w/ living trees.
        tree_tiles(list): List of all tiles w/ trees in the forest.
        tiles(list): List of all tiles in the forest.
    """

    def __init__(self):
        """Creates forest using arborlife.yml forest initialization parameters."""
        self._xdim = config.cfg["forest"]["xdim"]
        self._ydim = config.cfg["forest"]["ydim"]
        self._density = config.cfg["forest"]["density_init"]
        self._tree_tiles = []

        self._tiles = [
            al.Tile(x=x, y=y) for x in range(self.xdim) for y in range(self.ydim)
        ]
        # Using specified initial tree density, populate forest with trees
        for tile in self._tiles:
            if random() <= self._density:
                tile.tree = al.Tree()
                self._tree_tiles.append(tile)

    @property
    def xdim(self):
        return self._xdim

    @property
    def ydim(self):
        return self._ydim

    @property
    def density(self):
        return sum(1 for tile in self._tree_tiles if tile.tree.alive) / len(self._tiles)

    @property
    def tree_tiles(self):
        return self._tree_tiles

    @property
    def tiles(self):
        return self._tiles

    def find_tile(self, x, y):
        """Finds and returns the forest tile at the specified x/y location."""
        return self._tiles[x * self._xdim + y]

    def find_tiles_by_radius(self, center_tile, radius):
        """Returns list of tiles within radius of center_tile including center_tile"""

        # Specify a (clipped) bounding box big enough for area covered by radius
        x_origin = max(center_tile.x - math.floor(radius), 0)
        x_extent = min(center_tile.x + math.floor(radius) + 1, self._xdim)
        y_origin = max(center_tile.y - math.floor(radius), 0)
        y_extent = min(center_tile.y + math.floor(radius) + 1, self._ydim)

        tiles_by_radius = []

        # Iterate over bounding box collecting tiles w/in radius of center
        for x in range(x_origin, x_extent):
            for y in range(y_origin, y_extent):
                test_tile = self.find_tile(x, y)
                if test_tile.find_distance(center_tile) <= radius:
                    tiles_by_radius.append(test_tile)

        return tiles_by_radius
