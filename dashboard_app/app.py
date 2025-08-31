import streamlit as st
import pandas as pd
from src.data_preprocessing import load_data, clean_data
from src.analysis import monthly_sales, top_products, customer_segments
from src.visualizations import plot_monthly_sales, plot_top_products, plot_customer_segments
from src.utils import add_revenue_column

st.title("E-Commerce Sales Analysis Dashboard")

data_path = 'data/ecommerce_data.csv'
df = load_data(data_path)
df = clean_data(df)
df = add_revenue_column(df)

# Monthly Sales
monthly = monthly_sales(df)
st.subheader("Monthly Revenue")
st.line_chart(monthly['Revenue'])

# Top Products
top = top_products(df)
st.subheader("Top Products by Revenue")
st.dataframe(top)

# Customer Segments
customers = customer_segments(df)
st.subheader("Customer Segments")
st.bar_chart(customers['Segment'].value_counts())
