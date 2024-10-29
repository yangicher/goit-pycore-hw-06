from collections import UserDict
from assistant.models import Record

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def __str__(self):
        count = len(self.data)
        return f"Address Book with {count} records"

    def add_record(self, record: Record):
        if not self.data.get(record.name):
            self.data[record.name] = record
        else:
            print(f"Contact with name: {record.name} already exists")

    def find(self, name: str) -> Record | None:
        if not self.data.get(name):
            print(f"Can't find contact {name}")
        else:
            return self.data[name]

    def delete(self, name: str):
        result = self.data.pop(name)
        return result