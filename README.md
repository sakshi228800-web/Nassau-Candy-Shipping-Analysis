# Nassau-Candy-Shipping-Analysis
# Factory-to-Customer Shipping Route Efficiency Analysis

### Nassau Candy Distributor | Data Analytics Project

## 1. Project Overview

This project analyses the distribution and sales operations of Nassau Candy Distributor using Python and data analytics techniques.

The objective is to understand product performance, factory contributions, regional demand and factory-to-customer distribution activity. The analysis aims to provide useful business insights that can support better logistics and distribution planning.

## 2. Project Objectives

- Analyse sales and product performance.
- Identify factory-wise order activity.
- Examine regional and state-wise demand.
- Analyse factory-to-region distribution activity.
- Identify high-volume and low-volume routes.
- Develop meaningful business KPIs.
- Build an interactive Streamlit dashboard.

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Google Colab
- GitHub

## 4. Dataset Description

The project uses the Nassau Candy Distributor dataset.

The dataset contains information about:

- Order ID and order dates
- Shipping dates and shipping modes
- Customer details
- Country, state and city
- Product names and product IDs
- Sales, units, cost and gross profit

## 5. Analytical Methodology

1. Dataset loading and inspection.
2. Data-quality assessment.
3. Exploratory Data Analysis (EDA).
4. Product-to-factory mapping.
5. Factory-wise performance analysis.
6. Regional and state-wise demand analysis.
7. Factory-to-region route analysis.
8. KPI development.
9. Interactive dashboard development.

## 6. Factory Analysis

The project includes five factories:

- Lot's O' Nuts
- Wicked Choccy's
- Sugar Shack
- Secret Factory
- The Other Factory

Products were mapped to their respective factories using the factory information provided in the project assignment.

## 7. Key Performance Indicators

The project evaluates:

- Total order lines
- Unique orders
- Unique customers
- Total sales
- Total units sold
- Total factories
- Total products
- Sales per unique order
- Factory-wise order activity
- Factory-to-region order-line volume

## 8. Important Data Limitation

During date validation, the supplied order dates ranged from 2024 to 2025, while shipping dates ranged from 2026 to 2030.

This produced unusually large calculated lead times. Since the original date values could not be independently verified, no arbitrary date corrections were applied.

Therefore, shipping lead time and delivery-delay conclusions are treated as unvalidated and are not used to make confirmed delivery-efficiency claims.

Accurate customer coordinates were also unavailable, so precise geographical route distances were not calculated.

## 
