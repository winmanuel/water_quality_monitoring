import pandas as pd

def load_csv(filepath):
    """
    Load sensor data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df



#if __name__ == "__main__":
#   df = load_csv(r"C:\Users\FIEK X\Documents\GitHub\water_quality_monitoring\data\sensor_data.csv")
#   print("Data loaded successfully.")
#   print(df)
