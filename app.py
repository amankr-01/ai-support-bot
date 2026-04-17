from flask import Flask, request, jsonify, render_template
from model import predict_intent, get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    
    tag = predict_intent(user_input)
    response = get_response(tag)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
