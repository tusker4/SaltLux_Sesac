from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return 'hello flask 2223333333T4444TTTTTTTTTT'

if __name__ == '__main__':
    app.run(debug=True)

