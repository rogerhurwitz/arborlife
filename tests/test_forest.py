from random import randrange

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


def test_find_tile_by_xy(forest):
    rx = randrange(0, forest.xdim)
    ry = randrange(0, forest.ydim)
    tile = forest.find_tile_by_xy(rx, ry)
    assert tile.x == rx and tile.y == ry


@pytest.mark.parametrize("radius", [0, 1, 2, 5, 5.5, 6])
def test_find_tiles_by_radius(forest, fcfg, radius):
    test_x = round(fcfg["xdim"] / 2)
    test_y = round(fcfg["ydim"] / 2)
    test_tile = forest.find_tile_by_xy(test_x, test_y)

    subject_tiles = forest.find_tiles_by_radius(test_tile, radius)

    observed_tiles = [
        tile for tile in forest.tiles if tile.find_distance(test_tile) <= radius]

    assert subject_tiles == observed_tiles
