from arborlife.tile import Tile
from arborlife.soil import Soil


def test_default_init():
    tile = Tile(0, 0, Soil())

    assert not tile.tree
    assert tile.x == 0
    assert tile.y == 0


def test_find_distance():
    t1 = Tile(x=0, y=0, soil=Soil())
    t2 = Tile(x=3, y=4, soil=Soil())
    assert t1.find_distance(t2) == 5 and t2.find_distance(t1) == 5
