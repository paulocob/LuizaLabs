import unittest
from io import StringIO
from SOLID_applied.process_orders import parse_line, process_orders, User, Order

class TestOrders(unittest.TestCase):

    def test_parse_line(self):
        line = "0000000002 Medeiros00000123450000000111 256.2420201201\n"
        expected_output = (2, "Medeiros", 12345, 111, 256.24, "2020-12-01")
        self.assertEqual(parse_line(line), expected_output)

    def test_process_orders(self):
        input_data = "doc_test.txt"
        expected_output = [
            {
                "user_id": 1,
                "name": "Zarelli",
                "orders": [
                    {
                        "order_id": 123,
                        "total": "1024.48",
                        "date": "2021-12-01",
                        "products": [
                            {
                                "product_id": 111,
                                "value": "512.24"
                            },
                            {
                                "product_id": 122,
                                "value": "512.24"
                            }
                        ]
                    }
                ]
            },
            {
                "user_id": 2,
                "name": "Medeiros",
                "orders": [
                    {
                        "order_id": 12345,
                        "total": "512.48",
                        "date": "2020-12-01",
                        "products": [
                            {
                                "product_id": 111,
                                "value": "256.24"
                            },
                            {
                                "product_id": 122,
                                "value": "256.24"
                            }
                        ]
                    }
                ]
            }
        ]
        self.assertEqual(process_orders(input_data), expected_output)

    def test_user_class(self):
        user = User(1, "Zarelli")
        order = Order(123, "2021-12-01")
        order.add_product(111, 512.24)
        order.add_product(122, 512.24)
        user.add_order(order)
        expected_output = {
            "user_id": 1,
            "name": "Zarelli",
            "orders": [
                {
                    "order_id": 123,
                    "total": "1024.48",
                    "date": "2021-12-01",
                    "products": [
                        {
                            "product_id": 111,
                            "value": "512.24"
                        },
                        {
                            "product_id": 122,
                            "value": "512.24"
                        }
                    ]
                }
            ]
        }
        self.assertEqual(user.to_dict(), expected_output)

    def test_order_class(self):
        order = Order(123, "2021-12-01")
        order.add_product(111, 512.24)
        order.add_product(122, 512.24)
        expected_output = {
            "order_id": 123,
            "total": "1024.48",
            "date": "2021-12-01",
            "products": [
                {
                    "product_id": 111,
                    "value": "512.24"
                },
                {
                    "product_id": 122,
                    "value": "512.24"
                }
            ]
        }
        self.assertEqual(order.to_dict(), expected_output)

if __name__ == "__main__":
    unittest.main()
