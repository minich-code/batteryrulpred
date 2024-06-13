from src.BatteryRUL import logging
from src.BatteryRUL.pipelines.pip_01_data_ingestion import DataIngestionPipeline
from src.BatteryRUL.pipelines.pip_02_data_validation import DataValidationPipeline
from src.BatteryRUL.pipelines.pip_03_data_transformation import DataTransformationPipeline
from src.BatteryRUL.pipelines.pip_04_model_trainer import ModelTrainerPipeline
from src.BatteryRUL.pipelines.pip_05_model_evaluation import ModelEvaluationPipeline
from src.BatteryRUL.pipelines.pip_06_metrics_validation import ModelMetricsValidationPipeline





COMPONENT_01_NAME = "DATA INGESTION COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_01_NAME} Started! ================================= #")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logging.info(f"## ======================== {COMPONENT_01_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e


COMPONENT_02_NAME = "DATA VALIDATION COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_02_NAME} Started! ================================= #")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logging.info(f"## ======================== {COMPONENT_02_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e



COMPONENT_03_NAME = "DATA TRANSFORMATION COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_03_NAME} Started! ================================= #")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logging.info(f"## ======================== {COMPONENT_03_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e


COMPONENT_04_NAME = "MODEL TRAINER COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_04_NAME} Started! ================================= #")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logging.info(f"## ========================  {COMPONENT_04_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e


COMPONENT_05_NAME = "MODEL EVALUATION COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_05_NAME} Started! ================================= #")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logging.info(f"## ======================== {COMPONENT_05_NAME} Terminated Successfully!======================= ##\n\nx******************x")
except Exception as e:
    logging.exception(e)
    raise e


COMPONENT_06_NAME = "MODEL METRICS VALIDATION COMPONENT"
try:
    logging.info(f"# ====================== {COMPONENT_06_NAME} Started! ================================= #")
    model_metrics_validation_pipeline = ModelMetricsValidationPipeline()
    model_metrics_validation_pipeline.main()
    logging.info(f"## ======================== {COMPONENT_06_NAME} Terminated Successfully!======================= ##\n\nx******************x")
except Exception as e:
    logging.exception(e)
    raise e
