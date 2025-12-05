from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

    def __repr__(self):
        return f"<Dog id={self.id} name={self.name} breed={self.breed}>"
