from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Joke

DATABASE_URL = "sqlite:///jokes.db"  
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)

def save_jokes_to_db(jokes):

    session = SessionLocal()
    try:
        for joke_data in jokes:
            joke = Joke(
                category=joke_data["category"],
                type=joke_data["type"],
                joke=joke_data.get("joke"), 
                setup=joke_data.get("setup"),  
                delivery=joke_data.get("delivery"),
                nsfw=joke_data["flags"]["nsfw"],
                political=joke_data["flags"]["political"],
                sexist=joke_data["flags"]["sexist"],
                safe=joke_data["safe"],
                lang=joke_data["lang"],
            )
            session.add(joke)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
