from prefect import flow, task
import requests
import pandas as pd
import mysql.connector
import os
from datetime import datetime

API_KEY = "goldapi-15fedb52d5bdba98523c2d10dfadd270-io"


@task
def extract():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {"x-access-token": API_KEY}
    return requests.get(url, headers=headers).json()


@task
def transform(data):
    return {
        "datetime": datetime.now(),
        "price_usd": data["price"],
        "price_gram_24k": data["price_gram_24k"],
        "price_gram_22k": data["price_gram_22k"],
        "price_gram_21k": data["price_gram_21k"],
        "change_percent": data["chp"]
    }


@task
def load_to_csv(record):
    file_path = "data/gold_prices.csv"
    df = pd.DataFrame([record])

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)


@task
def load_to_mysql(record):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="gold_db"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO gold_prices (
        datetime, price_usd, price_gram_24k,
        price_gram_22k, price_gram_21k, change_percent
    ) VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        str(record["datetime"]),
        record["price_usd"],
        record["price_gram_24k"],
        record["price_gram_22k"],
        record["price_gram_21k"],
        record["change_percent"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()


@flow
def gold_pipeline():
    data = extract()
    record = transform(data)
    load_to_csv(record)
    load_to_mysql(record)


if __name__ == "__main__":
    gold_pipeline()