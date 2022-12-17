from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template('base.html')


@app.post("/predict")
def predict():
    # text = request.get_json().get("message")
    # text = request.get_json
    text = request.get_json().get("message")
    # print(text)
    # check if text id valid
    response = get_response(text)
    message = {"answer" : response}
    # print(message)
    # t = jsonify(message)
    # print(t)
    return jsonify(message)


# print(predict())

if __name__ == "__main__":
    app.run(debug=True)
