import os

class DataIngestion:
    def __init__(self):
        self.train_data_path = os.path.join("data/raw", "train.csv")
        self.test_data_path = os.path.join("data/raw", "test.csv")