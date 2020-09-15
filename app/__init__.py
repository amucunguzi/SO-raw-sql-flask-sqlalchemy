import os
from flask import Flask
from .db import db

from .api import api

# if os.getenv('FLASK_ENV') != 'production':
#     load_dotenv(verbose=True)

app = Flask(__name__)
# host = localhost for local db
database_uri = 'mysql+pymysql://<user>:<password>@<host>/<database_name>?charset=utf8mb4'
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
app.register_blueprint(api, urlprefix="/")
# cors = CORS(app, supports_credentials=True)
app.secret_key = '079bc80c-cbd6-4fc5-b1aa-8fe01fde50dc'