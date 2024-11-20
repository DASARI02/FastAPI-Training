from logic import Logic
from product import Product
from update import Update 
from db import Database

if __name__ == "__main__": 
    # Initialize the Logic instance
    a = Logic()

    # Create and add products to Logic
    p1 = Product(1, "Pizza", 500)
    p2 = Product(2, "Burger", 400)
    p3 = Product(3, "French Fries", 300)

    print(a.add_product(p1))
    print(a.add_product(p2))
    print(a.add_product(p1))

    # # Create an Update object with the new name and price
    updated_product = Update("Veggie Pizza", 550)

    # Update the product with ID 1
    if a.update_product(1, updated_product):
        print("Product updated successfully!")
    else:
        print("Product update failed.")

    for product in a.view_all() :
        print(product)

    #discount 
    # discount_percentage = 10  # Example discount of 10%
    # for product in a.products:
    #     discounted_price = a.calculate_discounted_price(product.ID, discount_percentage)
    #     if discounted_price is not None:
    #         print(f"Product ID: {product.ID}, Name: {product.name}, Original Price: {product.price}, "
    #               f"Discounted Price: {discounted_price}")
    #     else:
    #         print(f"Product with ID {product.ID} not found for discount application.")
discounted_price = 10 
p = a.discount(discounted_price)
print()
for i in p:
    print(i)

v = a.view_all() 
print()
for i in v:
    print(i)

a.close()