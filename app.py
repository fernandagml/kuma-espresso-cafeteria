from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/como-chegar')
def como_chegar():
    return render_template('como_chegar.html')


app.run(debug=True)