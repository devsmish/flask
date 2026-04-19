'''Создать систему для управления учетными записями пользователей, где необходимо:
Валидировать что email оканчивается на .com.
Проверить, что имя пользователя содержит только буквы.'''
from pydantic import BaseModel, EmailStr, field_validator
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_active: bool = True


    @field_validator("email")
    def valid_emails(cls, value):
        if value[-4:] == ".com":
            return value
        raise ValueError("Must have .come")

    @field_validator("name")
    def valid_name(cls, value):
        if not value.isalpha():
            raise ValueError("Must have only alpha")
        return value



if __name__ == "__main__":

    user = User(name="Ivan12", age=156, email="Ivan123@gmail.com")