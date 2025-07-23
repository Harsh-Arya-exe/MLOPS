import os
from src.logger.logger import logging
from src.exception.exception import CustomException
import sys
from dataclasses import dataclass
from src.utils.utils import save_object, evaluate_model
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifact', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Splitting Dependent and Independent variables")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "LinearRegression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "ElasticNet": ElasticNet(),
                "RandomForestRegressor": RandomForestRegressor(),
                "xgboost": XGBRegressor()
            }

            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print("\n=======================================================")
            logging.info(f'Model Report: {model_report}')

            # To get the best model score from dictionary
            best_model_name = max(model_report, key=model_report.get)

            best_model = models[best_model_name]

            print(f'Best Model Found, Model Name: {best_model}')
            print("\n===================================================")
            logging.info(f"Best Model Found, Model Name: {best_model}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            logging.info("Exception occured at Model Training")
            raise CustomException(e, sys)
