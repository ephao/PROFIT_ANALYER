# This file defines the Owner model for the database

from sqlalchemy import Column, Integer, String, Float  # Import SQLAlchemy types for defining columns
from app.database import Base  # Import the Base class for SQLAlchemy ORM

class Owner(Base):  # Define Owner model, inheriting from SQLAlchemy Base
    """
    Represents an owner in the system.
    Attributes:
        id: Unique identifier for each owner.
        address: Ethereum address of the owner (unique and required).
        total_profit: Total profit accumulated by the owner.
    """
    __tablename__ = 'owners'  # Specify the table name in the database

    # Define columns for the 'owners' table
    id = Column(Integer, primary_key=True)  # Unique identifier for each owner
    address = Column(String(255), unique=True, nullable=False)  # Ethereum address of the owner
    total_profit = Column(Float, default=0)  # Total profit accumulated by the owner

    def add_profit(self, profit):
        """
        Adds the given profit to the owner's total profit.
        Args:
            profit (float): The amount of profit to add.
        """
        self.total_profit += profit  # Increment total_profit by the given amount