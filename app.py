from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

app.run(debug=True)