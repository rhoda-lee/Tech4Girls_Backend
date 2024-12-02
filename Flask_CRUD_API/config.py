from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

database_username = os.getenv('DB_USERNAME')
database_password = os.getenv('DB_PASSWORD')
database_name = os.getenv('DB_NAME')

print(database_username, database_password, database_name)

# connection string or url
connection_str = f'mysql+mysqlconnector://{database_username}:{database_password}@localhost/{database_name}'

engine = create_engine(connection_str)

try:
    # establish connection to mysql database
    connection = engine.connect()
    print('Database has been located and connected to')
    connection.close()
except Exception as e:
    print(f'There was an error: {e}')

DBSession = sessionmaker(bind = engine)
session = DBSession()