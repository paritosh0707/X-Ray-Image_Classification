import sys
from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.utils.exception import CustomException
from Xray.utils.logger import logging

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Enetred start_data_ingetion method of Training Pipeline")
        try:
            logging.info("getting data from S3 bucket")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.intitiate_data_ingestion()
            logging.info("got the train_set and test_set for S3 bucket")
            logging.info("exited the start_data_ingestion method of Training Pipeline")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    training_pipeline = TrainingPipeline()
    training_pipeline.start_data_ingestion()