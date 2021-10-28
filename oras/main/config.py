__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from oras.logger import logger
from oras.utils import read_json, write_json
import os

class AuthConfig:

    def __init__(self, config_path):
        if not os.path.exists(config_path):
            logger.exit("%s does not exist." % config_path)
        self.config_path = config_path        
        self._config = read_json(config_path)
        if "auths" not in self._config:
            logger.exit("auths key missing in config.")

    def logout(self, name):
        """
        Determine if a hostname exists in the config.
        
        Removing the hostname from the config (I think) is logging out.
        """
        if name in self._config['auths']:
            logger.info("Logging out of %s" % name)
            del self._config['auths'][name]
            write_json(self._config, self.config_path)    


