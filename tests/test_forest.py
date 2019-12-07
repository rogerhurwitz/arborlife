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
    assert forest.density == len(forest.trees) / (forest.xdim * forest.ydim)


def test_tiles(forest):
    assert len(forest.tiles) == forest.xdim * forest.ydim


def test_find_tile(forest):
    rx = randrange(0, forest.xdim)
    ry = randrange(0, forest.ydim)
    tile = forest.find_tile(rx, ry)
    assert tile.x == rx and tile.y == ry
