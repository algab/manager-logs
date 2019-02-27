import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from collection import verify_collection
from app.log import log
from app.manager import Manager

load_dotenv('./config.env')

verify_collection()

app = Flask("manager-logs")

CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(log)

Manager().start()

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT")),use_reloader=True,load_dotenv=True)