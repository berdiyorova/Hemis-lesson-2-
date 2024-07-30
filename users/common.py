import hashlib
from enum import Enum
from typing import Union

from Programs.Hemis.file_manager import user_manager
from Programs.Hemis.logs import log_decorator

admin_username = "1"
admin_password = "1"


class UserTypes(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"


class User:
    def __init__(self, passport_id, username, password, user_type, first_name, last_name, phone_number):
        self.passport_id = passport_id
        self.username = username
        self.password = password
        self.user_type = user_type
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.is_login = False

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


def find_user(username: str, password: str) -> Union[dict, bool]:
    """read users.json file and find the matching user, if not found, return False"""
    for user in user_manager.read():
        if user['username'] == username and user['password'] == password:
            return user
    return False


def login() -> Union[bool, dict]:
    """
    Searching user from file, if exists return user, or it's type, and if not False
    """
    username: str = input("Enter your username: ")
    password: str = input("Enter your password: ")

    if username == admin_username and password == admin_password:
        return {'user_type': UserTypes.ADMIN.value}

    hashed_password: str = User.hash_password(password=password)
    user = find_user(username, hashed_password)
    if user:
        return user

    return False


@log_decorator
def add_user(user_type: str) -> dict:
    """add user with it is type to file"""

    passport_id: str = input("Enter passport ID: ").upper().strip()
    username: str = input("Enter your username: ").strip()
    password: str = input("Enter your password: ").strip()
    first_name: str = input("Enter your first name: ").strip()
    last_name: str = input("Enter your last name: ").strip()
    phone_number: str = input("Enter your phone number: ").strip()

    hashed_password: str = User.hash_password(password=password)
    new_user = User(username=username, password=hashed_password,
                    first_name=first_name, last_name=last_name,
                    phone_number=phone_number, user_type=user_type,
                    passport_id=passport_id).__dict__

    user_manager.add_data(data=new_user)
    return new_user
