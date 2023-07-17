import unittest
from app import app, transactions

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Configure the Flask app for testing
        app.testing = True
        self.client = app.test_client()

        # Set up sample data for testing
        transactions.clear()
        transactions.extend([
            {'id': 1, 'date': '2023-06-01', 'amount': 100},
            {'id': 2, 'date': '2023-06-02', 'amount': -200}
        ])

    # Test getting the transactions list ("/" route)
    def test_get_transactions(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Expect a successful response

    # Test adding a new transaction ("/add" route)
    def test_add_transaction(self): 
        data = {'date': '2023-06-03', 'amount': 300}
        response = self.client.post('/add', data=data)
        # ---- Practice 3 ----#
        # Expect the transactions list to have 3 items
    
    # Test deleting a transaction ("/delete/<transaction_id>" route)   
    def test_delete_transaction(self):
        response = self.client.get('/delete/1')
        self.assertEqual(len(transactions), 1)  # Expect the transactions list to have 1 item

    # Test editing an existing transaction ("/edit/<transaction_id>" route)
    def test_edit_transaction(self):
        data = {'date': '2023-06-01', 'amount': 150}
        response = self.client.post('/edit/1', data=data)
        # ---- Practice 4 ----#
        # Expect the amount of the first transaction to be updated
        
        
if __name__ == '__main__':
    unittest.main()
