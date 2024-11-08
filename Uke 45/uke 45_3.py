from flask import Flask
webApp = Flask(__name__)
@webApp.route("/")
def landing(): return "<h2>Hello World</h2>"
webApp.run(debug=True)