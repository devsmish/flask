'''Задача 1: Создание движка подключения
Задание: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///:memory:')
'''Задача 2: Создание сессии
Задание: Создайте сессию в продолжение к предыдущему коду.'''

Session = sessionmaker(bind=engine)
session = Session()
