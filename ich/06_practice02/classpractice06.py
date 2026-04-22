'''Задача 1: Определение модели продукта:
Определите модель Product с различными типами колонок: id (числовой идентификатор), name (строковый), price (точный
дробный), in_stock (логический)'''
from tkinter import Text

from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(DECIMAL(10,2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))

'''Задача 2: Определение связанной модели категории продукта:
Определите модель Category, которая будет связана с моделью Product для организации продуктов по категориям. Каждый 
продукт должен принадлежать одной категории. Category должна включать колонки: id (числовой идентификатор), 
name (строковый), description (строковый).'''

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(160))
    description = Column(Text)

    product = relationship("Product", backref="category")