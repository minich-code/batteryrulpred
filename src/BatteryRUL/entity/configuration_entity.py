from dataclasses import dataclass 
from pathlib import Path
import pymongo
from pymongo import MongoClient 
import pandas as pd
import os 

# Data Ingestion Entity 
@dataclass()
class DataIngestionConfig:
    root_dir: Path
    mongo_uri: str
    database_name: str
    collection_name: str


# Data validation entity 
@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    data_dir: Path
    all_schema: dict 

# Data Transformation entity 
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    numerical_cols: list
    categorical_cols: list


# Model trainer entity 
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    # XGBOOST parameters 
    objective: str  
    booster: str
    n_estimators: int
    learning_rate: float
    max_depth: int
    min_child_weight: int
    gamma: float
    subsample: float
    colsample_bytree: float
    reg_alpha: float
    reg_lambda: float
    random_state: int
    scale_pos_weight: int

# Model Evaluation Entity
@dataclass()
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    test_target_variable: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str


# Metrics validation 
@dataclass
class MetricsValidationConfig:
    root_dir: Path
    metric_file_name: Path
    validation_status_file: Path
    metrics_thresholds: dict
    
