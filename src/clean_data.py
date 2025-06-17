import pandas as pd
import numpy as np

def clean_sensor_data(df):

    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """

    cleaned_df = df.copy()

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce') #What does error =' coerce' do?
                                                                        #It will ignore all non-numeric values

    # pH should be 0-14, set invalid to NaN first
    df.loc[~df['pH'].between(0, 14), 'pH'] = np.nan

    # turbidity should be non negative.
    df.loc[df['turbidity'] < 0, 'turbidity'] = np.nan

    # dissolved oxygen should be non negative.
    df.loc[df['dissolved_oxygen'] < 0, 'dissolved_oxygen'] = np.nan

    # temperature assuming we expect -10°C to 50°C
    df.loc[~df['temperature'].between(-10, 50), 'temperature'] = np.nan

    # Fill missing values forward
    cleaned_df = df.ffill()

    return cleaned_df
