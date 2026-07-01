import pandas as pd

# ==========================================
# Day 1 & 2: Load and Explore Data
# ==========================================
# Load the dataset
df = pd.read_csv('sales.csv')

print("--- Data Info ---")
print(f"Dataset Shape: {df.shape}")
print(df.info())

# ==========================================
# Day 3: Clean Data
# ==========================================
# Handling missing values (if any)
df = df.dropna()

# Removing duplicates
df = df.drop_duplicates()

# ==========================================
# Day 4 & 5: Analyze Sales & Metrics
# ==========================================
# 1. Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2. Best-Selling Product (by Quantity)
product_qty = df.groupby('Product')['Quantity'].sum()
best_selling_product = product_qty.idxmax()
best_selling_qty = product_qty.max()

# 3. Additional Metric 1: Average Order Value (AOV)
avg_order_value = df['Total_Sales'].mean()

# 4. Additional Metric 2: Region-wise Total Sales
region_sales = df.groupby('Region')['Total_Sales'].sum()

# 5. Additional Metric 3: Highest Revenue Generating Product
product_revenue = df.groupby('Product')['Total_Sales'].sum()
top_revenue_product = product_revenue.idxmax()

# Print Results
print("\n--- Sales Analysis Report ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product (by Qty): {best_selling_product} ({best_selling_qty} units sold)")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")
print(f"Highest Revenue Product: {top_revenue_product} (₹{product_revenue.max():,.2f})")
print("\nRegional Sales Breakdown:")
print(region_sales.to_string())