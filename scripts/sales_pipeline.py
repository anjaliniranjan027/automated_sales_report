
import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\automated_sales_report\\data\\raw_sales_data.csv", parse_dates=["Date"])


# Add Total Sales column
df["Total Sales"] = df["Units Sold"] * df["Unit Price"]

# Summary by Category
category_summary = df.groupby("Category")["Total Sales"].sum()

# Daily Sales Trend
daily_sales = df.groupby("Date")["Total Sales"].sum()

# Top Products
top_products = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False)

# Save cleaned data
df.to_excel("C:/Users/lenovo/OneDrive/Desktop/automated_sales_report/reports/weekly_sales_report.xlsx", index=False)

# Plot category summary
plt.figure(figsize=(6,4))
category_summary.plot(kind="bar", color="skyblue")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("C:/Users/lenovo/OneDrive/Desktop/automated_sales_report/reports/sales_by_category.png")
plt.close()

# Plot daily trend
plt.figure(figsize=(6,4))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("C:/Users/lenovo/OneDrive/Desktop/automated_sales_report/reports/daily_sales_trend.png")
plt.close()

# Plot top products
plt.figure(figsize=(6,4))
top_products.plot(kind="pie", autopct='%1.1f%%')
plt.title("Top Selling Products")
plt.ylabel("")
plt.tight_layout()
plt.savefig("C:/Users/lenovo/OneDrive/Desktop/automated_sales_report/reports/top_products_pie.png")
plt.close()

print("Report generated successfully.")
