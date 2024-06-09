import numpy as np
import pandas as pd

def load_dataset(file_path):
    """
    Load a dataset from a given file path.
    """
    return pd.read_csv(file_path)

def preprocess_data(data):
    """
    Preprocess the dataset, e.g., handle missing values, normalize, etc.
    """
    # Dummy preprocessing step
    data.fillna(0, inplace=True)
    return data
