from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

logger.info("Welcome to our ML proj. logging")

STAGE_NAME ="Data Ingestion Stage"

try:
    logger.info(f">>>stage {STAGE_NAME} started >>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> STAGE {STAGE_NAME} completed >>> X====X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_2 = "Data Validation Stage"

try:
    logger.info(f">>>>stage {STAGE_NAME_2} started <<<<")
    data_ingestion = DataValidationTrainingPipeline
    data_ingestion.main()
    logger.info(f">>>stage {STAGE_NAME_2} completed <<<<\n\nx=====x")
except Exception as e:
    raise e

STAGE_NAME_3 = "Data Transformation Stage"

try:
    logger.info(f">>>>stage {STAGE_NAME_3} started <<<<")
    data_transformation = DataTransformationTrainingPipeline
    data_transformation.main()
    logger.info(f">>>stage {STAGE_NAME_3} completed <<<<\n\nx=====x")
except Exception as e:
    raise e


STAGE_NAME_4 = "Model Trainer Stage"

try:
    logger.info(f">>>>stage {STAGE_NAME_4} started <<<<")
    model_training = ModelTrainerTrainingPipeline
    model_training.main()
    logger.info(f">>>stage {STAGE_NAME_3} completed <<<<\n\nx=====x")
except Exception as e:
    raise e

