import os
import yaml
from box.exceptions import BoxValueError
from mlProject import logger
import json
from pathlib import Path
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
import joblib

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    """reads yaml file and returns
       Args :
            path_to_yaml (str) : path like input
       Raises:
            ValueError : if yaml file is empty
            e: empty file
        Returns:
            ConfigBox : ConfigBox type
    """

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    #  creates list of create_directories
    #  Args : path_to_directories (list)
    #  verbose : Boolean
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path:Path, data:dict):
    # save json File
    # Args:
    #   path(Path): Path to json File
    #   data(dict): data to be saved in json file 

    with open(path,"w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Saved json file: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    # load json files data 
    # Args:
    #    path (Path): path to json file
    # Return:
    #   ConfigBox : data as class attributes instead of dict

    with open(path) as f:
        content = json.load(f)
    logger.info(f"Loaded json file successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def get_size(path:Path) -> str:
    # get size in KB
    # Args:
    #    path (Path): path of the file
    # Return:
    #    str : size in KB
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"~{size_in_KB} KB"
    
    


