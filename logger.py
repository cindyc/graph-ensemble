# encoding: utf-8

__author__ = "Cindy Cao"
__email__ = "cindy@candidnarrative.com"

import os
import yaml
import logging
import logging.config

DEFAULT_LOG_NAME = 'graphensemble'

log_config_file = os.path.join(os.path.dirname(__file__), 'etc/logging.yaml')

with open(log_config_file, 'r') as log_config_yaml: 
    logging_config = yaml.load(log_config_yaml)
logging_config.setdefault('version', 1)
logging.config.dictConfig(logging_config)

def create_log(module_name='', class_name='', **specs):
    """Create a logger for a module or class specs
    """
    if not module_name and not class_name:
        name = DEFAULT_LOG_NAME
    else:
        name = '.'.join((module_name, class_name))
    return logging.getLogger(name)
