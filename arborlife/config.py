import yaml
from pkg_resources import resource_filename

# TODO: Think long and hard about using YAML this way
ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
with open(ymlfilename) as ymlfile:
    cfg = yaml.safe_load(ymlfile)
