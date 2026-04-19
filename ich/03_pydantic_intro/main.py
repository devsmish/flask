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
        return f"User {self.name}, {self.age} years old. Email: {self.email}. City: {self.address.city}"


class AdminUser(User):
    is_superuser: bool
    access_level: int

    def __str__(self):
        return f"Admin {self.name}, Email: {self.email}, Access Level: {self.access_level}"

    def promote_user(self):
        # print(f"Promoting {self.name} to higher privileges")
        self.access_level = self.access_level + 1


if __name__ == '__main__':
    json_string = """{
        "id": 1,
        "name": "John Doe",
        "age": 22,
        "email": "john.doe@example.com",
        "is_active": false,
        "is_superuser": false,
        "access_level": 0,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }"""

    user = User.model_validate_json(json_string,
                                    strict=True
                                    )  # Десериализация
    admin = AdminUser.model_validate_json(json_string,
                                          strict=True)
    print(admin)
    # print(user.id, type(user.id))
    # print(user.model_dump_json())  # сериализация
    print(admin.greet())
    print(admin.access_level)
    admin.promote_user()
    print(admin.access_level)
