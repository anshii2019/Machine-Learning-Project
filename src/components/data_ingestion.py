import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
# from src.mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingeation_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading code
            df=pd.read_csv("notebooks\data\data.csv")
            logging.info("Reading completed mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df._to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df._to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df._to_csv(self.ingestion_config.test_data_path,index=False,header=True)
        
            logging.info("Data ingestion completed")

            return(
                self.ingeation_config.train_data_path,
                self.ingeation_config.test_data_path,
            )

        except Exception as e:
            logging.info('Error occured while initiating data ingestion')
            raise CustomException(e,sys)


if __name__=='__main__':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    