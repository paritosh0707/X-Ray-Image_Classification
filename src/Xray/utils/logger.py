import logging
import os
from Xray.constants.training_pipeline import TIMESTAMP

LOG_FILE = f"{TIMESTAMP}.log"

log_path = os.path.join(os.getcwd(),"logs",TIMESTAMP)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)