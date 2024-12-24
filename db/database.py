import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
PORT = os.getenv("PORT")


database_url=f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(database_url)
sessionLocal=sessionmaker(autoflush=False, autocommit= False, bind=engine)
base = declarative_base()