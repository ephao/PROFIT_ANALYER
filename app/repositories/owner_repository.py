from sqlalchemy.orm import Session
from app.models.owner import Owner

class OwnerRepository:
    def __init__(self, session: Session):
        self.session = session

    def load_data(self, csv_file):
        # This method would be used to initially populate the database from CSV
        # For now, we'll leave it as a placeholder
        pass

    def get_or_create_owner(self, address):
        owner = self.session.query(Owner).filter_by(address=address).first()
        if not owner:
            owner = Owner(address=address)
            self.session.add(owner)
        return owner

    def add_profit(self, address, profit):
        owner = self.get_or_create_owner(address)
        owner.add_profit(profit)
        self.session.commit()

    def get_top_n_profitable_owners(self, n):
        return self.session.query(Owner).order_by(Owner.total_profit.desc()).limit(n).all()