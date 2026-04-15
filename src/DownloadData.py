from dotenv import load_dotenv
import os
import json
import kagglehub

# load environment variables from .env file
load_dotenv()

def download_data_from_kaggle():
    # Set up Kaggle dataset download path from config.json
    with open('../config.json', 'r') as plik:
        config = json.load(plik)

    os.environ['KAGGLEHUB_CACHE'] = config['DATA_DIR']

    # Check if dataset already exists before downloading
    if os.path.exists(config['DATA_DIR']):
        print(f"Dataset already exists at \"{config['DATA_DIR']}\"  Skipping download.")
        return config['DATA_DIR']

    # Download the dataset using kagglehub
    path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

    print("Path to dataset files:", path)
    return path