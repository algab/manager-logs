from flask import Flask
from flask_cors import CORS
from manager.log import log
from manager.manager import Manager

app = Flask("manager-logs")

CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(log)

if __name__ == '__main__':
    Manager().start()
    app.run(port=5000,debug=True,use_reloader=True)