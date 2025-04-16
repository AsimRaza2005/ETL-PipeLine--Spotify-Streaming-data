
import os
import kaggle
import requests

kaggle_username = os.getenv("KAGGLE_USERNAME")
kaggle_key = os.getenv("KAGGLE_KEY")
# Download the dataset

# Define the dataset
dataset = "atharvasoundankar/spotify-global-streaming-data-2024"
kaggle.api.dataset_download_files(dataset, path="./data", unzip=True)

print("Dataset downloaded successfully!")


