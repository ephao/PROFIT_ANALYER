import csv
from app.database import SessionLocal
from app.repositories.owner_repository import OwnerRepository

def populate_db_from_csv(csv_file):
    db = SessionLocal()
    owner_repository = OwnerRepository(db)

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            owner_address = row['Owner']
            volume_usd = float(row['VolumeUSD'])
            owner_repository.add_profit(owner_address, volume_usd)

    db.close()

if __name__ == "__main__":
    populate_db_from_csv('data.csv')