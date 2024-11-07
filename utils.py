from sqlalchemy.exc import OperationalError
from models import db
import time

def wait_for_db(app, max_retries=5, delay=5):
    with app.app_context():
        retries = 0
        while retries < max_retries:
            try:
                db.engine.connect()
                print("Database is ready!")
                return
            except OperationalError:
                retries += 1
                print(f"Database not ready. Retrying in {delay} seconds...")
                time.sleep(delay)
        print("Could not connect to the database.")
        exit(1)