"""
This module contains the functions to extract the data from a source file, 
verify if the file is in csv format, and check if it contains the expected columns.
"""

import pandas as pd
import logging
from etl_pipeline import setup_logging, open_config_file

def extract_data(data_file_path, config_file_path):
    """
    Extracts the data from a source file, verifies if the file is in csv format, and checks if it contains the expected columns. 
    Otherwise it exits with an exception.

    @param 
    - file_path (str): The path to the file to extract
    -config_file_path (str): The path to the configuration file, which contains the required columns
    
    @return pd.DataFrame: The data extracted from the file in a dataframe

    @exceptions:
    - ValueError: If the file is not a csv file
    - FileNotFoundError: If the file is not found
    - FileNotFoundError: If the configuration file is not found
    - ValueError: If the data is missing required columns
    """
    # Set up the logging configuration, for the ETL extract process
    setup_logging('extract')

    # Log a message that the extract process has started
    logging.info(f"Starting data extract process for: {data_file_path}")

    # Open the file
    data = open_data_file(data_file_path)
            
    # Open the configuration file, which contains the required columns
    config_col = open_config_file(config_file_path)

    # Access required columns
    required_columns = config_col['columns']['required_columns_to_load']
    
    # Validate if the data contains all the required 
    schema_validation(data, required_columns)

    # Return the data
    return data

def schema_validation(data, required_columns):
    """
    Validate if the data contains the required columns

    @param data (pd.DataFrame): The data extracted from the file in a dataframe
    @param required_columns (list): The list of required columns to validate
    """
    # Validate if the data contains all the required 
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.error(f"The file is missing required columns: {missing_columns}")
        raise ValueError(f"Schema validation failed. Missing columns: {missing_columns}")

    # Log a successful schema validation
    logging.info("Schema validation passed. All required columns are present.")

def open_data_file(file_path):
    """
    Open a file and return pandas DataFrame

    @param file_path (str): The path to the file to open
    @return pd.DataFrame: The data extracted from the file in a dataframe
    """
    # Log a message that the file is being opened
    logging.info(f"Opening file: {file_path}")

    # Check if the file is a csv file, if not a csv file, set an error message and raise a ValueError
    if not file_path.endswith('.csv'):
        # Log an error message
        logging.error(f"Invalid file type for file: {file_path}. Expected a csv file.")
        # Raise a ValueError
        raise ValueError(f"Invalid file type for file: {file_path}. Expected a csv file.")
        
    else:
        # Try to read the file
        try:
            # Load the data into a pandas DataFrame
            data = pd.read_csv(file_path)
            # Log a message that the data was successfully loaded
            logging.info(f"Data succesfully extracted from: {file_path}")

        # If the file is not found, catch the FileNotFoundError exception
        except FileNotFoundError:
            # Log an error message
            logging.error(f"File not found: {file_path}")
            # Raise a FileNotFoundError
            raise FileNotFoundError(f"File not found: {file_path}")
        
    # Return the file object
    return data