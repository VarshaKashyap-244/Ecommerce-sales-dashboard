def format_currency(num):
    return f"${num:,.2f}"

def add_revenue_column(df):
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df
