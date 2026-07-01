from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.database.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    rows = Column(Integer)

    columns = Column(Integer)

    upload_time = Column(
        DateTime,
        default=datetime.utcnow
    )