import pandas as pd

def monthly_sales(df):
    df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('YearMonth').agg({'Quantity': 'sum', 'UnitPrice': 'mean'})
    monthly['Revenue'] = monthly['Quantity'] * monthly['UnitPrice']
    return monthly

def top_products(df, n=10):
    top = df.groupby('Description').agg({'Quantity': 'sum', 'Revenue': lambda x: (x * df['UnitPrice']).sum()})
    return top.sort_values('Revenue', ascending=False).head(n)

def customer_segments(df):
    customers = df.groupby('CustomerID').agg({'Revenue': 'sum', 'InvoiceNo': 'nunique'})
    customers['Segment'] = pd.qcut(customers['Revenue'], q=4, labels=['Low', 'Mid', 'High', 'VIP'])
    return customers

if __name__ == "__main__":
    df = pd.read_csv('../data/ecommerce_data_cleaned.csv', parse_dates=['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    print(monthly_sales(df))
    print(top_products(df))
    print(customer_segments(df))
