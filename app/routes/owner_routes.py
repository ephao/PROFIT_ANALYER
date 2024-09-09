from flask import Blueprint, request, jsonify
from app.repositories.owner_repository import OwnerRepository
from app.services.profit_calculator import ProfitCalculator
from app.database import get_db

owner_routes = Blueprint('owner_routes', __name__)

@owner_routes.route('/api/top_profitable_owners')
def get_top_profitable_owners():
    """
    API endpoint to get the top profitable owners.
    Query Parameters:
        n (int): Number of top owners to retrieve (default: 10).
    Returns:
        JSON response with list of top profitable owners.
    """
    n = int(request.args.get('n', 10))  # Get 'n' from query params, default to 10
    db = next(get_db())  # Get a database session
    owner_repository = OwnerRepository(db)
    profit_service = ProfitCalculator(owner_repository)
    top_owners = profit_service.calculate_top_n_profitable_owners(n)
    # Convert owner objects to dictionaries for JSON response
    return jsonify([{'address': owner.address, 'total_profit': owner.total_profit} for owner in top_owners])