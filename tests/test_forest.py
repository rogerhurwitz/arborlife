import random

import pytest
import yaml
from pkg_resources import resource_filename

from arborlife import Forest


@pytest.fixture(scope="module")
def forest():
    return Forest()


@pytest.fixture(scope="module")
def fcfg():
    ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
    with open(ymlfilename) as ymlfile:
        return yaml.safe_load(ymlfile)["forest"]


def test_default_init(forest, fcfg):
    assert forest.xdim == fcfg["xdim"] and forest.ydim == fcfg["ydim"]


def test_density(forest):
    tree_count = sum(1 for tile in forest._tree_tiles if tile.tree.alive)
    assert forest.density == tree_count / (forest.xdim * forest.ydim)


def test_tiles(forest):
    assert len(forest.tiles) == forest.xdim * forest.ydim


def test_find_tile(forest):
    random.seed(0)
    rx = random.randrange(0, forest.xdim)
    ry = random.randrange(0, forest.ydim)
    tile = forest.find_tile(rx, ry)
    assert tile.x == rx and tile.y == ry


@pytest.mark.parametrize("seed", [0, 1, 5, 10])
def test_find_tiles_by_radius(forest, fcfg, seed):
    random.seed(seed)

    test_tile = forest._tree_tiles[random.randrange(0, len(forest.tree_tiles))]
    radius = test_tile.tree.radius

    subject_tiles = forest.find_tiles_by_radius(test_tile, radius)

    observed_tiles = [
        tile for tile in forest.tiles if tile.find_distance(test_tile) <= radius]

    assert subject_tiles == observed_tiles
