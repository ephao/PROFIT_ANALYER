from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    address = Column(String(255), unique=True, nullable=False)
    total_profit = Column(Float, default=0)

    def add_profit(self, profit):
        self.total_profit += profit