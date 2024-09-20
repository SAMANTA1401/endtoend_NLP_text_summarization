from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.stage02_data_validation_pipeline import DataValidationPipeline
from textSummarizer.pipeline.stage03_data_transformation_pipeline import DataTransformationPipeline
from textSummarizer.pipeline.stage04_model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME1 = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME1} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx======x")
except Exception as e:
    raise e



STAGE_NAME2 = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME2} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME2} completed <<<<<<\n\nx======x")

except Exception as e:
    raise e


STAGE_NAME3 = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME3} started <<<<<<")
    datatransform = DataTransformationPipeline()
    datatransform.main()
    logger.info(f">>>>>> stage {STAGE_NAME3} completed <<<<<<\n\nx======x")

except Exception as e:
    raise e


STAGE_NAME4 = "Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME4} started <<<<<<")
    modeltrainer = ModelTrainerPipeline()
    modeltrainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME4} completed <<<<<<\n\nx======x")

except Exception as e:
    raise e



