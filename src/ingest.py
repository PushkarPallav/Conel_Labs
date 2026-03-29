import pandas as pd

def load_data(file_path):
    return pd.read_json(file_path, lines=True)

def preprocess(df):
    # Convert timestamps safely
    df['ts'] = pd.to_datetime(df['ts'], errors='coerce')

    # Drop rows where timestamp is missing
    df = df.dropna(subset=['ts']).copy()

    # Fill only string columns
    for col in df.select_dtypes(include='object').columns:
        df.loc[:, col] = df[col].fillna("unknown")

    return df