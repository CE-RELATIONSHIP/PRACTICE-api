from flask import Flask, jsonify
from werkzeug import exceptions

app = Flask(__name__)
ctx = app.app_context()

class HttpMethod():
    GET = "GET"

@app.route('/next5/<num>', methods=[HttpMethod.GET])
def next5(num):
    # defined for natural numbers greater than 1 
    # with exactly two distinct positive divisors
    try:
        num = float(num)
        num += 5

    except Exception as err:
        raise exceptions.BadRequest(err)

    return jsonify(num)

if __name__ == '__main__':
    app.run(debug=True)