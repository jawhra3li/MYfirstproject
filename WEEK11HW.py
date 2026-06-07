#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Transform
df["Qty"] = df["Qty"].fillna(0).astype(int)
df["Unit_Price"] = df["Unit_Price"].fillna(0).astype(float)

df["Total_Price"] = df["Qty"] * df["Unit_Price"]

print(df.head())


# In[2]:


import pandas as pd

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df["Qty"] = df["Qty"].fillna(df["Qty"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["CustomerID"] = df["CustomerID"].fillna("Unknown")

df["Qty"] = df["Qty"].astype(int)
df["Unit_Price"] = df["Unit_Price"].astype(float)

df["Total_Price"] = df["Qty"] * df["Unit_Price"]

print(df.head())


# In[3]:


import pandas as pd

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

print(df.columns)


# In[4]:


import pandas as pd

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# 1. Handling Missing Values (Imputation)
df["Qty"] = df["Qty"].fillna(df["Qty"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["CustomerID"] = df["CustomerID"].fillna("Unknown")

# 2. Data Types
df["Qty"] = df["Qty"].astype(int)
df["Unit_Price"] = df["Unit_Price"].astype(float)
df["SaleDate"] = pd.to_datetime(df["SaleDate"])

# 3. Feature Engineering
df["Total_Price"] = df["Qty"] * df["Unit_Price"]

# 4. Currency Conversion
OMR_RATE = 0.385
df["Total_Price_OMR"] = df["Total_Price"] * OMR_RATE

# 5. Text Cleaning
df["ProductName"] = df["ProductName"].str.strip().str.upper()

print(df.head())


# In[5]:


print(df["CurrencyType"].unique())


# In[6]:


df["CurrencyType"] = df["CurrencyType"].str.upper()


# In[7]:


df["CurrencyType"] = df["CurrencyType"].fillna("USD")


# In[8]:


df["CurrencyType"] = df["CurrencyType"].replace({
    "USD": "USD",
    "US D": "USD",
})


# In[9]:


rates = {
    "USD": 0.385,
    "OMR": 1
}


# In[10]:


df["Unit_Price_OMR"] = df.apply(
    lambda x: x["Unit_Price"] * rates.get(x["CurrencyType"], 0.385),
    axis=1
)

df["Total_Price_OMR"] = df["Qty"] * df["Unit_Price_OMR"]


# In[11]:


print(df[["CurrencyType", "Unit_Price", "Unit_Price_OMR"]].head())


# In[12]:


print(df.head())


# In[13]:


print(df.isnull().sum())


# In[14]:


print(df.dtypes)


# In[15]:


print(df[["CurrencyType", "Unit_Price_OMR", "Total_Price_OMR"]].head())


# In[16]:


print(df[df["Qty"] < 0])
print(df[df["Unit_Price"] < 0])


# In[17]:


print("Total rows:", len(df))


# In[18]:


pip install mysql-connector-python


# In[19]:


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",   
    database="RetailDB"
)

cursor = conn.cursor()


# In[22]:


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="RetailDB"
)

conn.autocommit = False
cursor = conn.cursor()

data = list(df[[
    "ProductName",
    "Qty",
    "Unit_Price",
    "SaleDate",
    "CurrencyType",
    "CustomerID",
    "StoreID",
    "Total_Price",
    "Total_Price_OMR"
]].itertuples(index=False, name=None))

query = """
INSERT INTO Sales (
    ProductName, Qty, Unit_Price, SaleDate,
    CurrencyType, CustomerID, StoreID,
    Total_Price, Total_Price_OMR
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

batch_size = 1000

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    cursor.executemany(query, batch)
    conn.commit()

cursor.close()
conn.close()


# In[25]:


import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="RetailDB"
    )

    if conn.is_connected():
        print("Connected successfully")

    conn.close()

except Exception as e:
    print("Connection failed:", e)


# In[26]:


import pandas as pd
import mysql.connector

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# الاتصال
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="RetailDB"
)

cursor = connection.cursor()

tables = ["Sales"]  # أو أي جدول عندك

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

for table in tables:
    print(f"Processing table: {table}")

    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, con=connection)

    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    if not numeric_columns and not categorical_columns:
        print(f"No data in {table}")
        continue

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_columns),
            ('cat', categorical_transformer, categorical_columns)
        ],
        remainder='drop'
    )

    transformed_data = preprocessor.fit_transform(df)

    cat_names = preprocessor.named_transformers_['cat']         .named_steps['encoder'].get_feature_names_out(categorical_columns)

    transformed_columns = numeric_columns + list(cat_names)

    transformed_df = pd.DataFrame(transformed_data, columns=transformed_columns)

    cursor.execute(f"DROP TABLE IF EXISTS {table}_transformed")

    create_table_query = f"""
    CREATE TABLE {table}_transformed (
        {', '.join([f"`{col}` DOUBLE" for col in transformed_columns])}
    )
    """
    cursor.execute(create_table_query)

    insert_query = f"""
    INSERT INTO {table}_transformed
    VALUES ({', '.join(['%s'] * len(transformed_columns))})
    """

    for row in transformed_df.itertuples(index=False):
        cursor.execute(insert_query, tuple(row))

    connection.commit()

print("Done")
cursor.close()
connection.close()


# In[ ]:




