from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/trainingsplan')
def hello():
    return render_template('index.html', name="Pascal")


@app.route('/sitename')
def testlink():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)