from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.stage04_model_trainer import ModelTrainer



class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()



if __name__=="__main__":
    try:
        modeltrainer = ModelTrainerPipeline()
        modeltrainer.main()
    except Exception as e:
        raise e