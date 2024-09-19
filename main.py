from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion_pipeline import DataIngestionPipeline



STAGE_NAME1 = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME1} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx======x")
except Exception as e:
    raise e






