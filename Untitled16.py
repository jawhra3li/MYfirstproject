#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)
print(sys.executable)


# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip --version')


# In[3]:


get_ipython().run_line_magic('pip', 'install pandas')


# In[4]:


get_ipython().run_line_magic('pip', 'install pandas numpy matplotlib scikit-learn')


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

print("All packages loaded successfully!")


# In[6]:


import sys
get_ipython().system('{sys.executable} -m pip install --upgrade numexpr bottleneck')


# In[1]:


import numexpr
import bottleneck

print(numexpr.__version__)
print(bottleneck.__version__)


# In[1]:


import pandas as pd
import numexpr
import bottleneck

print(pd.__version__)
print(numexpr.__version__)
print(bottleneck.__version__)


# In[2]:


import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print(df)


# In[3]:


import sklearn
print(sklearn.__version__)


# In[4]:


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

numeric_features = ['Age', 'Salary']
categorical_features = ['Gender', 'City']

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

print("Pipeline Ready")


# In[7]:


import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/store_sales_db"
)

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# =========================
# TRANSFORM
# =========================

# تنظيف النصوص
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# تحويل البيانات
df['Qty'] = df['Qty'].astype(int)
df['Unit_Price'] = df['Unit_Price'].astype(float)
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# معالجة القيم المفقودة
df = df.dropna(subset=['StoreID', 'CustomerID', 'ProductName'])

# حساب القيم
df['Total_Price_OMR'] = df['Qty'] * df['Unit_Price'] * 0.385
df['Unit_Price_OMR'] = df['Unit_Price'] * 0.385

# =========================
# LOAD → TABLES
# =========================

# 🔵 STORE TABLE
store_df = df[['StoreID']].drop_duplicates()
store_df['StoreName'] = store_df['StoreID'].apply(lambda x: f"Store {x}")

store_df.to_sql('Store', engine, if_exists='append', index=False)

# 🔵 CUSTOMER TABLE
customer_df = df[['CustomerID']].drop_duplicates()
customer_df['CustomerName'] = None

customer_df.to_sql('Customer', engine, if_exists='append', index=False)

# 🔵 PRODUCT TABLE
product_df = df[['ProductName']].drop_duplicates()
product_df.to_sql('Product', engine, if_exists='append', index=False)

# 🔵 LINK PRODUCT ID
product_db = pd.read_sql("SELECT ProductID, ProductName FROM Product", engine)
df = df.merge(product_db, on='ProductName', how='left')

# 🔵 SALE TABLE (MATCH YOUR SQL EXACTLY)
sale_df = df[[
    'StoreID',
    'CustomerID',
    'ProductID',
    'Qty',
    'Unit_Price',
    'CurrencyType',
    'Unit_Price_OMR',
    'Total_Price_OMR',
    'SaleDate'
]]

sale_df.to_sql('Sale', engine, if_exists='append', index=False)

print("✔ DATA LOADED SUCCESSFULLY INTO ALL TABLES")


# In[6]:


pip install pymysql


# In[10]:


from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("SELECT * FROM Store"))


# In[12]:


with engine.connect() as conn:
    conn.execute(text("DELETE FROM Sale"))


# In[14]:


pip install pymysql pandas numpy scikit-learn


# In[15]:


import pandas as pd
import numpy as np
import pymysql
from sklearn.impute import SimpleImputer

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="store_sales_db",
    autocommit=True
)

cursor = conn.cursor()

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

df[['Qty']] = SimpleImputer(strategy='median').fit_transform(df[['Qty']])
df[['Unit_Price']] = SimpleImputer(strategy='mean').fit_transform(df[['Unit_Price']])

df = df.dropna(subset=['StoreID', 'CustomerID', 'ProductName'])

df['Qty'] = df['Qty'].astype(int)
df['Unit_Price'] = df['Unit_Price'].astype(float)
df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')
df = df.dropna(subset=['SaleDate'])

rate = 0.385

df['Unit_Price_OMR'] = df['Unit_Price'] * rate
df['Total_Price_OMR'] = df['Qty'] * df['Unit_Price_OMR']


stores = df[['StoreID']].drop_duplicates()
for _, row in stores.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO Store (StoreID, StoreName)
        VALUES (%s, %s)
    """, (row['StoreID'], f"Store {row['StoreID']}"))

customers = df[['CustomerID']].drop_duplicates()
for _, row in customers.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO Customer (CustomerID, CustomerName)
        VALUES (%s, %s)
    """, (row['CustomerID'], None))


products = df[['ProductName']].drop_duplicates()
for _, row in products.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO Product (ProductName)
        VALUES (%s)
    """, (row['ProductName'],))

cursor.execute("SELECT ProductID, ProductName FROM Product")
product_map = {name: pid for pid, name in cursor.fetchall()}

df['ProductID'] = df['ProductName'].map(product_map)

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Sale (
            StoreID, CustomerID, ProductID,
            Qty, Unit_Price, CurrencyType,
            Unit_Price_OMR, Total_Price_OMR, SaleDate
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row['StoreID'],
        row['CustomerID'],
        row['ProductID'],
        row['Qty'],
        row['Unit_Price'],
        row['CurrencyType'],
        row['Unit_Price_OMR'],
        row['Total_Price_OMR'],
        row['SaleDate']
    ))

conn.commit()

print("✔ FULL ETL COMPLETED SUCCESSFULLY USING MYSQL (CURSOR METHOD)")


# In[16]:


cursor.execute("SELECT COUNT(*) FROM Sale")
print("Total Sales Loaded:", cursor.fetchone()[0])


# In[17]:


import pandas as pd

df = pd.read_sql("SELECT * FROM Sale", conn)

print(df.groupby("StoreID")["Total_Price_OMR"].sum())


# In[18]:


import matplotlib.pyplot as plt

df.groupby("StoreID")["Total_Price_OMR"].sum().plot(kind='bar')
plt.show()


# In[19]:


import pandas as pd
import numpy as np
import pymysql
from sklearn.impute import SimpleImputer


# In[20]:


def extract_data(files):
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    print("✔ Extract completed")
    return df


# In[21]:


def load_to_staging(df, cursor, conn):

    cursor.execute("TRUNCATE TABLE staging_sales")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO staging_sales
            (StoreID, CustomerID, ProductName,
             Qty, Unit_Price, CurrencyType, SaleDate)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            row['StoreID'],
            row['CustomerID'],
            row['ProductName'],
            row['Qty'],
            row['Unit_Price'],
            row['CurrencyType'],
            row['SaleDate']
        ))

    conn.commit()
    print("✔ Load to staging completed")


# In[22]:


def transform_and_load(cursor, conn):

    df = pd.read_sql("SELECT * FROM staging_sales", conn)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    df[['Qty']] = SimpleImputer(strategy='median').fit_transform(df[['Qty']])
    df[['Unit_Price']] = SimpleImputer(strategy='mean').fit_transform(df[['Unit_Price']])

    df = df.dropna(subset=['StoreID', 'CustomerID', 'ProductName'])

    df['Qty'] = df['Qty'].astype(int)
    df['Unit_Price'] = df['Unit_Price'].astype(float)
    df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')
    df = df.dropna(subset=['SaleDate'])

    rate = 0.385

    df['Unit_Price_OMR'] = df['Unit_Price'] * rate
    df['Total_Price_OMR'] = df['Qty'] * df['Unit_Price_OMR']

    # =====================
    # STORE TABLE
    # =====================
    stores = df[['StoreID']].drop_duplicates()

    for _, row in stores.iterrows():
        cursor.execute("""
            INSERT IGNORE INTO Store (StoreID, StoreName)
            VALUES (%s, %s)
        """, (row['StoreID'], f"Store {row['StoreID']}"))

    # =====================
    # CUSTOMER TABLE
    # =====================
    customers = df[['CustomerID']].drop_duplicates()

    for _, row in customers.iterrows():
        cursor.execute("""
            INSERT IGNORE INTO Customer (CustomerID, CustomerName)
            VALUES (%s, %s)
        """, (row['CustomerID'], None))

    # =====================
    # PRODUCT TABLE
    # =====================
    products = df[['ProductName']].drop_duplicates()

    for _, row in products.iterrows():
        cursor.execute("""
            INSERT IGNORE INTO Product (ProductName)
            VALUES (%s)
        """, (row['ProductName'],))

    cursor.execute("SELECT ProductID, ProductName FROM Product")
    product_map = {name: pid for pid, name in cursor.fetchall()}

    df['ProductID'] = df['ProductName'].map(product_map)

    # =====================
    # FACT TABLE (SALE)
    # =====================
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO Sale (
                StoreID, CustomerID, ProductID,
                Qty, Unit_Price, CurrencyType,
                Unit_Price_OMR, Total_Price_OMR, SaleDate
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row['StoreID'],
            row['CustomerID'],
            row['ProductID'],
            row['Qty'],
            row['Unit_Price'],
            row['CurrencyType'],
            row['Unit_Price_OMR'],
            row['Total_Price_OMR'],
            row['SaleDate']
        ))

    conn.commit()
    print("✔ Transform + Load completed")


# In[26]:


print(df_raw['StoreID'].unique()[:10])


# In[27]:


try:

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="store_sales_db",
        autocommit=True
    )

    cursor = conn.cursor()

    files = [
        r"C:\Users\DELL\Downloads\store_sales_1.csv",
        r"C:\Users\DELL\Downloads\store_sales_2.csv",
        r"C:\Users\DELL\Downloads\store_sales_3.csv"
    ]

    # =====================
    # RUN PIPELINE
    # =====================
    df_raw = extract_data(files)

    load_to_staging(df_raw, cursor, conn)

    transform_and_load(cursor, conn)

    print("🎯 FULL ELT PIPELINE COMPLETED SUCCESSFULLY")

except Exception as e:
    print("❌ ERROR OCCURRED:")
    print(e)

finally:
    cursor.close()
    conn.close()


# In[31]:


import schedule
import time
import pymysql
import pandas as pd
from datetime import datetime, timedelta
import random


# In[29]:


pip install schedule


# In[32]:


def update_random_row():

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="store_sales_db",
        autocommit=True
    )

    cursor = conn.cursor()

    cursor.execute("SELECT SaleID FROM Sale")
    rows = cursor.fetchall()

    if not rows:
        print("No data found")
        return

    sale_id = random.choice(rows)[0]

    new_date = datetime.now()

    cursor.execute("""
        UPDATE Sale
        SET SaleDate = %s
        WHERE SaleID = %s
    """, (new_date, sale_id))

    conn.commit()
    conn.close()

    print(f"✔ Updated row {sale_id} at {new_date}")


# In[34]:


schedule.every(1).minutes.do(update_random_row)

print("⏳ Scheduler started... updating one row every 1 minutes")

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


cursor.execute("""
        SELECT SaleID, SaleDate
        FROM Sale
        WHERE SaleID = %s
    """, (sale_id,))

    updated_row = cursor.fetchone()

    print("===================================")
    print("✔ ROW UPDATED")
    print("SaleID:", updated_row[0])
    print("New SaleDate:", updated_row[1])
    print("Time:", datetime.now())
    print("===================================")

    conn.close()


# In[ ]:


def insert_new_sale():

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="store_sales_db",
        autocommit=True
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT StoreID, CustomerID, ProductName, Qty, Unit_Price, CurrencyType
        FROM staging_sales
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No data in staging")
        return

    row = random.choice(rows)

    store_id = row[0]
    customer_id = row[1]
    product_name = row[2]
    qty = float(row[3])
    unit_price = float(row[4])
    currency = row[5]

    cursor.execute("""
        SELECT ProductID FROM Product
        WHERE ProductName = %s
    """, (product_name,))

    result = cursor.fetchone()

    if not result:
        print("Product not found:", product_name)
        return

    product_id = result[0]

    rate = 0.385
    unit_price_omr = unit_price * rate
    total_price_omr = qty * unit_price_omr

    sale_date = datetime.now()

    cursor.execute("""
        INSERT INTO Sale (
            StoreID, CustomerID, ProductID,
            Qty, Unit_Price, CurrencyType,
            Unit_Price_OMR, Total_Price_OMR, SaleDate
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        store_id,
        customer_id,
        product_id,
        qty,
        unit_price,
        currency,
        unit_price_omr,
        total_price_omr,
        sale_date
    ))

    conn.commit()


    print(" NEW ROW INSERTED")
    print("Store:", store_id)
    print("Customer:", customer_id)
    print("Product:", product_name)
    print("Qty:", qty)
    print("Total (OMR):", total_price_omr)
    print("Date:", sale_date)

    conn.close()


# In[ ]:


#while True:insert_new_sale()time.sleep(60)  #


# In[1]:


files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]


# In[2]:


import pandas as pd
import numpy as np
import time
import pymysql
from datetime import datetime

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df = df.dropna(subset=['StoreID','CustomerID','ProductName'])
df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')
df = df.dropna(subset=['SaleDate'])


# In[3]:


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="store_sales_db",
    autocommit=True
)

cursor = conn.cursor()


# In[4]:


i = 0


# In[5]:


def insert_next_row():

    global i

    if i >= len(df):
        print("✔ All data processed")
        return False

    row = df.iloc[i]

    # تحويل العملة
    rate = 0.385
    unit_price_omr = row['Unit_Price'] * rate
    total_price_omr = row['Qty'] * unit_price_omr

    # ProductID
    cursor.execute("""
        SELECT ProductID FROM Product
        WHERE ProductName = %s
    """, (row['ProductName'],))

    res = cursor.fetchone()
    if not res:
        print("Product not found:", row['ProductName'])
        return True

    product_id = res[0]

    # INSERT
    cursor.execute("""
        INSERT INTO Sale (
            StoreID, CustomerID, ProductID,
            Qty, Unit_Price, CurrencyType,
            Unit_Price_OMR, Total_Price_OMR, SaleDate
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row['StoreID'],
        row['CustomerID'],
        product_id,
        row['Qty'],
        row['Unit_Price'],
        row['CurrencyType'],
        unit_price_omr,
        total_price_omr,
        row['SaleDate']
    ))

    conn.commit()

    print("✔ Inserted row:", i, "| Product:", row['ProductName'])

    i += 1
    return True


# In[6]:


while True:
    result = insert_next_row()

    if not result:
        break

    time.sleep(60)  


# In[7]:


import pandas as pd
import numpy as np
import pymysql
import time
from datetime import datetime

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df = df.dropna(subset=['StoreID','CustomerID','ProductName'])

df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')
df = df.dropna(subset=['SaleDate'])


# In[8]:


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="store_sales_db",
    autocommit=True
)

cursor = conn.cursor()


# In[9]:


i = 0


# In[10]:


def insert_full_row():

    global i

    if i >= len(df):
        print("✔ All rows inserted")
        return False

    row = df.iloc[i]

    rate = 0.385
    unit_price_omr = row['Unit_Price'] * rate
    total_price_omr = row['Qty'] * unit_price_omr

    cursor.execute("""
        SELECT ProductID
        FROM Product
        WHERE ProductName = %s
    """, (row['ProductName'],))

    res = cursor.fetchone()

    if not res:
        print("Product not found:", row['ProductName'])
        i += 1
        return True

    product_id = res[0]

    cursor.execute("""
        INSERT INTO Sale (
            StoreID,
            CustomerID,
            ProductID,
            Qty,
            Unit_Price,
            CurrencyType,
            Unit_Price_OMR,
            Total_Price_OMR,
            SaleDate
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row['StoreID'],
        row['CustomerID'],
        product_id,
        row['Qty'],
        row['Unit_Price'],
        row['CurrencyType'],
        unit_price_omr,
        total_price_omr,
        row['SaleDate']
    ))

    conn.commit()

    print(f"✔ Inserted FULL row {i} | Store={row['StoreID']} | Customer={row['CustomerID']} | Product={row['ProductName']}")

    i += 1
    return True


# In[11]:


while True:
    result = insert_full_row()

    if not result:
        break

    time.sleep(60)  # كل دقيقة


# In[12]:


import numpy as np

df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')


# In[13]:


df['Qty'] = df['Qty'].fillna(0)
df['Unit_Price'] = df['Unit_Price'].fillna(df['Unit_Price'].mean())


# In[14]:


df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')

df = df.dropna(subset=['Qty', 'Unit_Price'])

df['Qty'] = df['Qty'].astype(int)
df['Unit_Price'] = df['Unit_Price'].astype(float)


# In[4]:


import pandas as pd
import numpy as np
import pymysql
import time
from datetime import datetime

files = [
    r"C:\Users\DELL\Downloads\store_sales_1.csv",
    r"C:\Users\DELL\Downloads\store_sales_2.csv",
    r"C:\Users\DELL\Downloads\store_sales_3.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')

df = df.dropna(subset=['Qty','Unit_Price','StoreID','CustomerID','ProductName'])

df['is_loaded'] = 0   


# In[5]:


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="store_sales_db",
    autocommit=True
)

cursor = conn.cursor()


# In[6]:


df = df.reset_index(drop=True)


# In[7]:


i = 0

def insert_and_update():

    global i

    if i >= len(df):
        print("✔ All rows processed")
        return False

    row = df.iloc[i]

    # check loaded flag
    if df.loc[i, 'is_loaded'] == 1:
        i += 1
        return True

    rate = 0.385
    unit_price_omr = row['Unit_Price'] * rate
    total_price_omr = row['Qty'] * unit_price_omr

    cursor.execute("""
        SELECT ProductID FROM Product
        WHERE ProductName = %s
    """, (row['ProductName'],))

    res = cursor.fetchone()

    if not res:
        print("Product not found:", row['ProductName'])
        i += 1
        return True

    product_id = res[0]

    cursor.execute("""
        INSERT INTO Sale (
            StoreID, CustomerID, ProductID,
            Qty, Unit_Price, CurrencyType,
            Unit_Price_OMR, Total_Price_OMR, SaleDate
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row['StoreID'],
        row['CustomerID'],
        product_id,
        int(row['Qty']),
        row['Unit_Price'],
        row['CurrencyType'],
        unit_price_omr,
        total_price_omr,
        datetime.now()
    ))

    conn.commit()

    df.loc[i, 'is_loaded'] = 1

    df.to_csv(
        r"C:\Users\DELL\Downloads\store_sales_updated.csv",
        index=False
    )

    print(f"✔ Row {i} inserted + CSV updated")

    i += 1
    return True


# In[8]:


import time


# In[9]:


while True:
    try:
        print("running row:", i)

        result = insert_and_update()

        if not result:
            print(" Finished all rows")
            break

        time.sleep(30)

    except Exception as e:
        print("Error happened:", e)
        break


# In[10]:


cursor.execute("""
    SELECT *
    FROM Sale
    ORDER BY SaleID DESC
    LIMIT 5
""")

rows = cursor.fetchall()

for r in rows:
    print(r)


# In[11]:


import pandas as pd
import time
import pymysql

file_path = r"C:\Users\DELL\Downloads\store_sales_updated.csv"


# In[12]:


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="store_sales_db",
    autocommit=True
)

cursor = conn.cursor()


# In[13]:


last_len = 0


# In[14]:


import numpy as np


# In[15]:


row = row.replace({np.nan: None})


# In[ ]:


df = df.replace({np.nan: None})


# In[ ]:


def clean_row(row):
    return {
        "StoreID": None if pd.isna(row["StoreID"]) else row["StoreID"],
        "CustomerID": None if pd.isna(row["CustomerID"]) else row["CustomerID"],
        "ProductName": None if pd.isna(row["ProductName"]) else row["ProductName"],
        "Qty": None if pd.isna(row["Qty"]) else int(row["Qty"]),
        "Unit_Price": None if pd.isna(row["Unit_Price"]) else float(row["Unit_Price"]),
        "CurrencyType": row["CurrencyType"],
        "SaleDate": row["SaleDate"]
    }


# In[ ]:


row = clean_row(row)


# In[ ]:


while True:

    df = pd.read_csv(file_path)

    df = df.replace({np.nan: None})

    if len(df) > last_len:

        new_rows = df.iloc[last_len:]

        for _, row in new_rows.iterrows():

            try:
                rate = 0.385
                qty = int(row['Qty'])
                unit_price = float(row['Unit_Price'])

                unit_price_omr = unit_price * rate
                total_price_omr = qty * unit_price_omr

                cursor.execute("""
                    SELECT ProductID FROM Product
                    WHERE ProductName = %s
                """, (row['ProductName'],))

                res = cursor.fetchone()

                if not res:
                    print("❌ Product not found:", row['ProductName'])
                    continue

                product_id = res[0]

                cursor.execute("""
                    INSERT INTO Sale (
                        StoreID, CustomerID, ProductID,
                        Qty, Unit_Price, CurrencyType,
                        Unit_Price_OMR, Total_Price_OMR, SaleDate
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                    row['StoreID'],
                    row['CustomerID'],
                    product_id,
                    qty,
                    unit_price,
                    row['CurrencyType'],
                    unit_price_omr,
                    total_price_omr,
                    pd.to_datetime(row['SaleDate'])
                ))

                print("✔ New row inserted:", row['ProductName'])

            except Exception as e:
                print("❌ Error in row:", e)

        last_len = len(df)

    time.sleep(10) 


# In[17]:


pip install requests pandas schedule


# In[18]:


pip install requests pandas sqlalchemy pymysql schedule


# In[19]:


import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import schedule
import time

API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
CITY = "Muscat"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


engine = create_engine("mysql+pymysql://root:password@localhost/weather_db")


def extract():
    response = requests.get(URL)
    data = response.json()
    return data


def transform(data):
    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_desc": data["weather"][0]["description"],
        "recorded_at": datetime.now()
    }
    return transformed


def load(record):
    df = pd.DataFrame([record])
    df.to_sql("weather_data", con=engine, if_exists="append", index=False)


def etl():
    try:
        print("Running ETL...")
        raw_data = extract()
        clean_data = transform(raw_data)
        load(clean_data)
        print("Done ✔")
    except Exception as e:
        print("Error:", e)

schedule.every(1).minutes.do(etl)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import schedule
import time

# ======================
# CONFIG
# ======================
API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
CITY = "Muscat"

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# MySQL Connection
engine = create_engine("mysql+pymysql://root:1234@localhost/weather_db")


# ======================
# EXTRACT
# ======================
def extract():
    try:
        response = requests.get(URL, timeout=10)
        data = response.json()

        # تحقق من نجاح API
        if response.status_code != 200:
            raise Exception(data)

        # تحقق من البيانات الأساسية
        if "main" not in data or "weather" not in data:
            raise Exception("Invalid API response")

        return data

    except Exception as e:
        raise Exception(f"Extract Error: {e}")


# ======================
# TRANSFORM
# ======================
def transform(data):
    try:
        return {
            "city": data["name"],
            "temperature": float(data["main"]["temp"]),
            "humidity": int(data["main"]["humidity"]),
            "weather_desc": data["weather"][0]["description"],
            "recorded_at": datetime.now()
        }
    except Exception as e:
        raise Exception(f"Transform Error: {e}")


# ======================
# LOAD
# ======================
def load(record):
    try:
        df = pd.DataFrame([record])

        df.to_sql(
            name="weather_data",
            con=engine,
            if_exists="append",
            index=False,
            method="multi"
        )

    except Exception as e:
        raise Exception(f"Load Error: {e}")


# ======================
# ETL PIPELINE
# ======================
def etl():
    try:
        print(f"\n ETL START: {datetime.now()}")

        raw_data = extract()
        clean_data = transform(raw_data)
        load(clean_data)

        print(f"ETL SUCCESS: {datetime.now()}")

    except Exception as e:
        print(" ETL FAILED:", e)


# ======================
# SCHEDULER
# ======================
schedule.every(1).minutes.do(etl)

print("⏳ Scheduler Running...")

# تشغيل أول مرة مباشرة (مهم للدكتور)
etl()

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


import requests
import pandas as pd
import time
from datetime import datetime
from sqlalchemy import create_engine, text

username = "root"
password = "1234"
host = "localhost"
database = "weatherdb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)


API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
CITY = "Muscat"

def extract_weather():
    print("\nEXTRACTING WEATHER DATA...")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data)

    if "main" not in data:
        raise Exception("Invalid API response")

    return data

def transform_weather(data):
    print("TRANSFORMING DATA...")

    return pd.DataFrame([{
        "City": data["name"],
        "Temperature": float(data["main"]["temp"]),
        "Humidity": int(data["main"]["humidity"]),
        "Pressure": int(data["main"]["pressure"]),
        "WindSpeed": float(data["wind"]["speed"]),
        "WeatherDescription": data["weather"][0]["description"],
        "Timestamp": datetime.now()
    }])

def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS WeatherData (
            WeatherID INT AUTO_INCREMENT PRIMARY KEY,
            City VARCHAR(100),
            Temperature FLOAT,
            Humidity FLOAT,
            Pressure FLOAT,
            WindSpeed FLOAT,
            WeatherDescription VARCHAR(255),
            Timestamp DATETIME
        )
        """))
        conn.commit()

def load_weather(df):
    print("LOADING TO DATABASE...")

    df.to_sql(
        "WeatherData",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print("DATA INSERTED SUCCESSFULLY")

def run_weather_etl():
    try:
        weather_data = extract_weather()
        transformed_data = transform_weather(weather_data)
        create_table()
        load_weather(transformed_data)

        print("WEATHER ETL COMPLETED")

    except Exception as e:
        print("ETL ERROR:", e)

while True:
    print("\nRUNNING WEATHER ETL...")
    run_weather_etl()

    print("WAITING 30 sec...")
    time.sleep(30)


# In[1]:


import requests
import pandas as pd
import time
from datetime import datetime
from sqlalchemy import create_engine, text

# ======================
# DATABASE
# ======================
username = "root"
password = "1234"
host = "localhost"
database = "weatherdb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# ======================
# API
# ======================
API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
CITY = "Muscat"

# ======================
# EXTRACT
# ======================
def extract_weather():
    print("\nEXTRACTING WEATHER DATA...")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data)

    if "main" not in data:
        raise Exception("Invalid API response")

    return data

# ======================
# TRANSFORM
# ======================
def transform_weather(data):
    print("TRANSFORMING DATA...")

    return pd.DataFrame([{
        "City": data["name"],
        "Temperature": float(data["main"]["temp"]),
        "Humidity": int(data["main"]["humidity"]),
        "Pressure": int(data["main"]["pressure"]),
        "WindSpeed": float(data["wind"]["speed"]),
        "WeatherDescription": data["weather"][0]["description"],
        "RecordedAt": datetime.now()
    }])

# ======================
# CREATE TABLE
# ======================
def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS WeatherData (
            WeatherID INT AUTO_INCREMENT PRIMARY KEY,
            City VARCHAR(100),
            Temperature FLOAT,
            Humidity FLOAT,
            Pressure FLOAT,
            WindSpeed FLOAT,
            WeatherDescription VARCHAR(255),
            RecordedAt DATETIME
        )
        """))

# ======================
# LOAD
# ======================
def load_weather(df):
    print("LOADING TO DATABASE...")

    df.to_sql(
        "WeatherData",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print("DATA INSERTED SUCCESSFULLY")

# ======================
# PIPELINE
# ======================
def run_weather_etl():
    try:
        weather_data = extract_weather()
        transformed_data = transform_weather(weather_data)
        create_table()
        load_weather(transformed_data)

        print("WEATHER ETL COMPLETED")

    except Exception as e:
        print("ETL ERROR:", e)

# ======================
# LOOP
# ======================
while True:
    print("\nRUNNING WEATHER ETL...")
    run_weather_etl()

    print("WAITING 30 sec...")
    time.sleep(30)


# In[ ]:




