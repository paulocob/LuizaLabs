import unittest
from SOLID_applied.process_orders import process_orders


class TestProcessOrders(unittest.TestCase):

    def test_process_orders(self):
        with open("input_path.txt", "r") as f:
            input_data = f.read()

        expected_output = [
            {
                "user_id": 70,
                "name": "Palmer Prosacco",
                "orders": [
                    {
                        "order_id": 753,
                        "date": "2021-03-08",
                        "total": "1836.74",
                        "products": [
                            {
                                "product_id": 3,
                                "value": "1836.74"
                            }
                        ]
                    }
                ]
            },
            {
                "user_id": 75,
                "name": "Bobbie Batz",
                "orders": [
                    {
                        "order_id": 798,
                        "date": "2021-11-16",
                        "total": "1578.57",
                        "products": [
                            {
                                "product_id": 2,
                                "value": "1578.57"
                            }
                        ]
                    }
                ]
            },
            {
                "user_id": 49,
                "name": "Ken Wintheiser",
                "orders": [
                    {
                        "order_id": 523,
                        "date": "2021-09-03",
                        "total": "586.74",
                        "products": [
                            {
                                "product_id": 3,
                                "value": "586.74"
                            }
                        ]
                    }
                ]
            }
        ]

        output = process_orders(input_data)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
