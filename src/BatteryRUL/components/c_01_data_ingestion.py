import pandas as pd 
import pymongo
from pymongo import MongoClient 
import os 

from src.BatteryRUL.entity.configuration_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Method to fetch data from MongoDB
    def import_data_from_mongodb(self):
        # Connect to MongoDB
        client = pymongo.MongoClient(self.config.mongo_uri)
        db = client[self.config.database_name]
        collection = db[self.config.collection_name]

        # Convert the collection to a DataFrame
        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns:
            df = df.drop(columns=["_id"])

        # # Save the DataFrame to a CSV file in the root directory
        # output_path = self.config.root_dir / "data.csv"
        # df.to_csv(output_path, index=False)
        # logging.info(f"Data fetched from MongoDB and saved to {output_path}")

        #Save DataFrame to a file (optional, based on your needs)
        df.to_csv(os.path.join(self.config.root_dir, 'battery_rul.csv'), index=False)