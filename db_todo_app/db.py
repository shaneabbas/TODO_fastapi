from sqlalchemy import (
        Column,
        Integer,
        MetaData,
        String,
        Table,
        create_engine
    )
from databases import Database
import urllib
Database_URL = "postgresql://root:%s@localhost/items_db" % urllib.parse.quote_plus('123')

engine = create_engine(Database_URL)
metadata = MetaData()

Items = Table(
        "items",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("title", String(100)),
        Column("description", String(100))
)

User = Table(
        "user",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("username", String(100)),
        Column("password", String(200)),
)

database = Database(Database_URL)
