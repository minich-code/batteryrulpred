from src.BatteryRUL.config.configuration import ConfigurationManager
from src.BatteryRUL.components.c_06_metrics_validation import MetricsValidation
from src.BatteryRUL import logging 
import joblib 
import pandas as pd 



PIPELINE_NAME = "MODEL METRICS VALIDATION PIPELINE"


class ModelMetricsValidationPipeline:
    def __init__(self):
        pass 


    def main(self):
        # Initialize Configuration Manager
        config_manager = ConfigurationManager()
        metrics_validation_config = config_manager.get_metrics_validation_config()

        # Perform Model Validation
        metrics_validation = MetricsValidation(config=metrics_validation_config)
        validation_results = metrics_validation.validate_metrics()
        logging.info(validation_results)
        



if __name__=="__main__":
    try:
        logging.info(f"# ============== {PIPELINE_NAME} Started ================#")
        metrics_validation_pipeline = ModelMetricsValidationPipeline()
        metrics_validation_pipeline.main()
        logging.info(f"# ============= {PIPELINE_NAME} Terminated Successfully ! ===========\n\nx******************x") 
    except Exception as e:
        logging.exception(e)
        raise e
