import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_db(data_dir):
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "olist_warehouse")

    # start connection to the database
    db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(db_url)

    print(f"[Connecting] to the database: {db_name} on the {host} hosting server...\n")

    # Load each CSV file into the database
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(data_dir, file_name)

            # Renaming the table (e.g., “olist_orders_dataset.csv” -> “bronze_orders”)
            clean_name = file_name.replace("olist_", "").replace("_dataset.csv", "").replace(".csv", "")
            table_name = f"bronze_{clean_name}"

            print(f"[Uploading] the file {file_name} to the table ‘{table_name}’...")
            try:
                df = pd.read_csv(file_path)

                df.to_sql(table_name, engine, if_exists='replace', index=False)
            except Exception as e:
                print(f"[Error] uploading {file_name}: {e}")


