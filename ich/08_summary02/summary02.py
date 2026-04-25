# PYDANTIC
'''Задача 1: Определение модели события
Задание: Создайте модель Event, которая включает поля title (строка), date (дата и время события), и
location (строка). Добавьте валидацию, чтобы дата события не была в прошлом.'''
from pydantic import BaseModel, field_validator
from datetime import datetime, timedelta


class Event(BaseModel):
    title: str
    date: datetime
    location: str

    @field_validator('date')
    @classmethod
    def date_validator(cls, value):
        if value <= datetime.now():
            raise ValueError('The date can not be in the past')
        return value

event = Event(title='Python Advanced', date=datetime(2026,5,10,18,7), location='Berlin')
print(event)
# old_event = Event(title='Python Advanced', date=datetime(2026,3,10,18,7), location='Berlin')
# print(old_event)

try:
    future_event = Event(title="New Year Party", date=datetime.now() + timedelta(days=30), location="New York")
    print(future_event)
except ValueError as e:
    print(e)

'''Задача 2: Создание модели для пользователя с настройками
Задание: Определите модель UserProfile с полями username (строка), password (строка), и email (строка с валидацией
email). Используйте Field для добавления описаний и настройки валидации пароля (должен быть не менее 8 символов).'''
from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserProfile(BaseModel):
    username: str
    password: SecretStr = Field(..., min_length=8)
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe",
                "password": "securePassword123",
                "email": "john.doe@example.com"
            }
        }

user_profile = UserProfile(username='Serg', password='12345678', email='serg@gmail.com')
print(user_profile)
# bad_user_profile = UserProfile(username='3', password='1234567890', email='3@net')
# print(bad_user_profile)

'''Задача 3: Модель для управления транзакциями
Задание: Разработайте модель Transaction для управления финансовыми
операциями. Модель должна содержать amount (десятичное число), transaction_type (строка, принимает значения "debit"
или "credit"), и currency (строка).'''
# Pydantic v1
from pydantic import BaseModel, constr, condecimal


class Transaction(BaseModel):
    amount: condecimal(gt=0)
    transaction_type: constr(regex="^(debit|credit)$")
    currency: constr(min_length=3, max_length=3)

    class Config:
        any_str_strip_whitespace = True

# Пример транзакции
transaction = Transaction(amount=150.50, transaction_type="debit", currency="USD")
print(transaction)

# Pydantic v2
from typing import Annotated
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field


class TransactionType(str, Enum):
    debit = "debit"
    credit = "credit"

class Transaction(BaseModel):
    amount: Annotated[Decimal, Field(gt=0)]
    transaction_type: TransactionType
    currency: Annotated[str, Field(min_length=3, max_length=3)]

    model_config = {
        "str_strip_whitespace": True
    }

# Пример
transaction = Transaction(
    amount=150.50,
    transaction_type="debit",
    currency=" USD "
)

print(transaction)

'''Задача 4: Модель с расширенной валидацией даты
Задание: Создайте модель Appointment для записи на прием, которая включает patient_name (строка), appointment_date 
(дата и время), и проверку, что запись не может быть установлена ранее, чем через 24 часа от текущего момента.'''
from pydantic import BaseModel, field_validator
from datetime import datetime, timedelta


class Appointment(BaseModel):
    patient_name: str
    appointment_date: datetime

    @field_validator('appointment_date')
    def check_appointment_date(cls, v):
        if v < datetime.now() + timedelta(days=1):
            raise ValueError("Appointment must be scheduled at least 24 hours in advance.")
        return v

# Пример использования
try:
    appointment = Appointment(patient_name="Alice Smith", appointment_date=datetime.now() + timedelta(hours=25))
    print(appointment)
except ValueError as e:
    print(e)

# SQLALCHEMY
'''Задача 5: Создание движка подключения 
Задание: Создайте экземпляр движка для подключения к MySQL базе данных.'''
from sqlalchemy import create_engine, text


engine = create_engine('mysql+pymysql://user:password@localhost/mydatabase')

'''Задача 6: Настройка движка:
Напишите код для создания движка SQLAlchemy с подключением к базе данных SQLite, который будет располагаться в 
памяти, и настройте вывод логов всех операций с базой данных на экран.'''
from sqlalchemy import create_engine
import logging


logging.basicConfig(level=logging.INFO)
engine = create_engine('sqlite:///memory.db', echo=True)

with engine.connect() as conn:
    conn.execute(text("SELECT 7"))

'''Задача 7: Определение модели пользователя:
Создайте модель User с полями id (целочисленный тип, первичный ключ), name (строковый тип, длина до 50 символов), и 
age (целочисленный тип).'''
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

'''Задача 8: Моделирование и связи:Определите две модели, User и Post, где пользователь может иметь много 
постов (один ко многим). Используйте декларативный базовый класс.'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

Base.metadata.create_all(engine)

'''Задача 9: Моделирование и связи:
Определите две модели: User и Address, где User может иметь множество Address. Используйте декларативный базовый 
класс.'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

Base.metadata.create_all(engine)

'''Задание 6
Работа с сессией для добавления и удаления записей
Используя ранее определённые модели User и Address, создайте нового пользователя и
адрес, добавьте их в базу данных с помощью сессии, затем удалите пользователя и
проверьте изменения.'''
from sqlalchemy.orm import sessionmaker

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание нового пользователя и адреса
new_user = User(name="John Doe", age=28)
new_address = Address(user=new_user, description="123 Elm Street")

# Добавление в базу данных
session.add(new_user)
session.add(new_address)
session.commit()

# Удаление пользователя и проверка
session.delete(new_user)
session.commit()

# Проверка, что пользователь удалён
print(session.query(User).filter_by(name="John Doe").first())
