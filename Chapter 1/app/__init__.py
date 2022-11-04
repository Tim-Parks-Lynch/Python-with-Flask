from flask import Flask

app = Flask(__name__)

# Takes care of circular imports, apparently common in flask
from app import routes 
