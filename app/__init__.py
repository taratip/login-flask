from flask import Flask

# creating an app variable to be use throughout Flask application
app = Flask(__name__)

# routes have to be imported after app variable created, otherwise will break
from app import routes
