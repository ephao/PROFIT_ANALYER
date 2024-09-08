# Top Profitable Owners Analyzer

This project analyzes transaction data to identify the top profitable owners from a CSV file. It uses a Flask backend with SQLAlchemy for database operations and a React frontend for displaying results.


## Setup and Installation

### Backend

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install required packages:
   ```
   pip install flask flask-cors sqlalchemy
   ```

3. Initialize the database:
   ```
   python scripts/populate_db.py
   ```

4. Run the Flask application:
   ```
   python run.py
   ```

### Frontend

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

## Usage

1. Ensure both the backend and frontend servers are running.
2. Open a web browser and navigate to `http://localhost:3000`.
3. Use the input field to adjust the number of top owners to display.
4. The list of top profitable owners will update automatically.

## API Endpoints

- GET `/api/top_profitable_owners?n=10`: Retrieves the top N profitable owners (default is 10).

## Testing

To run tests:

python -m pytest tests/


## Security Considerations

- CORS is enabled for development. Configure it appropriately for production.
- Implement authentication and authorization for the API in a production environment.
- Use environment variables for sensitive information like database credentials.

## Future Improvements

- Implement pagination for large datasets.
- Add more comprehensive error handling and logging.
- Optimize database queries for better performance with large datasets.
- Implement caching for frequently accessed data.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.