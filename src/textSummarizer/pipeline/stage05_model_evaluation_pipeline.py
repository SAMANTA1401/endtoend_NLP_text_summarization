from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.stage05_model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()



if __name__=="__main__":
    try:
        modelevaluation = ModelEvaluationPipeline()
        modelevaluation.main()
    except Exception as e:
        raise e