import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, cleaned_df, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold
        self.df = cleaned_df.copy()
    def is_safe(self):
        """
        Determine if a row of water data is safe.
        """
        self.df['is_safe'] = (
                (self.df['pH'].between(6.5, 8.5)) &
                (self.df['turbidity'] < 4)
        )
        return self.df
