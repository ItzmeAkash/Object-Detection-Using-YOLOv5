import os
import sys
import zipfile
import gdown
from wasteDetection.logger import logging
from wasteDetection.exception import AppExceptio
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppExceptio(e, sys)
        
        
    def download_data(self) -> str:
        '''
        Fetch data from the url
        '''
        
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok= True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(F"Downloading data from {dataset_url} into file {zip_file_path}")
            
            
            file_id = dataset_url.split("/")[-2]
            perfix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(perfix+file_id,zip_file_path)
            
            
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")
            
            return zip_file_path
        
        except Exception as e:
            raise AppExceptio (e, sys)
        
        
    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function return None
        """
        
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
                
            logging.info(f"Extracting zip file: {zip_file_path} into dir:  {feature_store_path}")
            
            return feature_store_path
        except Exception as e:
            raise AppExceptio(e, sys)
        
    def initiate_Data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_Data_ingestion method of Data ingestion Class")
        
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)
            
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path = zip_file_path,
                feature_store_path = feature_store_path
            )
            
            logging.info("Exited initiate data ingestion method of Data ingestion class")
            logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppExceptio(e, sys)