from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1 style='color:red;text-align:center;margin-top:100px;font-size:50px'>Hello World! My Free Website Works!</h1>"

if __name__ == '__main__':
    app.run()
