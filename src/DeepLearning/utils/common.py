import os
from box.exceptions import BoxValueError
from src.DeepLearning import logger
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            config = ConfigBox(config)
            logger.info(f"yaml file loaded from {path_to_yaml}")
            return ConfigBox(config)

    except BoxValueError as e:
        logger.error(f"error in reading yaml file {e}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def load_json(path:Path)->dict:
    with open(path,"r") as f:
        data=json.load(f)
    logger.info(f"json file loaded from {path}")
    return ConfigBox(data)

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at {path}")

# @ensure_annotationsz
# def 


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())