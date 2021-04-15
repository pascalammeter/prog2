from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/hello')
def hello():
    return render_template('hello.html', name="Pascal")

@app.route('/hello/<name>')
def begruessung(name=False):
    if name:
         return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"

@app.route('/sitename')
def test():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
