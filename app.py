from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from seed import seed


DATABASE_URI = "postgres+psycopg2://localhost:5432/todo
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def refresh_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

def seed_database():
    seed(Session())


if __name__ == '__main__':
    refresh_database()
    # seed_database() # uncomment to seed
