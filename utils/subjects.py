from datetime import datetime
from typing import Union

from Programs.Hemis.file_manager import subject_manager


class Subject:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now().__str__()

    @classmethod
    def get_subject(cls, name) -> Union[None, dict]:
        subjects = subject_manager.read()
        for subject in subjects:
            if subject.name.lower() == name.lower():
                return subject
        return None


def add_subject() -> dict:
    name = input("Enter subject name: ")
    while Subject.get_subject(name):
        print("This subject already exists")
        add_subject()

    new_subject = Subject(name).__dict__
    subject_manager.add_data(new_subject)
    return new_subject
