from arborlife import Tile, Soil, Tree


def test_default_init():
    tile = Tile()

    assert not tile.tree
    assert isinstance(tile.soil, Soil)
    assert tile.x == 0
    assert tile.y == 0


def test_specified_init():
    tree = Tree()
    soil = Soil()

    tile = Tile(soil, tree, x=1, y=2)

    assert tile.tree is tree
    assert tile.soil is soil
    assert tile.x == 1
    assert tile.y == 2


def test_find_distance():
    t1 = Tile(x=0, y=0)
    t2 = Tile(x=3, y=4)
    assert t1.find_distance(t2) == 5 and t2.find_distance(t1) == 5
