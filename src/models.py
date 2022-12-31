from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
