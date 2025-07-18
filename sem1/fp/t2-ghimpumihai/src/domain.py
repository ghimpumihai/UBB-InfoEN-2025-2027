class Address:
    def __init__(self,address_id,street_name,street_number,x,y):
        self.address_id = address_id
        self.street_name = street_name
        self.street_number = street_number
        self.x = x
        self.y = y
    def __str__(self):
        return f"Address(id={self.address_id}, street_name='{self.street_name}', street_number={self.street_number}, x={self.x}, y={self.y})"
