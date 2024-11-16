from sqlalchemy import Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Proxy(Base):
    __tablename__ = "proxies"
    id = Column(Integer, primary_key=True)
    origin_url = Column(String(2048), nullable=False)
    unique_code = Column(String(3), nullable=False)
    created_at = Column(DateTime, default=func.now())
