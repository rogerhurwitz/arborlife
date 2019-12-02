import pytest
import yaml

from arborlife.tree import Tree


@pytest.fixture
def cfgd():
    with open("config/tree.yml") as ymlfile:
        return yaml.safe_load(ymlfile)


def test_default_init_good(cfgd):
    t = Tree()
    assert t.age == cfgd["starting_age"] and t.alive == cfgd["alive"]


def test_specified_init_good():
    t = Tree(starting_age=15, alive=False)
    assert t.age == 15 and not t.alive
