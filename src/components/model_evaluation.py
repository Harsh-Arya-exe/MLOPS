import os
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from src.logger.logger import logging
from src.exception.exception import CustomException
import sys
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_model

@dataclass
class ModelEvaluationConfig:
    raw_path = os.path.join("artifact", "raw.csv")
    train_path = os.path.join("artifact", "train.csv")
    test_path = os.path.join("artifact", "test.csv")


class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e, sys)
