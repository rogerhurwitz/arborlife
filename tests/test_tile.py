from arborlife import Tile, Soil, Tree


def test_default_init():
    t = Tile()
    assert isinstance(t.soil, Soil) and not t.tree and t.x == 0 and t.y == 0


def test_specified_init():
    t = Tile(None, Tree(), 1, 2)
    assert isinstance(t.tree, Tree) and not t.soil and t.x == 1 and t.y == 2


def test_find_distance():
    t1 = Tile(x=0, y=0)
    t2 = Tile(x=3, y=4)
    assert t1.find_distance(t2) == 5 and t2.find_distance(t1) == 5
