import os
import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import CustomException
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.preprocessing import OrdinalEncoder, StandardScaler


@dataclass
class DataTransformationConfig:
    pass


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self):
        try:

            logging.info("Starting the Data Ingestion")
            self.train_data = "training_link"
            self.test_data = "testing_link"

            os.makedirs(os.path.join(os.getcwd(), "artifact"))

            logging.info("Saving the train and test files")
            self.train_data.to_csv(self.data_ingestion_config.train_path, index=False)
            self.test_data.to_csv(self.data_ingestion_config.test_path, index=False)

            logging.info("Data Ingestion Completed")
        except Exception as e:
            logging.info()
            raise CustomException(e, sys)
