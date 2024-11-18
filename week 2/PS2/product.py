class Product:
    def __init__(self, Id, name, Price):
        self.Id = Id
        self.name = name
        self.Price = Price

    def __str__(self):
        """
        Returns a string representation of the Product.
        """
        return f"Product(Id: {self.Id}, Name: {self.name}, Price: {self.Price})"

    def to_dict(self):
        """
        Returns a dictionary representation of the Product.
        """
        return {
            "product Id": self.Id,
            "product name": self.name,
            "Product Price": self.Price
        }
