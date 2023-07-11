import unittest
from flask_testing import TestCase

# Import the Flask app
from app import app, transactions


class FlaskAppTestCase(TestCase):
    def create_app(self):
        # Set the Flask app to be tested
        app.config['TESTING'] = True
        return app

    def setUp(self):
        print("running before each test")
        # Add sample data for testing
        transactions.append({'id': 1, 'date': '2023-06-01', 'amount': 100, 'account': 'Checking'})
        transactions.append({'id': 2, 'date': '2023-06-02', 'amount': 200, 'account': 'Savings'})

    def tearDown(self):
        print("running after each test")
        # Clear the sample data after each test
        transactions.clear()

    def test_get_transaction(self):
        print("test_get_transaction")
        # --- Fill the missing code here --- # 

    def test_add_transaction_form(self):
        print("test_add_transaction_form")
        # --- Fill the missing code here --- # 

    def test_add_transaction(self):
        print("test_add_transaction")
        data = {'date': '2023-06-03', 'amount': 300, 'account': 'Investment'}
        response = self.client.post('/add', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200) # or self.assert200(response) or self.assertTrue(response.status_code==200)
        self.assertTemplateUsed('transactions.html') # to check that the correct template is used
        # --- Fill the missing code here --- # 

    def test_edit_transaction_form(self):
        print("test_edit_transaction_form")
        # --- Fill the missing code here --- # 
        self.assertEqual(response.status_code, 200) # or self.assert200(response) or self.assertTrue(response.status_code==200)
        self.assertTemplateUsed('edit.html') # to check that the correct template is used

    def test_delete_transaction(self):
        print("test_delete_transaction")
        response = self.client.get('/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200) # or self.assert200(response) or self.assertTrue(response.status_code==200)
        self.assertTemplateUsed('transactions.html') # to check that the correct template is used
        # --- Fill the missing code here --- # 


if __name__ == '__main__':
    unittest.main()
