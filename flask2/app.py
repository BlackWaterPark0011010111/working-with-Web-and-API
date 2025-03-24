from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/flask")
def flask_info():
    data = "Flask library contents will be displayed soon..."
    cars = ["Mercedes", "BMW", "Audi", "Porsche"]
    dict = {"1": "Gold", "2": "Silver", "3": "Bronze"}
    info = dir(Flask)
    return render_template(
        "flask.html", data=data, cars=cars, medals=dict["2"], flask=info
    )


if __name__ == "__main__":
    app.run(debug=True)