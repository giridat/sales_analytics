import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("superstore.csv",encoding="latin1")


print("csv loaded. Rows:", len(df) )

engine = create_engine(
        "postgresql://postgres:admin@localhost:5432/superstore_data"
)

df.to_sql("orders",engine,if_exists="replace",index=False)

print("Table 'orders' created and data imported successfully!")
