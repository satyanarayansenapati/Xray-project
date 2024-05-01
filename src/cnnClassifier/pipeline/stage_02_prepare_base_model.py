from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        '''Getting the configuration'''

        #creating an object of ConfigurationManager
        x = ConfigurationManager()
        
        #getting the configuration details
        prepare_base_model_config = x.get_prepare_base_model_config()


        '''Creating the model'''

        #initializing an object of PrepareBaseModel
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)

        #getting the base model
        prepare_base_model.get_base_model()

        #updating the base model
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e