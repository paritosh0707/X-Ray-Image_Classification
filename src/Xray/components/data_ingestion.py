import os
import sys

from Xray.entity.config_entity import DataIngestionConfig
from Xray.cloud_storage.s3_operation import S3Openration
from Xray.utils.exception import CustomException
from Xray.utils.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Openration()

    def get_data_from_s3(self):
        try:
            logging.info("Entered the get_data_from_s3 method of the DataIngestion class")
            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
                bucket_name=self.data_ingestion_config.bucket_name
            )
            logging.info("Exited the get_data_from_s3 method of the DataIngestion class")
        except Exception as e:
            raise CustomException(e,sys)
        
    def intitiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    