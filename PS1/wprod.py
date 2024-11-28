from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from logic import Logic
from sql import ProductInDB



class Product(BaseModel):
    productid: int
    name: str 
    price : int 



class ProductClass:
    def __init__(self, productID, name, price):
        self.productID = productID
        self.name = name 
        self.price = price 

# Initialize FastAPI app
app = FastAPI()
a = Logic()
@app.post("/addProduct")
async def add_Product(new_Product: Product) :

   
    add = a.add_product(new_Product)
    return add

@app.put("/UpdateProduct")
async def update_product(update_product: Product):

    # print("update_product", update_product)

    return True 

@app.get("/viewall")
async def viewall():
   
    view = a.view_all()
    return view
    
@app.put("/ApplyDiscount")
async def apply_discount(discount_product: float):

    v_price = a.discount(discount_product)
    print(v_price,discount_product,"hi")
    return v_price







# #    def discount (self, discounted_product):
# #         if len(self.products):
# #             for i in self.products:
# #                 va_price = i.Price*(discounted_product/100)
# #                 i.Price -= va_price
# #             return self.products
# #         else:
# #             return False




# from fastapi import FastAPI,status,HTTPException
# from pydantic import BaseModel
# from typing import Dict
# from logic import Logics
 
 
# # Create a Pydantic model for the input
# class Product(BaseModel):
#     productId: int
#     productName: str
#     productPrice: float
 
 
# # Initialize FastAPI app
# app = FastAPI()
# a = Logics()
 
# @app.post("/addProduct",status_code=status.HTTP_201_CREATED)
# async def addProductws(newProduct:Product):
#     add = a.addProduct(newProduct)
#     return add
 
 
# @app.put("/updateProduct")
# async def updateProductws(updateDetails: Product):
#     update = a.updateProduct(updateDetails)
#     return update
 
 
# @app.get("/viewProduct")
# async def viewProductws():
#     view = a.viewProducts()
#     return view
 
 
# @app.put("/applyDiscount")
# async def applyDiscws(discAmount: float):
#     result = a.applyDiscount(discAmount)
#     print(discAmount)
#     return  result
 


    
