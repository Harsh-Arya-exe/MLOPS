import sys
import os
import pandas as pd
from src.exception.exception import CustomException
from src.logger.logger import logging
from src.utils.utils import load_obj


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join('artifact', 'preprocessor.pkl')
            model_path = os.path.join('artifact', 'model.pkl')

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            scaled_features = preprocessor.transform(features)

            pred = model.predict(scaled_features)

            return pred

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self):
        pass

    def get_data_as_dataframe(self):
        pass