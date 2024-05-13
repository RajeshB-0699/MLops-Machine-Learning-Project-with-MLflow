from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 

logger.info("Welcome to our ML proj. logging")

STAGE_NAME ="Data Ingestion Stage"

try:
    logger.info(f">>>stage {STAGE_NAME} started >>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    loggger.info(f">>> STAGE {STAGE_NAME} completed >>> X====X")
except Exception as e:
    logger.exception(e)
    raise e

