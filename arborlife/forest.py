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
        return self.tiles[x * self.xdim + y]
