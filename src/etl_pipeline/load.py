"""
This module contains the function to load the transformed data into a SQLite database.
"""

import sqlite3
import logging
from setup_log import setup_logging

def load_data(data, db_path):
    """
    Load the transformed data into a SQLite database

    @param data (pd.DataFrame): The transformed data to load
    @param db_path (str): The path to the SQLite database
    """
    # Set up the logging configuration, for the ETL load process
    setup_logging('load')

    # Log a message that the load process has started
    logging.info("Starting data load process")

    try:
        # Connect to SQLite database (this will create a new file if it doesn't exist)
        conn = sqlite3.connect(db_path)

        # Create a table in SQLite dynamically from the DataFrame columns if it doesn't exist
        # Using `to_sql` automatically handles table creation if it doesn't exist.
        data.to_sql('customers', conn, if_exists='replace', index=False)

        # Commit the transaction
        conn.commit()
        logging.info(f"Data successfully loaded into database at {db_path}")
    except Exception as e:
        logging.error(f"Error during data load: {e}")
    finally:
        # Close the database connection
        conn.close()