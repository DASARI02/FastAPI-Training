from logic import Logic 
from product import Product 

if __name__ == "__main__":
    a = Logic()

    p1 = Product(1, "Pizza", 500)
    p2 = Product(2, "Burger", 400)

    print(a.place_order(p1))
    print(a.place_order(p2))
    print(a.place_order(p1))
    print()

    b = a.view_all()
    print()
    for i in b:
        print(i)
    
        # View all orders
    print("\nAll Orders:")
    for order in a.view_all():
        print(order.to_dict())  # Print each order as a dictionary

    # Cancel an order
    print("\nCanceling Order with ID 1:")
    print(a.cancel_order(1))  # Should print True

    # View all orders after cancellation
    print("\nOrders after cancellation:")
    for order in a.view_all():
        print(order.to_dict())

    # Place another order
    print("\nPlacing Another Order:")
    print(a.place_order(p2))  # Should print True

    # Calculate the total cost of all orders
    print("\nTotal Cost of All Orders:")
    print(a.calculate_total_cost())
