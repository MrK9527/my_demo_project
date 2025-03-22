from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, WellCome to OpenShift test!!!"

if __name__ == "__main__":
    app.run(debug=True)
