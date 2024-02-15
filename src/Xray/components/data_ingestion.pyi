import os
import sys

from Xray.entity.config_entity import DataIngestionConfig
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.cloud_storage.s3_operation import S3Openration
from Xray.utils.exception import CustomException
from Xray.utils.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        """_summary_

        Args:
            data_ingestion_config (DataIngestionConfig): _description_
        """        
        ...
    def get_data_from_s3(self)-> None:
        """_summary_

        Raises:
            CustomException: _description_
        """        
        ...
        
    def intitiate_data_ingestion(self)-> DataIngestionArtifact:
        """_summary_

        Raises:
            CustomException: _description_

        Returns:
            DataIngestionArtifact: _description_
        """        
        ...
    