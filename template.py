import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Xray"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/cloud_storage/__init__.py",
    f"src/{project_name}/cloud_storage/s3_operation.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/training_pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/model/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    ".github/workflows/ci.yaml",
    ".github/workflows/main.yaml",
    "test/unitTest/__init__.py",
    "test/integrationTest/__init__.py",
    "bentofile.yaml",
    "init_setup.sh",
    "setup.cfg",
    "tox.ini",
    "main.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "Notebook/experiment.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")