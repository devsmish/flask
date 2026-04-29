from itertools import count

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/101025-ptm')

Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    addresses = relationship("Address", back_populates="user")

    def __str__(self):
        return (f"User:\n"
                f"id: {self.id},\n"
                f"name:{self.name},\n"
                f"age: {self.age},\n"
                f"addresses: {[address.description for address in self.addresses]}")


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(100))
    user = relationship("User", back_populates="addresses")

'''Задача 1: Поиск пользователя по имени
Напишите запрос, который возвращает пользователя с конкретным именем (например, "Alice").'''
with Session() as session:
    user = session.query(User).filter(User.name == "Alice").first()
    print(user)
    print("-" * 16)

'''Задача 2: Вывод пользователей с определённым возрастом
Напишите запрос для вывода всех пользователей, возраст которых больше 20 лет.'''
with Session() as session:
    users = session.query(User).filter(User.age > 20).all()
    print(f"Всего найдено {len(users)} записей")
    for user in users:
        print(user)
        print("-" * 16)

'''Задача 3: Обновление данных пользователя
Допустим, вы хотите обновить возраст пользователя "Bob" до 25 лет. Напишите запрос для обновления данных.'''
with Session() as session:
    name = "Bob"
    new_age = 21
    user = session.query(User).filter(User.name == name).first()
    print(user.name, user.age)
    if user:
        user.age = new_age
        session.commit()
    else:
        print("User not found!")
    print(user)
    print("-" * 16)

'''Задача 4: Вывод пользователей моложе 30 лет
Напишите запрос для вывода всех пользователей, возраст которых меньше 30 лет. Выведите их имена и возраст.'''
with Session() as session:
    users = session.query(User).filter(User.age < 30).all()
    print(f"Всего найдено {len(users)} записей")
    for user in users:
        print(f"Имя: {user.name}, возраст: {user.age}")
        print(*[(user.name, user.age) for user in users], sep="\n")

'''Задача 5: Добавление пользователя
Напишите запрос, который добавляет пользователя с именем "Charlie".'''
# charlie = User(name="Charlie", age=21, addresses=[Address(description="Toronto")])
# with Session() as session:
#     session.add(charlie)
#     session.commit()
#     user = session.query(User).filter(User.name == "Charlie").first()
#     print(user)
#     print("-" * 16)

'''Задача 6: Удаление пользователя
Напишите запрос, который удаляет пользователя с определённым именем "Charlie". Выведите информацию о том, был ли он 
удален.'''
# with Session() as session:
#     user = session.query(User).filter(User.name == "Charlie").first()
#     if user:
#         session.delete(user)
#         session.commit()
#         print(f"User ID {user.id} was deleted!")
#     else:
#         print("User not found!")

"""Задача 7: Сортировка пользователей по возрасту
Создайте запрос, который выводит всех пользователей, отсортированных по возрасту в порядке убывания."""
with Session() as session:
    users = session.query(User).order_by(desc(User.age)).all()
    print("*" * 16)
    print(*[(user.id, user.name, user.age) for user in users], sep="\n")
    print("*" * 16)

"""Задача 8: Вывод пользователей с ограничением количества
Напишите запрос, который выводит первые 4 пользователя, отсортированных по имени в алфавитном порядке."""
with Session() as session:
    users = session.query(User).order_by(User.name).limit(4).all()
    print("~" * 16)
    print(*[(user.name, user.age) for user in users], sep="\n")
    print("~" * 16)

"""Задача 9: Обновление данных пользователя по ID
Напишите запрос для обновления данных пользователя, используя его id. Предположим, нужно обновить возраст пользователя 
с id равным 5 до 35 лет."""
with Session() as session:
    user_id = 5
    n_age = 35
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.age = n_age
        session.commit()
        print("!" * 16)
        print(user)
        print("!" * 16)
    else:
        print("User not found")

"""Задача 10: Проверка существования пользователя
Напишите запрос, который проверяет, существует ли пользователь с заданным name. Проверьте наличие пользователя с name 
равным "Charlie"."""
with Session() as session:
    username = "Charlie"
    users = session.query(User).filter(User.name == username).all()
    if len(users) > 0:
        print("@" * 16)
        print(f"В БД найдено {len(users)} пользователь с именем {username}")
        print(*[(user.name, user.age) for user in users], sep="\n")
        print("@" * 16)
    else:
        print("User not found")

"""Задача 11: Среднее значение возрастов
Напишите запрос, который находит средний возраст всех пользователей, и выведите результат."""
with Session() as session:
    avg_age = session.query(func.avg(User.age)).scalar()
    print("Средний возраст:", avg_age, "лет")
