# Import libraries

from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality

app = Flask(__name__)

# Sample data

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation

@app.route("/", methods = ["GET"])
def get_transactions():
    return render_template("transactions.html", transactions = transactions)


# Create operation

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")
    
    if request.method == "POST":

        transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        
        transactions.append(transaction)

        return redirect(url_for("get_transactions"))


# Update operation

@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":

        for transaction in transactions:

            if transaction["id"] == transaction_id:

                return render_template("edit.html", transaction = transaction)

        return {"message" : "Transaction number not found"}, 404 #implemented error handling if the transaction ID is not found.
            
    if request.method == "POST":
        date = request.form["date"]
        amount = float(request.form["amount"])

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = date
                transaction["amount"] = amount
                break 
        return redirect(url_for("get_transactions"))




# Delete operation

@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):

    for transaction in transactions: # go trough the transactions and check if the ID's match, if yes, delete the transaction form the list.
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("get_transactions")) #redirect the user to the transactions page.
        

# Add a search feature 

@app.route("/search", methods = ["GET", "POST"])
def search_transactions():
    if request.method == "POST":                       # get the minimum and maximum amount.
        min_amount = request.form.get("min_amount")
        max_amount = request.form.get("max_amount")

        min_amount = float(min_amount)                # convert the variables into floats.
        max_amount = float(max_amount)

        filtered_transactions = [                    # use a list comprehension to filter out the min and max amount criteria.
        
            transaction for transaction in transactions if min_amount <= transaction["amount"] <= max_amount

            ]

    
        return render_template("transactions.html", transactions = filtered_transactions ) #render the transactions.html, showing the filtered transactions.

    return render_template("search.html") # if request is GET, render the search.html file so the user can enter the amounts to filter.


@app.route("/balance")
def total_balance():

    amount_list = [] # made a empty list to store all of the transaction amounts

    for transaction in transactions:               #itereting trough the transactions and adding the amoun values to the list
        amount_list.append(transaction["amount"])

    total = sum(amount_list)      # summing the list
    
    return f"Total balance : {total}"  # returning a simple display text (may improve it later)



# Run the Flask app
    
if __name__ == "__main__":
    app.run(debug=True)