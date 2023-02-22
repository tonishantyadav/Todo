# Import SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to MYSQL database

# create Database URL to SQLAlchemy
# Note: You have to mention your mysql username, password, host and database
DB_URL = 'mysql://user:password@mysqlserver/database'

# create SQLAlchemy engine
engine = create_engine(DB_URL)

# create Base class
Base = declarative_base()

# Create a SessionLocal class
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)