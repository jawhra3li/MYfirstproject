from prefect import flow, task
from prefect.logging import get_run_logger
import pandas as pd
import mysql.connector


@task
def extract():

    logger = get_run_logger()

    logger.info("Reading telecom data...")

    df = pd.read_csv("data/raw/Telecom Subscriptions.csv")

    logger.info(f"{len(df)} records loaded")

    return df


@task
def transform(df):

    logger = get_run_logger()

    logger.info("Transforming data...")

    df.columns = [
        "year",
        "fixed_tel_subs",
        "fixed_tel_penetration",
        "fixed_bb_subs",
        "fixed_bb_penetration",
        "mobile_tel_subs",
        "mobile_tel_penetration",
        "mobile_bb_subs",
        "mobile_bb_penetration"
    ]

    df = df.fillna(0)

    # إزالة الفواصل من جميع الأعمدة
    for col in df.columns:
        df[col] = df[col].astype(str).str.replace(",", "", regex=False)

    logger.info("Transformation completed")

    return df


@task
def load(df):

    logger = get_run_logger()

    logger.info("Loading data into MySQL...")

    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="telecom_db"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO telecom_data
    (
        year,
        fixed_tel_subs,
        fixed_tel_penetration,
        fixed_bb_subs,
        fixed_bb_penetration,
        mobile_tel_subs,
        mobile_tel_penetration,
        mobile_bb_subs,
        mobile_bb_penetration
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():

        values = (
            int(float(row["year"])),
            float(row["fixed_tel_subs"]),
            float(row["fixed_tel_penetration"]),
            float(row["fixed_bb_subs"]),
            float(row["fixed_bb_penetration"]),
            float(row["mobile_tel_subs"]),
            float(row["mobile_tel_penetration"]),
            float(row["mobile_bb_subs"]),
            float(row["mobile_bb_penetration"])
        )

        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    logger.info("Data loaded successfully")


@flow(name="Telecom ETL Pipeline")
def telecom_pipeline():

    logger = get_run_logger()

    logger.info("Starting Telecom ETL Pipeline")

    df = extract()

    df = transform(df)

    load(df)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    telecom_pipeline()
