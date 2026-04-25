'''Задача 1: Вывод всех пользователей
Напишите простой запрос для вывода имен всех пользователей из таблицы User.'''
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from sqlalchemy import desc

Base = declarative_base()
engine = create_engine('sqlite:///example_2.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Base.metadata.create_all(engine)

# user1 = User(name="Katrin", age=23)
# user2 = User(name="Hanna", age=52)
# session.add_all([user1, user2])
# session.commit()

user = session.query(User.name).all()
print(user)

'''Задача 2: Подсчёт общего количества пользователей. Используйте функцию func.count() для подсчёта общего количества 
пользователей в базе данных.'''
total_users1 = session.query(User).count()
print(total_users1)
total_users2 = session.query(func.count())
print(total_users2)
total_users3 = session.query(func.count(User.id)).scalar()
print(total_users3)
