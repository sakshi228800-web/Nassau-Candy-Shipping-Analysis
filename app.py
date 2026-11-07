
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nassau Candy Shipping Dashboard",
    page_icon="",
    layout="wide"
)

st.title("Factory-to-Customer Shipping Route Efficiency")
st.subheader("Nassau Candy Distributor — Data Analytics Project")

# Load dataset
df = pd.read_csv("nassau_cleaned.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].dropna().unique()),
    default=sorted(df["Region"].dropna().unique())
)

shipping_modes = st.sidebar.multiselect(
    "Select Shipping Mode",
    options=sorted(df["Ship Mode"].dropna().unique()),
    default=sorted(df["Ship Mode"].dropna().unique())
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Ship Mode"].isin(shipping_modes))
]

# KPI cards
st.header("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Shipping Records", f"{len(filtered_df):,}")
col2.metric("Unique Orders", f"{filtered_df['Order ID'].nunique():,}")
col3.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col4.metric("Total Units", f"{filtered_df['Units'].sum():,}")

# Regional analysis
st.header("Regional Shipping Analysis")

regional = (
    filtered_df.groupby("Region")
    .agg(Shipping_Records=("Order ID", "count"))
    .reset_index()
)

fig1 = px.bar(
    regional,
    x="Region",
    y="Shipping_Records",
    title="Shipping Volume by Region"
)

st.plotly_chart(fig1, use_container_width=True)

# Shipping mode analysis
st.header("Shipping Mode Analysis")

mode_data = (
    filtered_df.groupby("Ship Mode")
    .agg(Shipping_Records=("Order ID", "count"))
    .reset_index()
)

fig2 = px.pie(
    mode_data,
    names="Ship Mode",
    values="Shipping_Records",
    title="Distribution of Shipping Modes"
)

st.plotly_chart(fig2, use_container_width=True)

# Product analysis
st.header("Product Performance")

product_data = (
    filtered_df.groupby("Product Name")
    .agg(Total_Sales=("Sales", "sum"))
    .reset_index()
    .sort_values("Total_Sales", ascending=False)
)

fig3 = px.bar(
    product_data,
    x="Product Name",
    y="Total_Sales",
    title="Sales by Product"
)

st.plotly_chart(fig3, use_container_width=True)

# Shipping lead time
st.header("Shipping Lead Time")

st.warning(
    "Lead-time results are provisional. The dataset contains unusual "
    "date ranges that must be verified before drawing delivery-efficiency conclusions."
)

if "Lead Time" in filtered_df.columns:
    lead_data = (
        filtered_df.groupby("Ship Mode")["Lead Time"]
        .mean()
        .reset_index()
    )

    fig4 = px.bar(
        lead_data,
        x="Ship Mode",
        y="Lead Time",
        title="Average Lead Time by Shipping Mode (Provisional)"
    )

    st.plotly_chart(fig4, use_container_width=True)

# Raw data
st.header("Explore Shipping Records")
st.dataframe(filtered_df, use_container_width=True)

st.caption("Project: Factory-to-Customer Shipping Route Efficiency Analysis")
