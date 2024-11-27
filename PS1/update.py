class Update:
    def __init__(self, name, new_price):
        self.name = name 
        self.new_price = new_price

    def __str__(self):
        return f"name of the product{self.name}, price of the product {self.new_price}"




