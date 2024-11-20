import csv
class Product:
    def __init__(self, Id, name, Price):
        self.ID = Id
        self.name = name 
        self.Price = Price

    def __str__(self):
        return f"product {self.ID}, name of product {self.name}, price of product{self.Price}"
    def write_to_csv(self):
        return [self.ID, self.name, self.Price]

    
    
    
    # def __str__(self):
    #     price_info = f"Price: {self.price}"
    #     if self.discounted_price is not None:
    #         price_info += f", Discounted Price: {self.discounted_price}"
    #     return f"Product ID: {self.ID}, Name: {self.name}, {price_info}"



# class Product:
#     def __init__(self, productId, productName, productPrice):
#         self.productId = productId
#         self.productName = productName
#         self.productPrice = float(productPrice)
       
#     def __repr__(self):
#         return f"Product({self.productId},{self.productName},{self.productPrice})"
   
#     def writeToCsv(self):
#         return [self.productId, self.productName, self.productPrice]
   
 
#     @classmethod
#     def readFromCsv(cls, row):
#         productId, productName, productPrice = row
#         return cls(int(productId), productName, float(productPrice))