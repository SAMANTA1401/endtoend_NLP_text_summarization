from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.stage02_data_validation import DataValidation


class DataValidationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validates_all_files_exist()
        

if __name__=="__main__":
    try:
        obj = DataValidationPipeline()
        obj.main()
    except Exception as e:
        raise e