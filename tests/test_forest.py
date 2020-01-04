import math
import random

import pytest
import yaml
from pkg_resources import resource_filename

from arborlife import Forest


# Instantiating a Forest is expensive, so do it once for module
@pytest.fixture(scope="module")
def forest():
    return Forest()

# Avoid reading/parsing YAML file more than once
@pytest.fixture(scope="module")
def fcfg():
    ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
    with open(ymlfilename) as ymlfile:
        return yaml.safe_load(ymlfile)["forest"]


def test_default_init(forest, fcfg):
    assert forest.xdim == fcfg["xdim"] and forest.ydim == fcfg["ydim"]


def test_density(forest):
    assert forest.density == len(forest.tree_tiles) / (forest.xdim * forest.ydim)


def test_total_tiles(forest):
    assert len(forest.tiles) == forest.xdim * forest.ydim


def test_find_tile_random(forest):
    random.seed(0)
    x = random.randrange(0, forest.xdim)
    y = random.randrange(0, forest.ydim)
    tile = forest.find_tile(x, y)
    assert tile.x == x and tile.y == y


def test_find_tile_min(forest):
    x, y = 0, 0
    tile = forest.find_tile(x, y)
    assert tile.x == x and tile.y == y


def test_find_tile_max(forest):
    x, y = forest.xdim - 1, forest.ydim - 1
    tile = forest.find_tile(x, y)
    assert tile.x == x and tile.y == y


@pytest.mark.parametrize("x,y", [(-1, 0), (0, -1), (math.inf, 0), (0, math.inf)])
def test_find_tile_oob(forest, x, y):
    with pytest.raises(ValueError):
        forest.find_tile(x, y)


@pytest.mark.parametrize("seed", [0, 1, 5, 10])
def test_find_tiles_by_radius(forest, fcfg, seed):
    random.seed(seed)

    test_tile = forest._tree_tiles[random.randrange(0, len(forest.tree_tiles))]
    radius = random.randrange(1, 10)

    subject_tiles = forest.find_tiles_by_radius(test_tile, radius)

    observed_tiles = [
        tile for tile in forest.tiles if tile.find_distance(test_tile) <= radius]

    assert subject_tiles == observed_tiles
