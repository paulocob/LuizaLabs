import json
from io import StringIO
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
    if len(line) < 95:
        raise ValueError(f"linha inválida: {line}")

    user_id = int(line[:10].strip())
    name = line[10:55].strip()
    order_id = int(line[55:65].strip() or '0')  # adiciona verificação para evitar ValueError quando o order_id está vazio
    product_id_str = line[65:75].strip()
    product_id = int(product_id_str) if product_id_str else 0  # adiciona verificação para evitar ValueError quando o product_id está vazio
    value_str = line[75:87].strip()
    value = float(value_str) if value_str else 0.0  # adiciona verificação para evitar ValueError quando o value está vazio
    date = line[87:95].strip()
    formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    return user_id, name, order_id, product_id, value, formatted_date


def process_orders(input_data: str) -> List[Dict]:
    users = {}

    with StringIO(input_data) as file:
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
        with open(input_file, 'r') as f:
            input_data = f.read()

        output_file = f"processed_orders_{i + 1}.json"

        orders_data = process_orders(input_data)
        save_to_file(output_file, orders_data)

        print(f"Output para o arquivo {input_file}:")
        print(json.dumps(orders_data, indent=2))
        print("\n")

if __name__ == "__main__":
    main()

