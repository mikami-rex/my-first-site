from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Marhaba b'k f Site dyali! 🚀</h1><p>Hada awwal site m'hosti b Python wa Render.</p>"

if __name__ == "__main__":
    app.run(debug=True)