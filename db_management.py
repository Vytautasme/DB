from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_alchemy.models import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


class DBManagement:
    def __init__(self):
        self.session = session

    def add_value(self, projektas: Projektas):
        self.session.add(projektas)
        self.session.commit()

    def get_value_by_id(self):
        value = session.query(Projektas).get(id)
        print(value)

    def filter_by_name(self, name):
        value = self.session.query(Projektas).filter_by(name=name).all()
        print(value)

    def update_value(self, id, new_name, new_salary):
        value = self.session.query(Projektas).get(id)
        value.name = new_name
        value.salary = new_salary
        self.session.commit()
