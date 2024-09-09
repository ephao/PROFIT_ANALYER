from sqlalchemy.orm import Session
from app.models.owner import Owner

class OwnerRepository:
    """
    Handles database operations for Owner objects.
    """

    def __init__(self, session: Session):
        """
        Initializes the repository with a database session.
        Args:
            session (Session): SQLAlchemy database session.
        """
        self.session = session  # Initialize with a database session

    def load_data(self, csv_file):
        """
        Placeholder method for loading data from a CSV file.
        Args:
            csv_file (str): Path to the CSV file.
        """
        # Placeholder method for loading data from CSV
        pass

    def get_or_create_owner(self, address):
        """
        Retrieves an existing owner or creates a new one if not found.
        Args:
            address (str): Ethereum address of the owner.
        Returns:
            Owner: The retrieved or newly created Owner object.
        """
        # Try to find an existing owner with the given address
        owner = self.session.query(Owner).filter_by(address=address).first()
        if not owner:
            # If not found, create a new owner
            owner = Owner(address=address)
            self.session.add(owner)
        return owner

    def add_profit(self, address, profit):
        """
        Adds profit to an owner's total profit.
        Args:
            address (str): Ethereum address of the owner.
            profit (float): Amount of profit to add.
        """
        owner = self.get_or_create_owner(address)
        owner.add_profit(profit)  # Add profit to the owner
        self.session.commit()  # Commit the changes to the database

    def get_top_n_profitable_owners(self, n):
        """
        Retrieves the top N profitable owners.
        Args:
            n (int): Number of top owners to retrieve.
        Returns:
            list[Owner]: List of top N profitable Owner objects.
        """
        # Query the database for top N owners by total profit
        return self.session.query(Owner).order_by(Owner.total_profit.desc()).limit(n).all()