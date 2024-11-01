import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    pattern = r"^\d{10}$"

    def __init__(self, value):
        super().__init__(value)
        if re.match(self.pattern, value):
            self.value = value
        else:
            print("Invalid phone number")

class Record:
    def __init__(self, name : Name):
        self.name = name
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
    
    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def remove_phone(self, phone: str):
        for i, phone in self.phones:
            if phone.value == phone:
                self.phones.pop(i)
                break

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone == old_phone:
                phone = new_phone
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone == phone_number:
                return phone
        return None
        