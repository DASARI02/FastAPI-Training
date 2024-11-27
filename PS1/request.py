import requests

# Base URL for the manufacturing API
base_url = "http://127.0.0.1:8000"

# 1. GET Request: Fetch all items in the warehouse
def get_items():
    response = requests.get(base_url)
    
    if response.status_code == 200:
        print("Items in Warehouse:")
        print(response.json())  # Display the list of items
    else:
        print(f"Failed to retrieve items. Status code: {response.status_code}")

# 2. POST Request: Add a new item to the warehouse
def add_item(item_data):
    response = requests.post(base_url, json=item_data)
    
    if response.status_code == 201:
        print("Item added successfully:")
        print(response.json())  # Display the added item details
    else:
        print(f"Failed to add item. Status code: {response.status_code}")

# 3. PUT Request: Update an existing item in the warehouse
def update_item(item_id, updated_data):
    url = f"{base_url}/{item_id}"
    response = requests.put(url, json=updated_data)
    
    if response.status_code == 200:
        print("Item updated successfully:")
        print(response.json())  # Display the updated item details
    else:
        print(f"Failed to update item. Status code: {response.status_code}")

# 4. DELETE Request: Delete an item from the warehouse
def delete_item(item_id):
    url = f"{base_url}/{item_id}"
    response = requests.delete(url)
    
    if response.status_code == 204:
        print(f"Item {item_id} deleted successfully.")
    else:
        print(f"Failed to delete item. Status code: {response.status_code}")


# Example Usage

# 1. GET request to fetch all items
get_items()

# 2. POST request to add a new item
new_item = {
    "name": "Steel Rod",
    "quantity": 50,
    "category": "Materials",
    "price_per_unit": 5.00
}
add_item(new_item)

# 3. PUT request to update an existing item
updated_item_data = {
    "name": "Steel Rod",
    "quantity": 75,  # Updated quantity
    "category": "Materials",
    "price_per_unit": 4.80  # Updated price
}
update_item(item_id=1, updated_data=updated_item_data)

# 4. DELETE request to remove an item
delete_item(item_id=2)