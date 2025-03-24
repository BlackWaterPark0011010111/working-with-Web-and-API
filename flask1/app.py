from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask!"


@app.route("/about")
def about():
    return "Hello from About page"


@app.route("/users")
def users():
    return "A list of users"


@app.route("/users/<user>")
def show_user(user):
    return f"User details for {user}."


@app.route("/products/<int:id>")
def show_product(id):
    return f"Product detail for ID: {id}."


if __name__ == "__main__":
    app.run(debug=True)