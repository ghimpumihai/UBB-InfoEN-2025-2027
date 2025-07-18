import os
from domain import Address
class TextFileRepository:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        self.addresses = {}
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                address_id, street_name, street_number,x,y = line.strip().split(',')
                self.addresses[int(address_id)] = Address(int(address_id), street_name, int(street_number),int(x),int(y))
    def _save(self):
        with open(self.filename, 'w') as file:
            for address in self.addresses.values():
                file.write(f"{address.address_id},{address.street_name},{address.street_number},{address.x},{address.y}\n")

    def add(self, address):
        if address.address_id in self.addresses:
            raise ValueError("Address with this ID already exists.")
        if address.address_id<0:
            raise ValueError("ID must be positive.")
        if len(address.street_name)<3:
            raise ValueError("Name must have at least 3 characters.")
        self.addresses[address.address_id] = address
        self._save()
    def get_all(self):
        return list(self.addresses.values())