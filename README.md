# etl-for-customer-analysis

ETL Pipeline for Data Transformation and Loading

This project demonstrates an **Extract, Transform, Load (ETL)** pipeline built with Python. It extracts data from source files, transforms it for consistency and usability, and loads it into a SQLite database. This pipeline is modular and uses best practices for logging, configuration management, and error handling.

## 🚀 Features

- **Modular Architecture**: Separates extraction, transformation, and loading processes into individual modules.
- **Error Handling**: Validates schema and file formats with detailed logging and error messages.
- **Dynamic Configuration**: Uses YAML configuration files for flexible management of pipeline parameters.
- **Data Transformation**: Implements:
  - Normalization with `MinMaxScaler`.
  - Label encoding for ordinal data.
  - One-hot encoding for nominal data.
- **Database Integration**: Automatically creates and populates SQLite tables.

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Required libraries: `pandas`, `scikit-learn`, `pyyaml`, `sqlite3`

## 📂 Project Structure:
```
  .
  ├── configuration              # Configuration files for ETL and modeling
  │   ├── etl                    # ETL-specific configurations
  │   │   ├── columns.yaml       # Column-specific transformation rules
  │   │   └── logging_paths.yaml # Paths for log files
  │   └── model                  # Model-specific configurations
  │       └── model_config.yaml  # Configuration for model training
  ├── data                       # Data directory
  │   ├── raw                    # Raw data files
  │   └── data_warehouse         # Processed data ready for analysis or modeling
  ├── logs                       # Log files
  │   ├── etl                    # Logs related to ETL processes
  │   └── eda                    # Logs related to exploratory data analysis
  ├── notebooks                  # Jupyter notebooks for EDA and ETL
  │   ├── etl                    # ETL-specific notebooks
  │   │   └── etl_pipeline_demo.ipynb
  │   └── eda                    # EDA-specific notebooks
  │       └── eda_analysis.ipynb
  ├── src                        # Source code
  │   ├── etl_pipeline           # ETL pipeline code
  │   │   ├── extract.py         # Handles data extraction and validation
  │   │   ├── transform.py       # Handles data transformations
  │   │   ├── load.py            # Handles data loading into SQLite database
  │   └── model                  # Model-related code
  │       ├── train_model.py     # Training machine learning models
  │       └── evaluate_model.py  # Model evaluation scripts
  ├── README.md                  # Project documentation
  ├── requirements.txt           # Python dependencies
  └── main.py                    # Entry point for running the ETL pipeline
```

## 🔑 Usage
##### Running the ETL Pipeline

To execute the ETL pipeline:
```
python etl.py --data_file_path <data-file> --config_file_path <config-file> --db_path <database-path>
```

##### Example:
```
python etl.py --data_file_path data/raw/customers.csv --config_file_path configuration/etl/columns.yaml --db_path data/data_warehouse/customers.db
```

## ETL Flow

	1.	Extract: Validates and loads CSV data into a Pandas DataFrame.
	2.	Transform:
	              •	Converts data types.
	              •	Handles missing values.
	              •	Applies normalization, label encoding, and one-hot encoding.
	3.	Load: Inserts transformed data into a SQLite database.

## 📝 Configuration

The pipeline uses YAML configuration files:
	•	columns.yaml: Specifies columns for transformation (e.g., normalization, encoding).
	•	logging_paths.yaml: Defines paths for log files for each process (e.g., extract.log, transform.log).

 
##### Example YAML file (columns.yaml):
```
columns:
  columns_to_change_from_object_to_numeric:
    - total_charges
    - monthly_charges
  columns_label_encode:
    - contract_type
  columns_one_hot_encode:
    - payment_method
  columns_to_normalize:
    - tenure
```

## 📈 Logs

Logs are automatically generated during the pipeline execution:
	•	extract.log
	•	transform.log
	•	load.log

 ##### Example log snippet:
 ```
 2024-12-03 10:15:20,123 - extract - INFO - Data successfully extracted from: data/customers.csv
```

## 🛡️ Error Handling

	•	Missing Columns: Validates against required schema.
	•	File Not Found: Gracefully handles missing files with descriptive errors.
	•	Invalid File Format: Only supports .csv.



