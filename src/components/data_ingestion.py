import os
from src.logger.logger import logging


class DataIngestionConfig:
    raw_path = os.path.join("artifact", "raw.csv")
    train_path = os.path.join("artifact", "train.csv")
    test_path = os.path.join("artifact", "test.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting the Data Ingestion")
        self.train_data = "training_link"
        self.test_data = "testing_link"

        os.makedirs(os.path.join(os.getcwd(), "artifact"))

        logging.info("Saving the train and test files")
        self.train_data.to_csv(self.data_ingestion_config.train_path, index=False)
        self.test_data.to_csv(self.data_ingestion_config.test_path, index=False)

        logging.info("Data Ingestion Completed")
