from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server".format(
                "sa",
                "<YourStrong!Passw0rd>",
                "127.0.0.1",
                "1433",
                'master')

db = SQLAlchemy(app)
