from config import session
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Laptops(Base):
    __tablename__ = 'laptops'
    laptop_name = Column(String(100), nullable = False)
    laptop_number = Column(Integer, primary_key = True, nullable = False)
    specification = Column(String(250), nullable = False)

    def __str__(self):
        return f'Laptop Name: {self.laptop_name}\nLaptop Number: {self.laptop_number}\nLaptop Specification: {self.specification}'
    

if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print(f'The Laptops table has been created successfully!')
    except Exception as e:
        print(f'There was an error: {e}')