from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello Wordl!"

@app.route("/about")
def about():
    return "pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)