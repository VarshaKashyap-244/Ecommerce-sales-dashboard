import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='ISO-8859-1')
    return df

def clean_data(df):
    df.dropna(subset=['CustomerID'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    return df

if __name__ == "__main__":
    df = load_data('../data/ecommerce_data.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('../data/ecommerce_data_cleaned.csv', index=False)
