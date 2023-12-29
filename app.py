# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask('__name__')

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def read_trans():
    try:
        return render_template('transactions.html'), transactions
    except NameError:
        return {"message": "transactions is not defined"}, 500


# Create operation
@app.route('/create', methods=['POST'])
def create_trans():
    if request.method == 'POST':
        transaction = {'id':request.form.id, 'date': request.form.date, 'amount':request.form.amount}
        if transaction:
            transactions.append(transaction)
            return redirect(url_for('read_trans'))
        return {"message": "Please input valid data"}, 422


# Update operation
@app.route('/update', methods=['POST'])
def update_trans(id):
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == id:
                return render_template('edit.html'), transaction
        return redirect(url_for('read_trans'))
        
# Delete operation

# Update operation
@app.route('/delete', methods=['GET'])
def delete_trans(id):
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == id:
                transactions.remmove(transaction)
                return redirect(url_for('read_trans'))

# Run the Flask app
if