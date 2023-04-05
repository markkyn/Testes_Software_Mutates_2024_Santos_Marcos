import re
from flask import Flask, jsonify, render_template, request
from selfparser import parseEqu

app = Flask(__name__)


@app.route('/operation', methods=["POST"])
def calculate():
    string1 = request.form['string1']
    string1 = string1.replace("\"", "")
    result = parseEqu(string1)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('application.html')


if __name__ == '__main__':
    app.run(debug=False)
