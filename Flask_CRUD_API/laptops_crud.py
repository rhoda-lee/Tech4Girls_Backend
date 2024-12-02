from config import session
from models import Laptops



class LaptopsCrud:
    def __init__(self, session):
        self.session = session

    def insert_laptop(self, laptop_name, laptop_number, specification):
        new_laptop = Laptops(laptop_name = laptop_name, laptop_number = laptop_number, specification = specification)
        self.session.add(new_laptop)
        self.session.commit()
        return f'Laptop with name {laptop_name} and number {laptop_number} with specifications: {specification} has been added'
    
    def search_laptop(self, search):
        return self.session.query(Laptops).filter(
            (Laptops.laptop_name.ilike(f"%{search}%")) |
            (Laptops.specification.ilike(f"%{search}%"))
        ).all()
    
    def select_all_laptop(self):
        return self.session.query(Laptops).all()
    
    def select_laptop_by_name(self, laptop_name):
        return self.session.query(Laptops).filter_by(laptop_name = laptop_name).first()
    
    def select_laptop_by_number(self, laptop_number):
        return self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
    
    def select_laptop_by_specification(self, specification):
        return self.session.query(Laptops).filter_by(specification = specification).first()
    
    def update_laptop(self, laptop_number, laptop_name = None, specification = None):
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
        if selected_laptop:
            if laptop_name:
                selected_laptop.laptop_name = laptop_name
            if specification:
                selected_laptop.specification = specification
            self.session.commit()
        return selected_laptop
    
    def delete_laptop(self, laptop_number):
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
        if selected_laptop:
            self.session.delete(selected_laptop)
        self.session.commit()
        return f'Laptop with laptop number: {laptop_number} has been removed.'




# Creating an instance of the LaptopsCrud class for this session
laptopscrud = LaptopsCrud(session)
