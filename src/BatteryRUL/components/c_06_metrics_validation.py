import json
from pathlib import Path
from dataclasses import dataclass
from src.BatteryRUL.utils.commons import read_yaml, save_json, create_directories
from src.BatteryRUL.entity.configuration_entity import MetricsValidationConfig



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
