from sqlalchemy import create_engine ,text ,MetaData
from sqlalchemy import (Table,Column,Integer,String)

engine=create_engine("postgresql+psycopg2://postgres:root@localhost/sqlalchemy_practice")
conn=engine.connect()
# print(conn)
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT current_database();"))
#     print("Connected to:", result.scalar())

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connected successfully!")
        print(result.fetchone())
except Exception as e:
    print("Connection failed!")
    print(e)

metadata=MetaData()    
users=Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(100))
)
persons=Table(
    "doctors",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(100))
)

print(metadata.tables)
metadata.create_all(engine,checkfirst=True)
metadata.reflect(engine)