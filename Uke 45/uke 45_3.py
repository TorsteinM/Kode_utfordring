from flask import Flask
webApp = Flask(__name__)
@webApp.route("/")
def landing(): return """<p>For å komme i gang med Flask, kan du følge <a href="https://flask.palletsprojects.com/en/latest/quickstart/#a-minimal-application" target="_blank">Minimal Application Guide</a> på Flask sine sider.</p>"""
webApp.run(debug=True)