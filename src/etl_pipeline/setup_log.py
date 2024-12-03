"""
This module contains the function to set up the logging configuration for the ETL processes
"""

import logging
import os
import yaml

def setup_logging(log_section):
    """
    Set up the logging configuration dynamically for various ETL processes

    @param log_section: str, the section of the logging configuration to use
    """
    config_path = '/Users/akram/DataScienceProjects/customer-churn-prediction/configuration/etl/logging_paths.yaml'
    with open(config_path, 'r') as file:
        log_config = yaml.safe_load(file)

    path = log_config['etl'][log_section]
    log_dir = os.path.dirname(path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=path,
        filemode='w'
    )