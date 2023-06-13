import pandas as pd
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/cnae_rn'

db = SQLAlchemy(app)
# Método GET
@app.route("/establishments", methods=['GET'])
def get_establishments():
    establishments = db.query.all()

    return Response(establishments)


#dataframe = pd.read_csv('/home/rafaelamarques/project_cnae/estabelecimentos_RN.csv')

#print(dataframe.head())  # Exibe as primeiras linhas do DataFrame
