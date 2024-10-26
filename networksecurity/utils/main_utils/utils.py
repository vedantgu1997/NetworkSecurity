import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle


def read_yaml_file(file_path):
    try:
        logging.info("Entered the read_yaml_file method of MainUtils class")
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
        logging.info("Exited the read_yaml_file method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def write_yaml_file(file_path, content, replace=True):
    try:
        logging.info("Entered the write_yaml_file method of MainUtils class")
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                yaml.dump(content, file)
        logging.info("Exited the write_yaml_file method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_numpy_array_data(file_path, array):
    try:
        logging.info("Entered the save_numpy_array_data method of MainUtils class")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, array)
        logging.info("Exited the save_numpy_array_data method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e