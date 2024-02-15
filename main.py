import sys

from Xray.utils.exception import CustomException
from Xray.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        training_pipeline = TrainingPipeline()

        training_pipeline.run_pipeline()

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    start_training()