#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
options = webdriver.ChromeOptions()
options.add_argument("--headless")  

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


driver.get("https://fakestoreapi.com/users")

data = json.loads(driver.find_element("tag name", "body").text)

rows = []

for user in data:
    address = user.get("address", {})

    rows.append({
        "id": user.get("id"),
        "firstname": user.get("name", {}).get("firstname"),
        "lastname": user.get("name", {}).get("lastname"),
        "email": user.get("email"),
        "phone": user.get("phone"),
        "city": address.get("city"),
        "street": address.get("street"),
        "number": address.get("number"),
        "zipcode": address.get("zipcode"),
        "full_address": f"{address.get('street')} {address.get('number')}, {address.get('city')}, {address.get('zipcode')}"
    })
df = pd.DataFrame(rows)
print(df)
df.to_excel("users_addresses.xlsx", index=False)
driver.quit()


# In[ ]:


get_ipython().system('pip install webdriver-manager')


# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json

driver = webdriver.Chrome()

driver.get("https://fakestoreapi.com/products")
products = json.loads(driver.find_element(By.TAG_NAME, "body").text)

products_df = pd.json_normalize(products)

print("=== PRODUCTS ===")
print(products_df.head())

driver.get("https://fakestoreapi.com/users")
users = json.loads(driver.find_element(By.TAG_NAME, "body").text)

users_df = pd.json_normalize(users)

print("\n=== USERS ===")
print(users_df.head())

driver.get("https://fakestoreapi.com/carts")
carts = json.loads(driver.find_element(By.TAG_NAME, "body").text)

carts_df = pd.json_normalize(carts)

print("\n=== CARTS ===")
print(carts_df.head())

with pd.ExcelWriter("fakestore_data.xlsx") as writer:
    products_df.to_excel(writer, sheet_name="Products", index=False)
    users_df.to_excel(writer, sheet_name="Users", index=False)
    carts_df.to_excel(writer, sheet_name="Carts", index=False)

driver.quit()


# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
options = webdriver.ChromeOptions()
options.add_argument("--headless")  

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


driver.get("https://fakestoreapi.com/users")

data = json.loads(driver.find_element("tag name", "body").text)

rows = []

for user in data:
    address = user.get("address", {})

    rows.append({
        "id": user.get("id"),
        "firstname": user.get("name", {}).get("firstname"),
        "lastname": user.get("name", {}).get("lastname"),
        "email": user.get("email"),
        "phone": user.get("phone"),
        "city": address.get("city"),
        "street": address.get("street"),
        "number": address.get("number"),
        "zipcode": address.get("zipcode"),
        "full_address": f"{address.get('street')} {address.get('number')}, {address.get('city')}, {address.get('zipcode')}"
    })
df = pd.DataFrame(rows)
print(df)
df.to_excel("users_addresses.xlsx", index=False)
driver.quit()


# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()

driver.get("https://fakestoreapi.com/products")
products = json.loads(driver.find_element(By.TAG_NAME, "body").text)
products_count = len(products)

driver.get("https://fakestoreapi.com/users")
users = json.loads(driver.find_element(By.TAG_NAME, "body").text)
users_count = len(users)

print(f"عدد المنتجات: {products_count}")
print(f"عدد المستخدمين: {users_count}")

driver.quit()


# In[ ]:


import requests
API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Muscat,OM",
    "appid": API_KEY,
    "units": "metric",
    "lang": "ar"
}
response = requests.get(url, params=params)
data = response.json()

if response.status_code != 200:
    print(" خطأ في الطلب:")
    print(data)
else:
    print(" المدينة:", data["name"])
    print(" درجة الحرارة:", data["main"]["temp"], "°C")
    print(" الإحساس الحقيقي:", data["main"]["feels_like"], "°C")
    print(" الرطوبة:", data["main"]["humidity"], "%")
    print(" الطقس:", data["weather"][0]["description"])
    print(" سرعة الرياح:", data["wind"]["speed"], "م/ث")


# In[3]:


import requests

API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Muscat,OM",
    "appid": API_KEY,
    "units": "metric",
    "lang": "ar"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code != 200:
    print("خطأ في الطلب:")
    print(data)
else:
    print("\n" + "=" * 40)
    print("        طقس مدينة مسقط")
    print("=" * 40)

    print(f"المدينة        : {data['name']}")
    print(f"درجة الحرارة   : {data['main']['temp']} °C")
    print(f"الإحساس        : {data['main']['feels_like']} °C")
    print(f"الرطوبة        : {data['main']['humidity']} %")
    print(f"الحالة         : {data['weather'][0]['description']}")
    print(f"سرعة الرياح    : {data['wind']['speed']} m/s")

    print("=" * 40)


# In[4]:


import requests

API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"

cities = [
    "Muscat,OM", "Dubai,AE", "London,UK", "Paris,FR",
    "New York,US", "Tokyo,JP", "Berlin,DE", "Cairo,EG",
    "Riyadh,SA", "Doha,QA"
]


cities = (cities * 50)[:500]

results = []

for city in cities:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        results.append({
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        })

        print("تم:", data["name"])
    else:
        print("فشل:", city)

print("\nعدد المدن التي تم جلبها:", len(results))


# In[5]:


get_ipython().system('pip install requests pandas')


# In[ ]:


import requests
import pandas as pd
import json
import time
API_KEY = "d2450428d9b1e306ed63da45a4e3ba1b"
cities_url = "https://raw.githubusercontent.com/lutangar/cities.json/master/cities.json"
response = requests.get(cities_url)
cities = response.json()
cities = cities[:500]
raw_data = []
clean_data = []
for i, city in enumerate(cities):

    lat = city.get("lat")
    lon = city.get("lng")

    if lat is None or lon is None:
        continue

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        raw_data.append(data)
        clean_data.append({
            "city": city.get("name"),
            "country": city.get("country"),

            "lat": lat,
            "lon": lon,

            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "humidity": data.get("main", {}).get("humidity"),
            "pressure": data.get("main", {}).get("pressure"),

            "wind_speed": data.get("wind", {}).get("speed"),
            "wind_direction": data.get("wind", {}).get("deg"),

            "clouds": data.get("clouds", {}).get("all"),
            "visibility": data.get("visibility"),

            "sunrise": data.get("sys", {}).get("sunrise"),
            "sunset": data.get("sys", {}).get("sunset"),

            "weather_condition": (
                data["weather"][0]["description"]
                if "weather" in data and len(data["weather"]) > 0
                else None
            ),

            "timestamp": data.get("dt")
        })

        print(f"{i+1}/500 - OK: {city.get('name')}")

    else:
        print(f"{i+1}/500 - FAILED: {city.get('name')}")

    time.sleep(1)  

df = pd.DataFrame(clean_data)


df.to_csv("weather_500_cities.csv", index=False)

with open("raw_weather.json", "w", encoding="utf-8") as f:
    json.dump(raw_data, f, indent=4)

print("\nDONE: Data Warehouse Created Successfully")
print("Files created:")
print("- weather_500_cities.csv")
print("- raw_weather.json")


# In[ ]:


import os
print(os.getcwd())


# In[6]:


from IPython.display import FileLink

FileLink("weather_500_cities.csv")


# In[7]:


import pandas as pd

df = pd.read_csv("weather_500_cities.csv")

df.head(50)


# In[8]:


get_ipython().system('pip install mysql-connector-python')


# In[9]:


import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="coffee_shop"
)

print("Connected successfully")


# In[ ]:


import pandas as pd

tables = [
    "employee",
    "customer",
    "orders",
    "product",
    "order_item",
    "payment",
    "bean",
    "roaster",
    "skill",
    "equipment"
]

dataframes = {}

for t in tables:
    print(f"Loading: {t}")
    df = pd.read_sql(f"SELECT * FROM {t}", conn)
    dataframes[t] = df
    display(df.head())


# In[ ]:


import pandas as pd

tables = [
    "employee",
    "customer",
    "orders",
    "product",
    "order_item",
    "payment",
    "bean",
    "roaster"
]

for t in tables:
    print(f"\n===== {t} =====")
    df = pd.read_sql(f"SELECT * FROM {t}", conn)
    display(df)  
conn.close()


# In[10]:


get_ipython().system('pip install pytesseract opencv-python pillow pandas')


# In[11]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[ ]:


import os
import cv2
import pytesseract

folder = "dataset/invoices"

files = os.listdir(folder)[:5]  # أول 5 صور

extracted_texts = {}

for file in files:
    path = os.path.join(folder, file)

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    extracted_texts[file] = text

    txt_name = file.replace(".jpg", ".txt").replace(".png", ".txt")

    with open(f"output/{txt_name}", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Processed: {file}")


# In[ ]:


import os
print(os.getcwd())


# In[12]:


print(os.listdir())


# In[13]:


import os

os.makedirs("dataset/invoices", exist_ok=True)


# In[14]:


import os

folder = "dataset/invoices"

if not os.path.exists(folder):
    print("Folder not found, checking current directory...")
    folder = os.getcwd()

files = os.listdir(folder)[:5]

print(files)


# In[15]:


import os
import cv2
import pytesseract

folder = "dataset/invoices"

files = os.listdir(folder)[:5]  # أول 5 صور

extracted_texts = {}

for file in files:
    path = os.path.join(folder, file)

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    extracted_texts[file] = text

    # حفظ النص في ملف .txt
    txt_name = file.replace(".jpg", ".txt").replace(".png", ".txt")

    with open(f"output/{txt_name}", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Processed: {file}")


# In[16]:


import re
import pandas as pd

data = []

for file, text in extracted_texts.items():

    invoice_no = re.search(r"invoice\s*(no|number)?[:\-]?\s*(\w+)", text, re.I)
    date = re.search(r"\d{2}[/-]\d{2}[/-]\d{2,4}", text)
    total = re.search(r"total\s*[:\-]?\s*\$?\s*(\d+\.?\d*)", text, re.I)
    company = re.search(r"(company|from)\s*[:\-]?\s*(.*)", text, re.I)
    customer = re.search(r"(bill to|customer)\s*[:\-]?\s*(.*)", text, re.I)

    data.append({
        "file": file,
        "invoice_number": invoice_no.group(2) if invoice_no else None,
        "date": date.group(0) if date else None,
        "total_amount": total.group(1) if total else None,
        "company_name": company.group(2) if company else None,
        "customer_name": customer.group(2) if customer else None
    })

df = pd.DataFrame(data)
df


# In[17]:


import kagglehub

path = kagglehub.dataset_download("senju14/invoice-ocr")

print("Dataset path:", path)


# In[18]:


import os

print(os.listdir(path))


# In[19]:


import os

base_path = path  

img_folder = os.path.join(base_path, "test")

print(os.listdir(img_folder)[:5])


# In[20]:


for root, dirs, files in os.walk(img_folder):
    print("ROOT:", root)
    print("FILES sample:", files[:3])
    print("-"*40)


# In[21]:


import os

for root, dirs, files in os.walk(path):
    print("ROOT:", root)
    print("DIRS:", dirs)
    print("FILES sample:", files[:5])
    print("-"*60)


# In[22]:


import os

base_path = r"C:\Users\DELL\.cache\kagglehub\datasets\senju14\invoice-ocr\versions\1"

img_folder = os.path.join(base_path, "test", "images")

print(img_folder)
print(os.listdir(img_folder)[:5])


# In[23]:


import os
import cv2
import pytesseract

img_folder = r"C:\Users\DELL\.cache\kagglehub\datasets\senju14\invoice-ocr\versions\1\test\images"

files = os.listdir(img_folder)[:5]

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

extracted_texts = {}

for file in files:
    path_img = os.path.join(img_folder, file)

    img = cv2.imread(path_img)

    if img is None:
        print("Cannot read:", file)
        continue

    # تحسين بسيط للصورة (يرفع دقة OCR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    extracted_texts[file] = text

    print("\nFILE:", file)
    print(text[:300])
    print("-"*50)


# In[24]:


import os

os.makedirs("output", exist_ok=True)

for file, text in extracted_texts.items():
    name = file.split(".")[0]

    with open(f"output/{name}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("TXT files saved")


# In[25]:


import re
import pandas as pd

data = []

for file, text in extracted_texts.items():

    invoice_no = re.search(r"invoice\s*(no|number)?[:\-]?\s*(\w+)", text, re.I)
    date = re.search(r"\d{2}[/-]\d{2}[/-]\d{2,4}", text)
    total = re.search(r"total\s*[:\-]?\s*\$?\s*(\d+\.?\d*)", text, re.I)
    company = re.search(r"(company|from)\s*[:\-]?\s*(.*)", text, re.I)
    customer = re.search(r"(bill to|customer)\s*[:\-]?\s*(.*)", text, re.I)

    data.append({
        "file": file,
        "invoice_number": invoice_no.group(2) if invoice_no else None,
        "date": date.group(0) if date else None,
        "company_name": company.group(2) if company else None,
        "customer_name": customer.group(2) if customer else None,
        "total_amount": total.group(1) if total else None
    })

df = pd.DataFrame(data)
df


# In[26]:


df.to_csv("invoice_results.csv", index=False)

print("DONE: invoice_results.csv created")


# In[27]:


from IPython.display import FileLink

FileLink("invoice_results.csv")


# In[28]:


import os

folder = r"C:\Users\DELL\Downloads"

print(os.listdir(folder))


# In[29]:


import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"C:\Users\DELL\Downloads\your_image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

text = pytesseract.image_to_string(thresh)

print(text)


# In[30]:


import os

folder = r"C:\Users\DELL\Downloads"

print(os.listdir(folder))


# In[31]:


import cv2
import pytesseract

# مسار Tesseract (تأكد أنه مثبت عندك)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# مسار الصورة الصحيح
img_path = r"C:\Users\DELL\Downloads\VAT-Invoice_simple2.jpg"

# قراءة الصورة
img = cv2.imread(img_path)

# تأكد أن الصورة انقرأت
if img is None:
    print("❌ لم يتم قراءة الصورة - تحقق من المسار")
else:
    # تحويلها إلى grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # تحسين بسيط
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    # OCR
    text = pytesseract.image_to_string(gray)

    print("===== OCR RESULT =====")
    print(text)


# In[32]:


import os

os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"


# In[33]:


get_ipython().system('pip install easyocr')
get_ipython().system('pip install opencv-python')


# In[34]:


import easyocr

# إنشاء القارئ (عربي + إنجليزي)
reader = easyocr.Reader(['ar', 'en'])

img_path = r"C:\Users\DELL\Downloads\VAT-Invoice_simple2.jpg"

results = reader.readtext(img_path, detail=0)

# دمج النصوص
text = "\n".join(results)

print(text)


# In[29]:


conda create -n ocr_env python=3.9
conda activate ocr_env
pip install easyocr opencv-python


# In[38]:


from sklearn.preprocessing import OrdinalEncoder

data = [["Low"], ["Medium"], ["High"], ["Medium"]]

encoder = OrdinalEncoder()

encoded = encoder.fit_transform(data)

print(encoded)


# In[36]:


get_ipython().system('pip install --upgrade --force-reinstall numpy pandas')


# In[43]:


get_ipython().system('pip install --upgrade --force-reinstall numpy')
get_ipython().system('pip install --upgrade --force-reinstall scikit-learn')


# In[44]:


import kagglehub

# Download latest version
path = kagglehub.dataset_download("hesh97/titanicdataset-traincsv")

print("Path to dataset files:", path)


# In[45]:


import os

print(path)
print(os.listdir(path))


# In[49]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import fetch_openml

# =========================
# 1. Load dataset
# =========================
titanic = fetch_openml("titanic", version=1, as_frame=True)
df = titanic.data
y = titanic.target

# =========================
# 2. Select columns
# =========================
num_cols = ["age", "fare"]
cat_cols = ["sex", "embarked"]

X = df[num_cols + cat_cols]

# =========================
# 3. Train/test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 4. Pipelines
# =========================

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# =========================
# 5. Column Transformer
# =========================

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])


model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier())
])

model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))


# In[ ]:




