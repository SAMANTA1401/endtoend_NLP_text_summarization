from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.stage03_data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()



if __name__=="__main__":
    try:
        datatransform = DataTransformationPipeline()
        datatransform.main()
    except Exception as e:
        raise e
