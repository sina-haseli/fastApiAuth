from datetime import datetime

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    # email = Column(String(255), unique=True)
    phone_number = Column(String(255), unique=True)
    password = Column(String(255))
    # created_at = Column(DateTime, default=datetime.utcnow)