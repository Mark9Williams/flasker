from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    first_name = "William"
    stuff = "This is Bold"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushroom", 41]
    return render_template("index.html",
     first_name=first_name,
     stuff=stuff,
     favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#Create Custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500