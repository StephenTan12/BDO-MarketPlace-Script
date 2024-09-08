from google.cloud.sql.connector import Connector
import sqlalchemy
import os

from dotenv import load_dotenv

from .models import ItemData

load_dotenv()

connector = Connector()

def _getconn():
    conn = connector.connect(
        os.getenv("DB_INSTANCE_CONN"),
        os.getenv("DB_DRIVER"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        ip_type=os.getenv("DB_IP_TYPE"),
        db=os.getenv("DB_NAME")
    )
    return conn

pool = sqlalchemy.create_engine(
    os.getenv("DB_ENGINE_URL"),
    creator=_getconn,
)

def insert_to_database(item_data: ItemData):
    with pool.connect() as db_conn:
        insert_statement_text = _format_insert_query(item_data)
        db_conn.execute(insert_statement_text)
        db_conn.commit()

def _format_insert_query(item_data: ItemData) -> sqlalchemy.text:
    db_table_name = os.getenv("DB_TABLE_NAME")
    text = f"INSERT INTO {db_table_name} VALUES {item_data}"
    return sqlalchemy.text(text)