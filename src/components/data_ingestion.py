import os
import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import CustomException
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_path = os.path.join("artifact", "raw.csv")
    train_path = os.path.join("artifact", "train.csv")
    test_path = os.path.join("artifact", "test.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting the Data Ingestion")
        try:
            """
            data = pd.read_csv("Raw_data_link")
            logging.info("Reading a df")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_path))
            data.to_csv(self.data_ingestion_config.raw_path, index=False)
            logging.info("I have saved the raw data in the artifact folder")

            logging.info("Performing the train-test split")

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("train-test split completed")

            train_data.to_csv(self.data_ingestion_config.train_path, index=False)
            test_data.to_csv(self.data_ingestion_config.test_path, index=False)

            logging.info("Ingestion part complete")

            return (
                self.data_ingestion_config.train_path,
                self.data_ingestion_config.test_path
            )
            """
            
            logging.info("Creating the artifact folder")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_path), exist_ok=True)

            self.train_data_link = "https://raw.githubusercontent.com/Harsh-Arya-exe/Gemstone-data/refs/heads/main/train.csv"
            self.test_data_link = "https://raw.githubusercontent.com/Harsh-Arya-exe/Gemstone-data/refs/heads/main/train.csv"

            self.train_data = pd.read_csv(self.train_data_link)
            self.test_data = pd.read_csv(self.test_data_link)

            logging.info("Saving the train and test files")
            self.train_data.to_csv(self.data_ingestion_config.train_path, index=False)
            self.test_data.to_csv(self.data_ingestion_config.test_path, index=False)

            return (
                self.data_ingestion_config.train_path,
                self.data_ingestion_config.test_path
            )

            logging.info("Data Ingestion Completed")
        except Exception as e:
            logging.info("Exception occured at Data Ingestion")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
