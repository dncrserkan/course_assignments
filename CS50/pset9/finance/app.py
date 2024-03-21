import sqlite3
import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from myhelpers import password_validity_check, username_validity_check


app = Flask(__name__)

app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get("user_id")

    with sqlite3.connect("finance.db") as conn:
        cur = conn.cursor()
        #items will be a tuple with lists ["symbol", total_shares]
        items = cur.execute("""SELECT symbol, SUM(shares) FROM purchases 
                            WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) != 0""", 
                            (user_id, )).fetchall()

    # Look for current prices and create dictionary
    rows = []
    total = 0   # General total
    for item in items:
        row = {}
        current_price = lookup(item[0])["price"]         #item[0] is "symbol"
        # lookup fuction returns a dict for "symbol, price, name" and type of price is float
        total_item = item[1] * current_price    # item[1] is total_shares
        row["symbol"] = item[0]
        row["name"] = item[0]
        row["shares"] = item[1]
        row["price"] = current_price
        row["total"] = total_item
        rows.append(row)
        total += total_item
    
    cash = cur.execute("SELECT cash FROM users WHERE id = ?", (user_id,)).fetchone()[0]
    total += cash
    return render_template("index.html", rows=rows, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        try:
            # Check if shares is a number or whole number and wrost is not number
            if shares == "" or (float(shares) % 1 != 0):
                return apology("Shares must be filled with whole number")

            else:
                shares = int(shares)
                # We are sure about shares is int
                if shares < 1:
                    # share must be positive
                    return apology("Shares must be positive number")
                else:
                    pass        # ALL OKEY for shares
        except ValueError:
            # Worst case, shares is not number and there is a ValueError 
            return apology("Shares must be whole number")

        if symbol == "":
            return apology("They can't be empty")
        
        values = lookup(symbol)
        # lookup function returns a dict for "symbol, price, name" and type of price is float orthers are string
        if values is None:
            return apology("We don't sell that")


        with sqlite3.connect("finance.db") as conn:
            cur = conn.cursor()
            user_id = session.get("user_id")
            
            # Get Cash
            cash = cur.execute("SELECT cash FROM users WHERE id = ?", (user_id,)).fetchone()[0]

            # Values for database
            symbol = values["symbol"]
            price = values["price"]
            type = "Buy"
            timestamp = datetime.datetime.now()
            
            if price * shares <= cash:
                # TRANSACTION IS AVAILABLE
                cash -= ( price * shares )
                cur.execute("UPDATE users SET cash = ? WHERE id = ?", (cash, user_id))
                cur.execute("""INSERT INTO purchases(user_id, symbol, shares, price, type, timestamp) 
                            VALUES (?, ?, ?, ?, ?, ?)""", 
                            (user_id, symbol, shares, price, type, timestamp))
                conn.commit()
                cur.close()
                return redirect("/")
            else:
                cur.close()
                return apology("You don't have enough cash")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    with sqlite3.connect("finance.db") as conn:
        cur = conn.cursor()
        items = cur.execute("""SELECT symbol, shares, price, type, timestamp 
                            FROM purchases WHERE user_id = ?""", 
                            (user_id, )).fetchall()
        cur.close()
        return render_template("history.html", items=items)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        temp_username = request.form.get("username")
        temp_password = request.form.get("password")

        if not temp_username:
            return apology("must provide username")
        if not temp_password:
            return apology("must provide password")

        # Query database for username
        with sqlite3.connect("finance.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (temp_username,))
            rows = cur.fetchall()
            cur.close()
        
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0][2], temp_password): #2->"hash"
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0][0]
        session["username"] = rows[0][1]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()     # Forget any user_id
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if symbol == "":
            return render_template("quote.html")
        values = lookup(symbol)
        if values is None:
            return apology(f"No such thing as {symbol}")
        return render_template("quoted.html", values=values)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        # Check password match and validity
        if password != password_confirm or not password_validity_check(password) :
            # If passwords do not match or has invalid character
            return apology("Check Your Passwords")

        # Check if username is empty or ha invalid character
        if username == "" or not username_validity_check(username):
            return apology("Check your username")
        
        with sqlite3.connect("finance.db") as conn:
            cur = conn.cursor()
            # Check user name avaialability (is it alreay exist)
            existing_username = cur.execute("SELECT username FROM users WHERE username = ?", (username, )).fetchone()
            if existing_username:
                cur.close()
                return apology("Username in use")
        
            # Conditions met, add database
            else:
                hash_password = generate_password_hash(password, "scrypt", len(password))
                cur.execute("INSERT INTO users(username, hash) VALUES (?, ?)", (username, hash_password))
                conn.commit()
                cur.close()
                return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        with sqlite3.connect("finance.db") as conn:
            # Get own symbols and create list of symbols
            user_id = session.get("user_id")
            cur = conn.cursor()

            temp = cur.execute("SELECT symbol FROM purchases WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) != 0", (user_id, )).fetchall()
            owns = []
            for item in temp:
                owns.append(item[0])

            cur.close()
            return render_template("sell.html", owns=owns)
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        try:
            # Check if shares is a number or whole number and wrost is not number
            if shares == "" or (float(shares) % 1 != 0):
                return apology("Shares must be filled with whole number")

            else:
                shares = int(shares)
                # We are sure about shares is int
                if shares < 1:
                    # share must be positive
                    return apology("Shares must be positive number")
                else:
                    pass        # ALL OKEY for shares BUT still don't know user has that much

        except ValueError:
            # Worst case, shares is not number and there is a ValueError 
            return apology("Shares must be whole number")


        if symbol == "" or symbol is None:
            return apology("You wanna sell nothing")
        
        values = lookup(symbol)
        # lookup function returns a dict for "symbol, price, name" and type of price is float orthers are string
        if values is None:
            return apology("We don't buy that")


        with sqlite3.connect("finance.db") as conn:
            user_id = session.get("user_id")
            # Get, if user realy has that currency and its shares value
            cur = conn.cursor()
            item = cur.execute("SELECT symbol, SUM(shares) FROM purchases WHERE user_id = ? AND symbol = ? GROUP BY symbol", (user_id, symbol)).fetchone()
            
            # Check for user has it and has that much
            if symbol != item[0]:
                # In case html source hack (MAYBE THIS IS NOT NECESSARY)
                return apology("Somehow you don't have that")

            elif shares > item[1]:
                # Be sure user has that much shares
                return apology("You don't have that much")


            # ALL PASSED NOW WE CAN MAKE TRANSACTION
            query = "INSERT INTO purchases(user_id, symbol, shares, price, type, timestamp) VALUES (?, ?, ?, ?, ?, ?)"
            # Values for database
            temp = lookup(symbol)
            price = temp["price"]
            type = "Sell"
            timestamp = datetime.datetime.now()
 
            cur.execute(query, (user_id, symbol, -shares, price, type, timestamp))
            conn.commit()

            cash = cur.execute("SELECT cash FROM users WHERE id = ?", (user_id, )).fetchone()[0]
            cash += ( price * shares)
            cur.execute("UPDATE users SET cash = ? WHERE id = ?", (cash, user_id))
            conn.commit()
            cur.close()
            return redirect("/")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    """Register user"""
    if request.method == "GET":
        return render_template("settings.html")
    
    else:
        user_id = session.get("user_id")
        # Take inputs
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        new_password_confirm = request.form.get("new_password_confirm")


        # Query database for username
        with sqlite3.connect("finance.db") as conn:
            cur = conn.cursor()
            real = cur.execute("SELECT hash FROM users WHERE id = ?", (user_id, )).fetchone()[0]
            cur.close()
        
        # Ensure current_password is correct
        if check_password_hash(real, current_password):

            # If passwords do not match or has invalid character
            if new_password != new_password_confirm or not password_validity_check(new_password) :
                return apology("Check Your Passwords")

            
            with sqlite3.connect("finance.db") as conn:
                cur = conn.cursor()
                # Conditions met
                hash_password = generate_password_hash(new_password, "scrypt", len(new_password))
                cur.execute("UPDATE users SET hash = ? WHERE id = ?", (hash_password, user_id))
                conn.commit()
                cur.close()
                return redirect("/")
        else:
            return apology("It seems like, you don't know your own password")
