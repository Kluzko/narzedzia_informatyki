from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class AgeData(Base):
    __tablename__ = 'age_data'
    id = Column(Integer, primary_key=True)
    sheet_name = Column(String)
    age_group = Column(String)
    count = Column(Integer)

class DiseaseData(Base):
    __tablename__ = 'disease_data'
    id = Column(Integer, primary_key=True)
    sheet_name = Column(String)
    disease_code = Column(String)
    count = Column(Integer)

# Konfiguracja połączenia z bazą danych 
engine = create_engine('sqlite:///death_data.db')
Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()
