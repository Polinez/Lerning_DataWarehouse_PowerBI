#ELT
from src.extract_data import download_data_from_kaggle
from src.load_data_to_db import load_to_db
from src.transform_data_in_db import transform_in_db

#ML scripts
from src.preprocessing import clean_and_prepare_features
from src.train_model import train_and_score

import pandas as pd

'''
This is a main script to make ELT pipeline in local environment. The Cloud version is in notebooks/
'''
def run_pipeline():
    # Extract
    print("\nStarting pipeline: Fetching raw data...")
    data_dir = download_data_from_kaggle()

    # Load
    print("\nLoading raw data to the database...")
    load_to_db(data_dir)

    # Transform
    print("\nCleaning and preparing features in db...")
    transform_in_db()

if __name__ == "__main__":
    run_pipeline()