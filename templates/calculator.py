from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("calculator_UI.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    a = int(request.form["a"])
    b = int(request.form["b"])
    operation = request.form["operation"]

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":
        result = a / b if b != 0 else "Error: Division by zero"

    else:
        result = "Invalid operation"

    return render_template("calculator_UI.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)