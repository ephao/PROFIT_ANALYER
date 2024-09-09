import csv
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
        for row in reader:
            owner_address = row['Owner']
            volume_usd = float(row['VolumeUSD'])
            owner_repository.add_profit(owner_address, volume_usd)  # Add profit for each owner

    db.close()  # Close the database session

if __name__ == "__main__":
    populate_db_from_csv('data.csv')  # Run the script to populate the database