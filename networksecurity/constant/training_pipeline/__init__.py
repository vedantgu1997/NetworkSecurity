import os
import sys
import numpy as np
import pandas as pd
'''
Training Pipeline Constants
'''
TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = 'NetworkSecurity'
ARTIFACTS_DIR: str = 'Artifacts'
FILE_NAME: str = 'PhishingData.csv'
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
SCHEMA_FILE_PATH: str = os.path.join('data_schema','schema.yaml')

'''
Data Ingestion Constants
'''
DATA_INGESTION_COLLECTION_NAME: str = "PhishingData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

'''
Data Validation Constants
'''
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "valid"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

'''
Data Transformation Constants
'''

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed_data"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformation_object"
PREPROCESSING_OBJECT_FILE_NAME: str = 'preprocessor.pkl'

#knn imputer params
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    'missing_values': np.nan,
    'n_neighbors': 3,
    'weights': 'uniform'
}