from flask import Flask, redirect, request, jsonify, render_template, url_for

app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100, 'account': 'Checking'},
    {'id': 2, 'date': '2023-06-02', 'amount': 200, 'account': 'Savings'},
    {'id': 3, 'date': '2023-06-03', 'amount': 300, 'account': 'Investment'}
]

# Read operation: List all transactions
# --- Fill the missing code here --- # 
    
# Create operation: Display add transaction form
# --- Fill the missing code here --- #   
        date = request.form.get("date")
        amount = float(request.form.get("amount"))
        account = request.form.get("account")

        # Generate a unique ID for the new transaction
        new_id = len(transactions) + 1

        # Create the new transaction object
        new_transaction = {
            'id': new_id,
            'date': date,
            'amount': amount,
            'account': account
        }

        # Add the new transaction to the list
        transactions.append(new_transaction)

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    return render_template("form.html")



# Update operation: Display edit transaction form
# --- Fill the missing code here --- # 
    if request.method == 'POST':
        # --- Fill the missing code here --- # 

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                transaction['account'] = account
                break

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)
    # Transaction not found
    return "Transaction not found"


# Delete operation: Delete a transaction
# --- Fill the missing code here --- # 
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # --- Fill the missing code here --- # 
            break

    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
    
    # Run the tests
    runner = unittest.TextTestRunner()
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(FlaskAppTestCase)
    runner.run(tests)
