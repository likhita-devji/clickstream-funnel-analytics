"""
ETL Pipeline
"""

import pandas as pd


class ETLPipeline:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def extract(self):
        """
        Load CSV dataset.
        """
        self.df = pd.read_csv(self.file_path)

        print(f"Dataset Loaded Successfully")
        print(f"Rows : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

        return self.df

    def preview(self):
        """
        Display first five records.
        """
        print(self.df.head())

    def information(self):
        """
        Display dataset information.
        """
        print(self.df.info())