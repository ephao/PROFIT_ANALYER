import sys
import os
import csv

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.repositories.owner_repository import OwnerRepository

def populate_db_from_csv(csv_file):
    """
    Populates the database with owner data from a CSV file.
    Args:
        csv_file (str): Path to the CSV file containing owner data.
    """
    db = SessionLocal()  # Create a database session
    owner_repository = OwnerRepository(db)

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        # Print column names
        print("Column names:", reader.fieldnames)
        
        # Print the first row
        first_row = next(reader, None)
        if first_row:
            print("First row:", first_row)
        else:
            print("The CSV file is empty")
            return

        # Reset the reader to the beginning of the file
        file.seek(0)
        next(reader)  # Skip the header row
        
        for row in reader:
            # Use .get() method to provide a default value if the key doesn't exist
            owner_address = row.get('Owner', row.get('owner', row.get('Address', row.get('address'))))
            volume_usd = float(row.get('VolumeUSD', row.get('volume_usd', 0)))
            
            if owner_address and volume_usd:
                owner_repository.add_profit(owner_address, volume_usd)  # Add profit for each owner
            else:
                print(f"Skipping row due to missing data: {row}")

    db.close()  # Close the database session

if __name__ == "__main__":
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    populate_db_from_csv(csv_file_path)  # Run the script to populate the database