from faker import Faker
from app import app
from models import db, MMR

def create_dummy_data(num_records=100):
    faker = Faker()
    
    with app.app_context():
        for _ in range(num_records):
            mmr_value = faker.random_int(0, 5000)
            new_record = MMR(id=faker.unique.random_number(digits=10), mmr=mmr_value)
            db.session.add(new_record)
        
        db.session.commit()
        print(f"{num_records} data records have been created")

if __name__ == "__main__":
    create_dummy_data()