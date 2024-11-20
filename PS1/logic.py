from product import Product
class Logic:
    def __init__(self):
        self.products = [Product(1,"Maggie",20)]  

    def add_product(self,new_product):
        for i in self.products:
            if i.ID == new_product.ID:
                return False
        self.products.append(new_product)
        return True

    def update_product(self, product_id, updated_product):

        for product in self.products:
            if product.ID == product_id:
                product.name = updated_product.name
                product.price = updated_product.new_price
                return True
        return False
    
    def view_all(self):
        return self.products
    
    
    def discount (self, discounted_product):
        if len(self.products):
            for i in self.products:
                va_price = i.Price*(discounted_product/100)
                i.Price -= va_price
            return self.products
        else:
            return False

#     # def view_all(self):
#     #     return self.products
   
        

            
    


# import csv
# from product import Product
# class Logics:
 
#     def __init__(self):
#         self.products = []
 
 
#     def addProduct(self, newProduct):
#         for nproduct in self.products:
#             if nproduct.productId == newProduct.productId:              
#                 return False
#         self.products.append(newProduct)
#         self.viewProducts()
#         return True
   
 
 
#     def updateProduct(self, productId, newName, newPrice):
#         for uProduct in self.products:
#             if uProduct.productId == productId:
#                 uProduct.productName = str(newName)
#                 uProduct.productPrice = float(newPrice)
#                 return f"Product Updated with Id: {productId},  ProductName: {newName}, ProductPrice {newPrice}"
#             return f"Product Not found"
       
 
 
 
#     def viewProducts(self):
#         return self.products
 
 
#     def applyDiscount(self, discountPercentage):      
#         for dProducts in self.products:
#             discAmount = dProducts.productPrice * discountPercentage / 100
#             dProducts.productPrice = round(dProducts.productPrice - discAmount,2)      
#         return self.products
       
 
#     def writeProductToCsv(self, filename = 'products.csv'):
#         final = False
#         with open(filename, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['productId', 'productName', 'productPrice'])
#             for product in self.products:
#                 writer.writerow(product.writeToCsv())
#                 final = True
#         return final
               
 
 
#     def readProductFromCsv(self, filename = 'products.csv'):
#         self.products.clear()
#         final = False
#         with open(filename, mode='r', newline='') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 self.products.append(Product.readFromCsv(row))
#                 final = True
#         return final