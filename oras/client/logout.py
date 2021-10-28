__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MIT"

import oras.defaults as defaults
from oras.logger import logger
from oras.main.config import AuthConfig
import os
import sys

def resolve_hostname(hostname):
    """
    Return the docker index server given an alias, otherwise return hostname as is
    """
    if hostname in [defaults.registry.index_hostname, defaults.registry.index_name, defaults.registry.default_v2_registry['host']]:
        return defaults.registry.index_server
    return hostname

def main(args, parser, extra, subparser):

    hostname = resolve_hostname(args.hostname)

    config = None
    for path in [os.path.expanduser("~/.docker/config.json"), os.path.expanduser("~/.dockercfg")]:
        if os.path.exists(path):
            config = path
            break

    # A user specified config over-rides default
    # This will exit with clear message if the config does not exist
    config = AuthConfig(args.config or config)
    config.logout(hostname)
