# model/data_loader.py
import pandas as pd

def load_dataset(path, budget=500000):
    df = pd.read_csv(path)
    df = df[(df['cost'] > 0) & (df['cost'] <= budget)].reset_index(drop=True)
    df['profit'] = df['cost'] * (df['profit_pct'] / 100)
    return df