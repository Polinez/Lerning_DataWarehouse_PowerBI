from dotenv import load_dotenv
import os
import json
import kagglehub

# load environment variables from .env file
load_dotenv()

def download_data_from_kaggle():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '..', 'config.json')

    # Set up Kaggle dataset download path from config.json
    with open(config_path, 'r') as file:
        config = json.load(file)

    os.environ['KAGGLEHUB_CACHE'] = config['DATA_DIR']

    # Download the dataset using kagglehub
    path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

    print("Path to dataset files:", path)
    return path