class GroceryStore:
    def __init__(self, name, apples_sold, apple_price, oranges_sold, orange_price):
        self.name = name
        self.apples_sold = apples_sold
        self.apple_price = apple_price
        self.oranges_sold = oranges_sold
        self.orange_price = orange_price

    def yearly_revenue(self):
        return (self.apples_sold * self.apple_price) + (self.oranges_sold * self.orange_price)



bambaraush = GroceryStore("Бамбарууш", 534, 5000, 487, 10000)
jimshen = GroceryStore("Жимсэн", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)


stores = [bambaraush, jimshen, fruits]

total_revenue = 0
for store in stores:
    revenue = store.yearly_revenue()
    print(f"{store.name} дэлгүүрийн орлого: {revenue}")
    total_revenue += revenue

print(f"Нийт борлуулалтын орлого: {total_revenue}")