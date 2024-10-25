import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

uri = os.getenv('MONGO_DB_URL')

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return f'Inserted {len(self.records)} records successfully'
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == '__main__':
    FILE_PATH = 'Network_Data/phishingData.csv'
    DATABASE = 'NetworkSecurity'
    COLLECTION = 'PhishingData'

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(FILE_PATH)
    print(networkobj.insert_data_mongodb(records, DATABASE, COLLECTION))