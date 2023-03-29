import json

def parse_line(line):
    user_id = int(line[:10].strip())
    name = line[10:55].strip()
    order_id = int(line[55:65].strip())
    product_id = int(line[65:75].strip())
    value = float(line[75:87].strip())
    date = line[87:95].strip()
    formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    return user_id, name, order_id, product_id, value, formatted_date

def process_orders(input_file):
    users = {}
    with open(input_file, 'r') as file:
        for line in file:
            user_id, name, order_id, product_id, value, date = parse_line(line)
            
            if user_id not in users:
                users[user_id] = {
                    "user_id": user_id,
                    "name": name,
                    "orders": {}
                }
                
            if order_id not in users[user_id]["orders"]:
                users[user_id]["orders"][order_id] = {
                    "order_id": order_id,
                    "total": 0,
                    "date": date,
                    "products": []
                }
                
            users[user_id]["orders"][order_id]["products"].append({
                                "product_id": product_id,
                "value": f"{value:.2f}"
            })

            users[user_id]["orders"][order_id]["total"] += value

    output_data = []
    for user in users.values():
        user_orders = list(user["orders"].values())
        for order in user_orders:
            order["total"] = f"{order['total']:.2f}"
        user["orders"] = user_orders
        output_data.append(user)

    return output_data


def main():
    input_files = ["data_1.txt", "data_2.txt"]
    
    for i, input_file in enumerate(input_files):
        output_file = f"processed_orders_{i + 1}.json"
        
        orders_data = process_orders(input_file)
        
        with open(output_file, "w") as file:
            json.dump(orders_data, file, indent=2)
        
        print(f"Output para o arquivo {input_file}:")
        print(json.dumps(orders_data, indent=2))
        print("\n")

        # Faz o download dos arquivos JSON
        downloaded_file = open('downloaded_files','w+')
        json.dump(output_file, downloaded_file)   

if __name__ == "__main__":
    main()