# from pydantic import BaseModel, EmailStr


# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     is_active: bool = True
#
# if '__name__' == '__main__':
#     user = User(id=1, name='Danil', age=30, is_active=True)
#     print(user)

# class Address(BaseModel):
#     city: str
#     street: str
#     house_number: int
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     is_active: bool = True
#     address: Address


# if '__name__' == '__main__':
#     address = Address(city="New York", street="Green", house_number=1)
#     user = User(id=1, name="John Doe", age=30, address=address)
#     print(user.model_dump_json())

from pydantic import BaseModel, EmailStr, ValidationError


class Address(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    is_active: bool = True
    address: Address

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __str__(self):
        return f"{self.name}, {self.age} years old"

class AdminUser(User):
    is_superuser: bool
    access_level: int



if __name__ == '__main__':
    json_string = """{
        "id": "1",
        "name": "John Doe",
        "age": 22,
        "email": "john.doe@example.com",
        "is_active": false,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }"""

    user = User.model_validate_json(json_string) # десериализация
    print(user)
    # print(user.id, type(user.id))
    print(user.model_dump_json())  # сериализация
