from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from channel.driver.env import DATABASE_URL


engine = create_engine(url=DATABASE_URL)
Session  = sessionmaker(engine)
