from src.DownloadData import download_data_from_kaggle
from src.preprocessing import clean_and_prepare_features
from src.train_model import train_and_score
import pandas as pd


def run_pipeline():
    # 1. Data Ingestion
    print("Starting pipeline: Fetching raw data...")
    data_dir = download_data_from_kaggle()



if __name__ == "__main__":
    run_pipeline()