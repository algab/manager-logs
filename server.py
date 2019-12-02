import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from app.log import log
from app.schedule import Schedule

app = Flask("manager-logs")

CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(log)
Schedule().start()

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT")),use_reloader=True,load_dotenv=True)