from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.stage02_data_validation_pipeline import DataValidationPipeline
from textSummarizer.pipeline.stage03_data_transformation_pipeline import DataTransformationPipeline


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

