import logging

import yaml
from pkg_resources import resource_filename

_cfg = None


def get_cfg(section=None):

    global _cfg

    if _cfg is None:

        ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
        with open(ymlfilename) as ymlfile:
            _cfg = yaml.safe_load(ymlfile)

        # Package-level logging initialization
        # logging.basicConfig(level=_cfg["logging"]["level"])
        logging.basicConfig(level=logging.DEBUG)

    return _cfg if section is None else _cfg[section]
