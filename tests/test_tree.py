import pytest
import yaml

from arborlife.tree import Tree
from pkg_resources import resource_filename


@pytest.fixture(scope="module")
def tcfg():
    ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
    with open(ymlfilename) as ymlfile:
        return yaml.safe_load(ymlfile)["tree"]


def test_init_age(tcfg):
    tree_ages = [Tree().age for _ in range(1000)]
    assert (
        min(tree_ages) >= tcfg["age_init_min"]
        and max(tree_ages) <= tcfg["age_init_max"])


def test_init_alive(tcfg):
    assert Tree().alive == tcfg["alive"]
