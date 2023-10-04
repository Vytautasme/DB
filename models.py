import datetime
from sqlalchemy import Column, Integer, DateTime, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')

Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True)
    name = Column('Vardas', String)
    surname = Column('Pavardė', String)
    salary = Column("Atlyginimas", Integer)
    taxes = Column('Mokesčiai', Float)
    working_from = Column('Dirba nuo', DateTime, default=datetime.datetime.now())

    def __init__(self, name, surname, salary, taxes):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.taxes = taxes

    def __repr__(self):
        return (f'{self.id} {self.name} {self.surname} - {self.salary},'
                f' {self.taxes} : {self.working_from}')


Base.metadata.create_all(engine)
