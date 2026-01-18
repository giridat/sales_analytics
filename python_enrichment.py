# load data from postgresoql instead of csv
# rename messy columns to snake_case
# Convert dates
# Create new analytical features by converting date getting profit margins
# handle infinite values and missing values
import pandas as pd
from sqlalchemy import create_engine


# .1 Load data
engine = create_engine(
        "postgresql://postgres:admin@localhost:5432/superstore_data"
)

query = 'select * FROM orders'
df = pd.read_sql(query,engine)

print("Rows loaded from DB:", len(df))

# 2. Rename messy columns to snake_case

df = df.rename(columns={
    "Row ID": "row_id",
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Ship Date": "ship_date",
    "Customer ID": "customer_id",
    "Customer Name": "customer_name",
    "Product Name": "product_name",
    "Sub-Category": "sub_category"
})

#3. convert dates
df["order_date"] = pd.to_datetime(df["order_date"], format="%m/%d/%Y")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%m/%d/%Y")
#4. new analytics features
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()

df["profit_margin"] = (df["Profit"]/df["Sales"]) * 100

# 5. Handle infinite / missing values
df.replace([float("inf"), float("-inf")],0,inplace=True)
df.fillna(0,inplace=True)

df.to_csv("cleaned_superstore.csv",index=False)

print("Cleaned dataset saved as cleaned_superstore.csv")




