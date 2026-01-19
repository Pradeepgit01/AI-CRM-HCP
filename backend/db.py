from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://user:password@localhost:5432/ai_crm"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)

def connect_db():
    database.connect()

def disconnect_db():
    database.disconnect()
