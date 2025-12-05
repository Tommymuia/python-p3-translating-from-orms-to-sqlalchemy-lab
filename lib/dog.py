import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog

def create_table(Base, engine):
    """
    Creates all tables for the Base metadata.
    """
    Base.metadata.create_all(engine)


def save(session, dog):
    """
    Saves a Dog instance to the DB.
    """
    session.add(dog)
    session.commit()


def get_all(session):
    """
    Returns all Dog instances.
    """
    return session.query(Dog).all()


def find_by_name(session, name):
    """
    Finds a Dog by name.
    """
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    """
    Finds a Dog by ID.
    """
    return session.query(Dog).filter_by(id=id).first()


def find_by_name_and_breed(session, name, breed):
    """
    Finds a Dog by name and breed.
    """
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, new_breed):
    """
    Updates a Dog's breed and commits changes.
    """
    dog.breed = new_breed
    session.commit()
