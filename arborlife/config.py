import logging

import yaml
from pkg_resources import resource_filename


def initialize_package():

    global cfg

    # TODO: Remove hard-coding, add error checking
    ymlfilename = resource_filename("arborlife", "config/arborlife.yml")
    with open(ymlfilename) as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    # Package-level logging initialization
    logging.basicConfig(level=cfg["logging"]["level"])
