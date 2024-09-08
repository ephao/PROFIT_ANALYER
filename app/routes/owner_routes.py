from flask import Blueprint, request, jsonify
from app.repositories.owner_repository import OwnerRepository
from app.services.profit_calculator import ProfitCalculator
from app.database import get_db

owner_routes = Blueprint('owner_routes', __name__)

@owner_routes.route('/api/top_profitable_owners')
def top_profitable_owners():
    n = int(request.args.get('n', 10))
    db = next(get_db())
    owner_repository = OwnerRepository(db)
    profit_calculator = ProfitCalculator(owner_repository)
    top_owners = profit_calculator.calculate_top_n_profitable_owners(n)
    return jsonify([{'address': owner.address, 'total_profit': owner.total_profit} for owner in top_owners])