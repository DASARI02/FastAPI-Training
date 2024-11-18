        
    
# class Logic:
 
#     def __init__(self):
#         self.Products = []
 
 
 
#     def addProduct(self, new_product):
#         for nproduct in self.Products:
#             if nproduct.productId == new_product.productId:              
#                 return False
#         self.Products.append(new_product)
#         return True
 
 
 
#     def updateProduct(self, productId, new_name, new_price):
#         for uProduct in self.Products:
#             if uProduct.productId == productId:
#                 uProduct["ProductName"] = new_name
#                 uProduct["ProductPrice"] = new_price
#                 # print(f"Product {productId} Updated: \nName: {newName} \nPrice: {newPrice}")
#                 return
#         #print("Task Not Found")
 
 
 
    # def viewProducts(self):
    #     print(self.Products)
 
 
 
    # def applyDiscount(self, discountPercentage):
    #     if discountPercentage < 0 or discountPercentage > 100:
    #         print("Invalid discount percentage.")
    #         return
       
        # for ADproduct in self.Products:
        #     originalPrice = ADproduct.productPrice
        #     discountPrice = originalPrice - (originalPrice * discountPercentage / 100)
        #     ADproduct.productPrice = round(discountPrice,2)
        #     print(f"Discount applied to {ADproduct.productName}, \nOriginal Price {originalPrice}, \nAfter Discount {ADproduct.productPrice}")
       
       

    # def update(self, product, updated_product):
    #     for i in self.product:
    #         if i.ID == product.ID:
    #             i.name = updated_product.name
    #             i.price = updated_product.new_price
    #             return True
    #     return False
    


# logic.py
# class Logic:
#     def __init__(self):
#         self.products = []  # List to store products

#     def add_product(self, product):
#         self.products.append(product)
#         return f"Product '{product.name}' added successfully."

#     def update_product(self, product_id, updated_product):
#         # Loop through products to find the matching ID
#         for product in self.products:
#             if product.ID == product_id:
#                 # Update product attributes with those from updated_product
#                 product.name = updated_product.name
#                 product.price = updated_product.new_price
#                 return True
#         return False


class Logic:
    def __init__(self):
        self.products = []  

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
    # def discount(self, discounted_price):
    #     def calculate_discounted_price(self, product_id, discount_percentage):
    #     # Find the product by ID and apply the discount
    #         for product in self.products:
    #             if product.ID == product_id:
    #                 discount = product.price * (discount_percentage / 100)
    #                 product.discounted_price = product.price - discount
    #                 return product.discounted_price
    #         return None
    
#price = price - (price*(discount/100))
    def discount (self, discounted_product):
        if len(self.products):
            for i in self.products:
                va_price = i.Price*(discounted_product/100)
                i.Price -= va_price
            return self.products
        else:
            return False

    def view_all(self):
        return self.products
   
        

            
    
