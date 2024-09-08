from flask import jsonify
from app.services.profit_calculator import ProfitCalculator
from app.repositories.owner_repository import OwnerRepository

class OwnerController:
    def __init__(self, csv_file):
        self.owner_repository = OwnerRepository(csv_file)
        self.profit_calculator = ProfitCalculator(self.owner_repository)

    def get_top_n_profitable_owners(self, n):
        top_owners = self.profit_calculator.calculate_top_n_profitable_owners(n)
        return jsonify([{'address': owner.address, 'total_profit': owner.total_profit} for owner in top_owners])