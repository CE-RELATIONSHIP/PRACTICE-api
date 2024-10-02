from flask import Flask, jsonify
from werkzeug import exceptions

app = Flask(__name__)
ctx = app.app_context()

class HttpMethod():
    GET = "GET"

@app.route('/is_prime/<num>', methods=[HttpMethod.GET])
def is_prime(num):
    # defined for natural numbers greater than 1 
    # with exactly two distinct positive divisors
    try:
        num = float(num)
        print('test push')
        
        if (not num.is_integer() or num <= 1):
            return jsonify(False)

        for i in range(2, int(num**0.5) + 1):
            if (num % i == 0):
                return jsonify(False)

    except Exception as err:
        raise exceptions.BadRequest(err)

    return jsonify(True)

if __name__ == '__main__':
    app.run(debug=True)