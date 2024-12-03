import logging
import pandas as pd
from src.etl_pipeline.extract import extract_data
from src.etl_pipeline.transform import transform
from src.etl_pipeline.load import load_data
from setup_log import setup_logging

def etl(data_file_path, config_file_path, db_path):
    """
    Extracts, transforms, and loads the data from a source file to a SQLite database

    @param data_file_path (str): The path to the file to extract
    @param config_file_path (str): The path to the configuration file
    @param db_path (str): The path to the SQLite database
    """
    # Set up the logging configuration, for the ETL process
    setup_logging('etl')

    # Log a message that the ETL process has started
    logging.info("Starting ETL process")

    # Extract the data
    data = extract_data(data_file_path, config_file_path)

    # Transform the data
    transformed_data = transform(data, config_file_path)

    # Load the transformed data into the SQLite database
    load_data(transformed_data, db_path)

    # Log a message that the ETL process has ended
    logging.info("ETL process completed")