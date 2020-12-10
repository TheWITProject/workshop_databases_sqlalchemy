
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"

    # add properties here

    # add relationships here


class Task(Base):
    __tablename__ = "tasks"

    # add properties here

    # add relationships here


class Project(Base):
    __tablename__ = "projects"

    # add properties here

    # add relationships here