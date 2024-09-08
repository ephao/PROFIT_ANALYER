from flask import request
from app import app, limiter
from app.controllers.owner_controller import OwnerController

controller = OwnerController('data.csv')

@app.route('/top_profitable_owners')
@limiter.limit("10 per minute")
def top_profitable_owners():
    n = int(request.args.get('n', 10))
    return controller.get_top_n_profitable_owners(n)