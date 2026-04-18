
from src.extract_data import download_data_from_kaggle

'''
This pipline is only for downloading row data, data was transformed using databricks 
Next i wanna to use power BI, and build a ML model on top of this data
'''
def run_pipeline():
    print("\nStarting pipeline: Fetching raw data...")
    data_dir = download_data_from_kaggle()
if __name__ == "__main__":
    run_pipeline()