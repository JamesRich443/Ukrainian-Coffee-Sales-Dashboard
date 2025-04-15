import logging
import azure.functions as func
import kaggle
import pandas as pd
import io
import os
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.timer_trigger(schedule="0 59 23 * * 0", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def UkranianCoffeeSales(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    # Authenticate with Kaggle API
    kaggle.api.authenticate()

    # Define dataset
    dataset_name = 'ihelon/coffee-sales'
    download_path = './coffee_data'

    # Ensure the download directory exists
    os.makedirs(download_path, exist_ok=True)

    # Download and unzip the dataset
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

    # List CSV files
    csv_files = [f for f in os.listdir(download_path) if f.endswith(".csv")]
    csv_files = csv_files[::-1]
    dataframes = []

    for file in csv_files:
        file_path = os.path.join(download_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

    # Combine and convert currency
    final_df = pd.concat(dataframes, ignore_index=True)
    exchange_rate = 0.024218368
    final_df['money'] = final_df['money'] * exchange_rate

    # Convert to CSV in memory
    output = io.StringIO()
    final_df.to_csv(output, index=False)
    output.seek(0)

    # Upload to Azure Blob Storage
    storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=jamesinit;AccountKey=eyZeAzdSSx928RGbCYFznSYMOpvm8ulQIU+EqKSC61DN9o1TmSIMhVlBGgV6Sm7u9HRRjBdBg5hU+AStzbKl+Q==;EndpointSuffix=core.windows.net"
    container_name = "jamesinitcontainer"
    blob_name = "coffee_data.csv"
    
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(output.getvalue(), overwrite=True)

    logging.info("✅ CSV uploaded to Azure Blob Storage successfully.")