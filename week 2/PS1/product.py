import csv
class Product:
    def __init__(self, Id, name, Price):
        self.ID = Id
        self.name = name 
        self.Price = Price

    def __str__(cls, self):
        return f"product {self.ID}, name of product {self.name}, price of product{self.Price}"
    def write_to_csv(self):
        return [self.Id, self.name, self.Price]
    
    @classmethod 
    
    
    
    # def __str__(self):
    #     price_info = f"Price: {self.price}"
    #     if self.discounted_price is not None:
    #         price_info += f", Discounted Price: {self.discounted_price}"
    #     return f"Product ID: {self.ID}, Name: {self.name}, {price_info}"
