from flask import Flask
from flask import render_template
from flask import request

app = Flask("Trainingsplan-Generator")


@app.route('/startseite')
@app.route('/startseite/<vorname>', methods=['GET', 'POST'])
def abfrage1_vorname():
    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        ausgabe1 = "Hello " + vorname + nachname + "!"
        return ausgabe1
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
