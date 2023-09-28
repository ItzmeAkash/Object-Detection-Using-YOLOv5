from dataclasses import dataclass


# Return type of the Components 
@dataclass
class DataIngestionArtifact:
    data_zip_file_path:str
    feature_store_path:str