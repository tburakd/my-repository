from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World!</h1"

@app.route("/second")
def second():
    return "This is the second page"

@app.route("/third/burak")
def third():
    return "This is the subpath of the third path"

@app.route("/fourt/<string:id>")
def fourt(id):
    return f'Id of this page is {id}'

if __name__=="__main__":                    #if this is my main app then run it on debug mode(True)
    app.run(debug=True)