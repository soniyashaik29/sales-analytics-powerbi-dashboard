import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Samsung Global Sales Dashboard")

# Load data
df = pd.read_csv("data/samsung_global_sales_dataset.csv")

# Region Filter
region = st.selectbox("Select Region", df["region"].unique())

filtered = df[df["region"] == region]

# KPI Metrics
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue ($)", round(filtered["revenue_usd"].sum(), 2))
col2.metric("Total Units Sold", int(filtered["units_sold"].sum()))
col3.metric("Average Customer Rating", round(filtered["customer_rating"].mean(), 2))

# Revenue by Product
st.subheader("Revenue by Product")

product_sales = filtered.groupby("product_name")["revenue_usd"].sum().reset_index()

fig1 = px.bar(product_sales, x="product_name", y="revenue_usd", title="Revenue by Product")

st.plotly_chart(fig1)

# Category Distribution
st.subheader("Sales by Category")

category_sales = filtered.groupby("category")["revenue_usd"].sum().reset_index()

fig2 = px.pie(category_sales, names="category", values="revenue_usd")

st.plotly_chart(fig2)

# Monthly Sales Trend
st.subheader("Monthly Revenue Trend")

trend = filtered.groupby("month")["revenue_usd"].sum().reset_index()

fig3 = px.line(trend, x="month", y="revenue_usd")

st.plotly_chart(fig3)

# Show Data
st.subheader("Filtered Data")

st.dataframe(filtered)