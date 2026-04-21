# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase
#
# engine = create_engine('sqlite:///example.db', echo=True)
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# # Определяем класс `User`, который наследуется от базового класса `Base`.
# # Этот класс представляет собой сущность базы данных.
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     age = Column(Integer)
#
#
# # Для того чтобы в базе данных появилась таблицы вызываем метод `create_all()` объекта `metadata` базового класса `Base`
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# with Session() as session:
#     with session.begin():
#         new_user = User(name="John Doe", age=30)
#         session.add(new_user)
#
# print(new_user)
# print(session.is_active)

# SQL Alchemy 1.0
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# import logging
#
# engine = create_engine('sqlite:///example.db')
#
# # Настройка базового логирования
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s | %(levelname) | %(name)s | %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )
#
# # Включение логирования SQL-запросов
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# # Определяем класс `User`, который наследуется от базового класса `Base`.
# # Этот класс представляет собой сущность базы данных.
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     age = Column(Integer)
#
#
# # Для того чтобы в базе данных появилась таблицы вызываем метод `create_all()` объекта `metadata` базового класса `Base`
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# with Session() as session:
#     with session.begin():
#         new_user = User(name="John Doe", age=30)
#         session.add(new_user)
#
# print(new_user)
# print(session.is_active)

# SQL Alchemy 2.0
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('sqlite:///example.db')  # без echo


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age})"


Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="John Doe", age=30)
    session.add(user)
    session.commit()

    print(user)