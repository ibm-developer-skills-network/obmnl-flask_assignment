# Import necessary libraries from Flask
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask application
app = Flask("Transaction_Management")

# Sample data representing transactions
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: Route to list all transactions
@app.route("/")
def get_transactions():
    # Render the transactions list template and pass the transactions data
    return render_template("transactions.html", transactions=transactions)

# Create operation: Route to display and process add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        # Extract form data to create a new transaction object
        transaction = {
            'id': len(transactions) + 1,         # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],        # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }

        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))

    # Render the form template to display the add transaction form if the request method is GET
    return render_template("form.html")

# Update operation: Route to display and process edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break                            # Exit the loop once the transaction is found and updated

        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))

    # Find the transaction with the matching ID and render the edit form if the request method is GET
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

# Delete operation: Route to delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break                            # Exit the loop once the transaction is found and removed

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

@app.route("/show_balance")
def show_balance():
    total_balance = 0
    for transaction in transactions:
        total_balance += transaction['amount']
    return f'''<h2>Total Balance: {total_balance}</h2>'''


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
