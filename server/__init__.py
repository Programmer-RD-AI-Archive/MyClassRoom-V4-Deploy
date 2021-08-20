from flask import *
from flask_restful import *
from pymongo import *
import json



def get_link():
    with open(
        "./private/mongodb-client.json"
    ) as json_info:
        info = json.load(json_info)
    return info["MongoDB-Client-Url"]


# Configing the web application
app = Flask(__name__)
app.debug = True
app.secret_key = "--568963558fgdg85fbfd/8gf6bed8fgf6dbhde9rfg5sdf96eyhgr96f5hr9ehr--Ranuga D 2008--568963558fgdg85fbfd/8gf6bed8fgf6dbhde9rfg5sdf96eyhgr96f5hr9ehr--"
api = Api(app)
# COnfiging the databases
link = get_link()
try:
    cluster = MongoClient(link)
except:
    cluster = MongoClient(link, connect=False)
else:
    cluster = MongoClient(link, connect=True)
from server.routes import *
