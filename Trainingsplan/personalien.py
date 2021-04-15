from flask import Flask
from flask import render_template
from flask import request

app = Flask("Trainingsplan-Generator")

@app.route('/trainingsplan', methods=['GET', 'POST'])
def abfrage2_personalien():
    if request.method == 'POST':
        groesse = request.form['groesse']
        gewicht = request.form['gewicht']
        ausgabe2 = "Hello " + groesse + gewicht + "!"
        return ausgabe2
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)