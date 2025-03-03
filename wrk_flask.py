# Flaskを使って掲示板アプリを作成する


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kenichiro!.My name is Flask!"

if __name__ == "__main__":
    app.run(debug=True)