"""
This module contains the function open_config_file, which opens a configuration file and returns a dictionary with the configuration data.
"""

import yaml
import logging

def open_config_file(file_path):
    """
    Open a configuration file and return a dictionary

    @param file_path (str): The path to the configuration file to open
    @return dict: The configuration data extracted from the file
    """
    # Log a message that the configuration file is being opened
    logging.info(f"Opening configuration file: {file_path}")

    # Load the YAML configuration, which contains the required columns
    # Try to open the configuration file
    try:
        # Open the configuration file, in read mode, the path is hardcoded since the same configuration file is used for all ETL processes
        with open(file_path, 'r') as file:
            # Load the YAML file, and store it in a dictionary
            config_col = yaml.safe_load(file)
        # Log a message that the required columns were successfully loaded
        logging.info(f'Required columns succesfully extracted from configuration file.')
    
    # If the configuration file is not found, catch the FileNotFoundError exception
    except FileNotFoundError:
        # Log an error message
        logging.error(f"Configuration file not found: {file_path}")
        # Raise a FileNotFoundError
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    
    # Return the configuration data
    return config_col