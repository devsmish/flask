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
    print("-" * 16)

"""Задача 12: Максимальный и минимальный возраст
Создайте запрос, который найдет максимальный и минимальный возраст среди пользователей. Используйте функции func.max() 
и func.min()."""
with Session() as session:
    age_min = session.query(func.min(User.age)).scalar()
    age_max = session.query(func.max(User.age)).scalar()
    print(f"Минимальный {age_min} и максимальный {age_max} возраст пользователей")
    print("-" * 16)

with Session() as session:
    min_max =  session.query(func.max(User.age).label('max_age'),
                             func.min(User.age).label('min_age')).one()
    print(min_max)
    print("-" * 16)

"""Задача 13: Группировка пользователей по возрасту
Напишите запрос, который группирует пользователей по возрасту и подсчитывает количество пользователей в каждой 
возрастной группе."""
with Session() as session:
    group_users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
    print(*[(item[0], item[1]) for item in group_users], sep="\n")
    print("#" * 16)

with Session() as session:
    groups_age = session.query(User.age, func.count(User.id)).group_by(User.age).all()
    for age, count in groups_age:
        print(f"Age {age}: count {count}")
        print("-" * 16)

"""Задача 14: Фильтрация групп с использованием having()
Измените предыдущий запрос так, чтобы он возвращал только те возрастные группы, где количество пользователей больше 1.
Используйте having() для фильтрации результатов агрегации."""
with Session() as session:
    group_users = session.query(User.age, func.count(User.id)).group_by(User.age).having(func.count(User.id) > 1).all()
    print(*[(item[0], item[1]) for item in group_users], sep="\n")
    print("#" * 16)

with Session() as session:
    age_groups = session.query(User.age, func.count(User.id)).group_by(User.age).having(func.count(User.id)>1).all()
    for age, count in age_groups:
        print(f"Age: {age}, Count: {count}")

"""Задача 15: Присоединение и подзапросы
Создайте подзапрос, который вычисляет средний возраст пользователей, а затем напишите основной запрос, который выбирает 
пользователей старше среднего возраста."""
with Session() as session:
    avg_age_subquery = session.query(func.avg(User.age)).scalar_subquery()
    print("Average age:", avg_age_subquery)
    older_users = session.query(User).filter(User.age > avg_age_subquery).all()
    for user in older_users:
        print(user.name, user.age)
    print("$" * 16)

with Session() as session:
    subquery = session.query(func.avg(User.age).label('average_age'), func.max(User.age).label('max_age')).subquery()
    query = session.query(User).filter(User.age > subquery.c.average_age).all()
    print(*query)

"""Задача 16: Вывод всех адресов пользователей
Напишите запрос, который выводит всех пользователей вместе с их адресами."""
with Session() as session:
    full_users = session.query(User).outerjoin(Address).all()
    for user in full_users:
        for address in user.addresses:
            print(f"{user.id}. {user.name}: {user.age} from {address.description}")
    print("%" * 16)

"""Задача 17: Пользователи без адресов
Напишите запрос, который выводит пользователей, у которых нет адресов."""
with Session() as session:
    users_without_adr = session.query(User).outerjoin(Address).filter(Address.id == None).all()
    print(*users_without_adr)
    print("^" * 16)

"""Задача 18: Подсчёт пользователей в каждом городе
Создайте запрос, который подсчитывает количество пользователей в каждом городе."""
with Session() as session:
    users_in_city = session.query(Address.description, func.count(User.id)).join(User).group_by(Address.description).all()
    for city, count in users_in_city:
        print(f"{city}: {count}")

"""Задача 19: Поиск пользователей по городу
Напишите запрос для поиска всех пользователей из определённого города, например, из "Berlin"."""
with Session() as session:
    berlin_users = session.query(User).join(Address).filter(Address.description == "Berlin").all()
    for user in berlin_users:
        for address in user.addresses:
            print(user.name, address.description)
        print("-" * 16)

"""Задача 20: Обновление адреса пользователя
Предположим, что нужно обновить адрес пользователя "Bob" на "Paris". Напишите соответствующий запрос."""
with Session() as session:
    user_bob = session.query(User).filter(User.name == "Bob").first()
    if user_bob:
        for address in user_bob.addresses:
            address.description = "Paris"
        session.commit()
        print("&" * 16)
        print(user_bob)
        print("-" * 16)
    else:
        print("User not found")
