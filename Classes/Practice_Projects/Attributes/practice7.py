'''
. Setting Multiple Attributes Dynamically
Create a class Product with attributes name and price. Use a loop with
setattr() to dynamically set several additional attributes (like category, discount, and stock) for an instance of Product.
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

PR1 = Product("Cake",78)
additional_attributes = {
    "category": "Electronics",
    "discount": 10,  # Percentage discount
    "stock": 50      # Number of items in stock
}
for attr,value in additional_attributes.items():
    setattr(PR1, attr, value)

print(PR1.name)
print(PR1.price)
print(getattr(PR1,'category'))
print(getattr(PR1,'discount'))
print(getattr(PR1,'stock'))

