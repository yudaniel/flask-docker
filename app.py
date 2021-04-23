from flask import Flask
import uuid

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World"

@app.route('/random')
def token_generator():
    random_token = uuid.uuid4().hex[:6]
    return ("Random Generated Token from Flask Server is: {}".format(random_token))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9000')