import logging
import math
import random

import arborlife
from arborlife import config

logger = logging.getLogger(__name__)


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
        cfg = config.get_cfg("forest")
        density_init = cfg["density_init"]

        self._xdim = cfg["xdim"]
        self._ydim = cfg["ydim"]
        self._tiles, self._tree_tiles = [], []

        logger.debug(f"xdim: {self._xdim}, ydim: {self._ydim}")

        for x in range(self.xdim):
            for y in range(self.ydim):

                # Not every tile in the forest has a tree
                tree = arborlife.Tree() if random.random() <= density_init else None

                tile = arborlife.Tile(x, y, arborlife.Soil(), tree)
                self._tiles.append(tile)

                if tree is not None:
                    self._tree_tiles.append(tile)

        logger.debug(f"tree tiles: {len(self._tree_tiles)}, density: {self.density}")

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

        # No point clamping if invalid coordinate(s)
        if x < 0 or x >= self._xdim or y < 0 or y >= self._ydim:
            logger.error(f"find_tile called w/ out of bounds value: (x={x}, y={y})")
            raise(ValueError)

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
