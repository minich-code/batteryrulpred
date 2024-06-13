import json
from pathlib import Path
from dataclasses import dataclass
from src.BatteryRUL.utils.commons import read_yaml, save_json, create_directories
from src.BatteryRUL.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH, METRICS_FILE_PATH

@dataclass
class MetricsValidationConfig:
    root_dir: Path
    metric_file_name: Path
    validation_status_file: Path
    metrics_thresholds: dict
    

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH, 
        schema_filepath=SCHEMA_FILE_PATH, 
        metrics_filepath=METRICS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        self.metrics_thresholds = read_yaml(metrics_filepath)['METRICS']
       
        create_directories([self.config['artifacts_root']])

    def get_metrics_validation_config(self) -> MetricsValidationConfig:
        config = self.config['model_metrics_validation']
        
        create_directories([config['root_dir']])

        metrics_validation_config = MetricsValidationConfig(
            root_dir=Path(config['root_dir']),
            metric_file_name=Path(config['metric_file_name']),
            validation_status_file=Path(config['validation_status_file']),
            metrics_thresholds=self.metrics_thresholds,
            
        )
        return metrics_validation_config

class MetricsValidation:
    def __init__(self, config: MetricsValidationConfig):
        self.config = config
        
    def validate_metrics(self):
        """Validates the metrics in the metrics file against the thresholds."""
        metrics = read_yaml(self.config.metric_file_name)
        validation_results = self._validate(metrics)
        
        # Save validation results
        self.save_validation_results(validation_results) 

    def _validate(self, metrics: dict) -> dict:
        """Performs the validation of each metric."""
        validation_results = {}
        for metric_name, metric_value in metrics.items():
            thresholds = self.config.metrics_thresholds.get(metric_name)
            if thresholds is None:
                validation_results[metric_name] = {
                    "result": "Not Available",
                    "message": f"Thresholds for {metric_name} not defined in 'metrics_thresholds.yaml'."
                }
                continue  

            # Use the specified thresholds directly
            lower_bound = thresholds['min']
            upper_bound = thresholds['max']

            is_valid = lower_bound <= metric_value <= upper_bound

            validation_results[metric_name] = {
                "value": metric_value,
                "is_valid": is_valid,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "message": f"Metric value is {'within' if is_valid else 'outside'} acceptable bounds."
            }

        return validation_results
    
    def save_validation_results(self, validation_results: dict):
        """Saves the validation results to a JSON file."""
        save_json(self.config.validation_status_file, validation_results) 
        print(f"Validation results saved to: {self.config.validation_status_file}")

if __name__ == "__main__":
    try:
        # Initialize Configuration Manager
        config_manager = ConfigurationManager()
        metrics_validation_config = config_manager.get_metrics_validation_config()

        # Perform Model Validation
        metrics_validation = MetricsValidation(config=metrics_validation_config)
        validation_results = metrics_validation.validate_metrics()

    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
