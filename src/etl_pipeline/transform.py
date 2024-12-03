"""
This module contains the functions to transform the data by normalizing, label encoding, and one hot encoding the columns in the data.
"""

import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from src.etl_pipeline import setup_logging, open_config_file

def transform(data, config_file):
    """
    Transforms the data by normalizing, label encoding, and one hot encoding the columns in the data.
    The columns to normalize, label encode, and one hot encode are loaded from the configuration file.

    @param data (pd.DataFrame): The data to transform
    @param config_file (str): The path to the configuration file
    @return pd.DataFrame: The transformed data
    """
    # Set up the logging configuration, for the ETL transform process
    setup_logging('transform')

    # Log a message that the transform process has started
    logging.info("Starting data transform process")

    # Open the configuration file, which contains the columns
    config_columns = open_config_file(config_file)
    
    # Access the columns from the configuration file
    columns_to_change_from_object_to_numeric = config_columns['columns']['columns_to_change_from_object_to_numeric']
    columns_one_hot_encode = config_columns['columns']['columns_one_hot_encode']
    columns_label_encode = config_columns['columns']['columns_label_encode']
    columns_to_normalize = config_columns['columns']['columns_to_normalize']
    # Columns that depend on another column, these columns will be label encoded
    columns_that_depend_on_another_column = config_columns['columns']['columns_that_depend_on_another_column']

    # Change the columns from object to numeric
    data[columns_to_change_from_object_to_numeric] = data[columns_to_change_from_object_to_numeric].apply(pd.to_numeric, errors='coerce')

    # Fill missing values with zero value for the columns that will be converted to numeric, since empty means no information about the customer, which means no charges has been made
    data[columns_to_change_from_object_to_numeric] = data[columns_to_change_from_object_to_numeric].fillna(0)

    # Normalize the columns
    data = normalize(data, columns_to_normalize)

    # Label encode independent columns
    data = label_encode(data, columns_label_encode)

    # One hot encode the columns
    data = one_hot_encode(data, columns_one_hot_encode)

    # Label encode columns that depend on another column
    data = label_encode(data, columns_that_depend_on_another_column)
    
    # Log a message that the transform process has ended
    logging.info("Data transform process completed")

    # Return the transformed data
    return data

def label_encode(data, columns_to_label_encode):
    """
    Label encodes the columns in the data, using the LabelEncoder.
    Label encoding is used for columns that are ordinal, meaning the data has a meaningful order.

    @param data (pd.DataFrame): The data to label encode
    @param columns_to_label_encode (list): The columns to label encode
    @return pd.DataFrame: The data with the label encoded columns
    """
    # Log a message that the label encoding process has started
    logging.info("Starting label encoding process")

    # Initialize the LabelEncoder object
    label_encoder = LabelEncoder()
    # Label encode the columns
    data[columns_to_label_encode] = data[columns_to_label_encode].apply(label_encoder.fit_transform)

    # Log a message that the label encoding process has ended
    logging.info("Label encoding process completed")

    # Return the data with the label encoded columns
    return data

def one_hot_encode(data, columns_to_one_hot_encode):
    """
    One hot encodes the columns in the data, using the get_dummies method.
    One hot encoding is used for columns that are nominal, meaning the data has no meaningful order.

    @param data (pd.DataFrame): The data to one hot encode
    @param columns_to_one_hot_encode (list): The columns to one hot encode
    @return pd.DataFrame: The data with the one hot encoded columns
    """
    # Log a message that the one hot encoding process has started
    logging.info("Starting one hot encoding process")

    # One hot encode the columns
    data = pd.get_dummies(data, columns=columns_to_one_hot_encode, dtype=int)

    # Log a message that the one hot encoding process has ended
    logging.info("One hot encoding process completed")

    # Return the data with the one hot encoded columns
    return data

def normalize(data, columns_to_normalize):
    """
    Normalizes the columns in the data, using the MinMaxScaler
    Normalization is chosen over standardization because the data's difference is meaningful 
    and the data is not normally distributed. 

    @param data (pd.DataFrame): The data to normalize
    @param columns_to_normalize (list): The columns to normalize
    @return pd.DataFrame: The data with the normalized columns
    """
    # Log a message that the normalization process has started
    logging.info("Starting normalization process")

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    # Normalize the columns
    data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

    # Log a message that the normalization process has ended
    logging.info("Normalization process completed")

    # Return the data with the normalized columns
    return data