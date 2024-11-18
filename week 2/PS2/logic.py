class Logic:
    def __init__(self):
        self.product = []

    def place_order(self, Id):
        for i in self.product:
            if i.Id == Id.Id: 
                return False 
        self.product.append(Id)
        return True 
    def view_all(self):
        return self.product
    
    def cancel_order(self, order_id):
        """
        Cancels an order with the given order_id.
        :param order_id: ID of the order to cancel.
        :return: True if order was found and canceled, False otherwise.
        """
        for order in self.product:
            if order.order_id == order_id:
                self.product.remove(order)
                return True
        return False

    def calculate_total_cost(self):
        """
        Calculates the total cost of all product.
        :return: Total cost of all product.
        """
        return sum(order.total for order in self.product)

    def summarize_orders_by_customer(self, customer_id):
        """
        Summarizes all product for a specific customer.
        :param customer_id: ID of the customer.
        :return: List of product for the customer.
        """
        customer_orders = [order for order in self.product if order.customer_id == customer_id]
        summary = {
            'customer_id': customer_id,
            'total_orders': len(customer_orders),
            'product': customer_orders,
            'total_cost': sum(order.total for order in customer_orders)
        }
        return summary

        
        


