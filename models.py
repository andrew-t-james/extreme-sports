import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Categories(Base):
    '''Create model for season and relationship to Sport'''
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    season = Column(String(80), nullable=False)
    sports = relationship('Sports')

    @property
    def serialize(self):
        '''Returns data to be JSONified for apis'''
        return {
            'season': self.season,
            'id': self.id
        }


class Sports(Base):
    '''Create model for xGames sport'''
    __tablename__ = 'sport'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    description_link = Column(String(250))
    image_link = Column(String(250))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Categories')

    @property
    def serialize(self):
        '''Returns data to be JSONified for apis'''
        return {
            'name': self.name,
            'description': self.description,
            'description_link': self.description_link,
            'image_link': self.image_link,
            'id': self.id
        }


ENGINE = create_engine('sqlite:///catalogue.db')

Base.metadata.create_all(ENGINE)
