import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name, download_path):
    """
    Downloads a dataset from Kaggle to a specific path.

    Args:
        dataset_name (str): The name of the dataset in the format 'username/dataset-name'.
        download_path (str): The local path where the dataset will be downloaded.
    """
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)

    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download the dataset
    print(f"Downloading dataset '{dataset_name}' to '{download_path}'...")
    api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset downloaded and extracted to '{download_path}'.")

if __name__ == "__main__":
    # Define the dataset name and download path
    DATASET_NAME = "praanj/limit-orderbook-data"  # Replace with your dataset name
    DOWNLOAD_PATH = "./data"  # Replace with your desired download path

    # Download the dataset
    download_dataset(DATASET_NAME, DOWNLOAD_PATH)