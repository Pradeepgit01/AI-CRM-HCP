from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+aiomysql://user:password@localhost:3306/ai_crm"
pip install aiomysql
pip install pymysql


database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)

def connect_db():
    database.connect()

def disconnect_db():
    database.disconnect()
