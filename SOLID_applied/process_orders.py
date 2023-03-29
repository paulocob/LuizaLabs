import json
from typing import List, Dict

class Order:
    def __init__(self, order_id: int, date: str):
        self.order_id = order_id
        self.date = date
        self.total = 0
        self.products = []

    def add_product(self, product_id: int, value: float):
        self.products.append({
            "product_id": product_id,
            "value": f"{value:.2f}"
        })
        self.total += value

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "date": self.date,
            "total": f"{self.total:.2f}",
            "products": self.products
        }

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.orders = {}

    def add_order(self, order: Order):
        self.orders[order.order_id] = order

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "orders": [order.to_dict() for order in self.orders.values()]
        }

def parse_line(line: str):
    user_id = int(line[:10].strip())
    name = line[10:55].strip()
    order_id = int(line[55:65].strip())
    product_id = int(line[65:75].strip())
    value = float(line[75:87].strip())
    date = line[87:95].strip()
    formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    return user_id, name, order_id, product_id, value, formatted_date

def process_orders(input_file: str) -> List[Dict]:
    users = {}

    with open(input_file, 'r') as file:
        for line in file:
            user_id, name, order_id, product_id, value, date = parse_line(line)

            if user_id not in users:
                users[user_id] = User(user_id, name)

            if order_id not in users[user_id].orders:
                users[user_id].add_order(Order(order_id, date))

            users[user_id].orders[order_id].add_product(product_id, value)

    return [user.to_dict() for user in users.values()]

def save_to_file(output_file: str, data: List[Dict]):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=2)

def main():
    input_files = ["data_1.txt", "data_2.txt"]

    for i, input_file in enumerate(input_files):
        output_file = f"processed_orders_{i + 1}.json"

        orders_data = process_orders(input_file)
        save_to_file(output_file, orders_data)

        print(f"Output para o arquivo {input_file}:")
        print(json.dumps(orders_data, indent=2))
        print("\n")

        # Faz o download dos arquivos JSON
        downloaded_file = open('downloaded_files','w+')
        json.dump(output_file, downloaded_file) 

if __name__ == "__main__":
    main()