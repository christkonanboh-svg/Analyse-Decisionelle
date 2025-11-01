import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load_and_filter(self, budget=500000):
        df = pd.read_csv(self.path)
        df = df[(df['cost'] > 0) & (df['cost'] <= budget)].reset_index(drop=True)
        df['profit'] = df['cost'] * (df['profit_pct'] / 100)
        self.df = df
        return df
