from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Credit Card Fraud Detection</h1>
    <p>Welcome to our fraud detection application!</p>
    <form action="/predict" method="post">
        <label>Transaction Amount:</label>
        <input type="number" name="amount" required>
        <button type="submit">Check Transaction</button>
    </form>
    """


@app.route("/predict", methods=["POST"])
def predict():

    amount = float(request.form.get("amount", 0))

    if amount > 10000:
        result = "Potentially Fraudulent"
    else:
        result = "Legitimate Transaction"

    return f"<h2>Prediction: {result}</h2>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)