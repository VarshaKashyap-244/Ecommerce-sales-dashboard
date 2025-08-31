import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_monthly_sales(monthly):
    plt.figure(figsize=(10,5))
    plt.plot(monthly.index.astype(str), monthly['Revenue'], marker='o')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_top_products(top):
    fig = px.bar(top.reset_index(), x='Description', y='Revenue', title='Top Products by Revenue')
    fig.show()

def plot_customer_segments(customers):
    sns.countplot(x='Segment', data=customers)
    plt.title('Customer Segments')
    plt.show()
