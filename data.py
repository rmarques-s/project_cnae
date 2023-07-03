import pandas as pd
from flask import Flask, render_template, jsonify
import psycopg2 #pip install psycopg2
import psycopg2.extras
import numpy as np

app = Flask(__name__)
app.secret_key = 'rmmarques-code_cnae'

DB_HOST = "localhost"
DB_NAME = "cnae_rn"
DB_USER = "postgres"
DB_PASS = "postgres"

connect = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# Método GET
@app.route('/')
def Index():
    cur = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM public.template_estabelecimentos"
    cur.execute(s) #Execute the SQL
    list_establishments = cur.fetchall()
    return render_template('main.html', list_establishments=list_establishments)

@app.route('/municipios', methods=['GET'])
def get_neighborhood():
    cur = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM public.template_estabelecimentos.municipio"
    cur.execute(s)
    list_CNAE = cur.fetchall()
    return render_template('main.html', list_CNAE=list_CNAE)

def data_creation(data, percent, class_labels):
    for index, item in enumerate(percent):
        data_instance = {}
        data_instance['id'] = class_labels[index]
        data_instance['value'] = item
        data.append(data_instance)

@app.route('/get_barchart_data')
def get_barchart_data():
    tenure_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
    neighborhoods = pd.cut(get_neighborhood.tenure, range(0, 81, 10), labels=tenure_labels)

    barchart_data = []
    data_creation(barchart_data,neighborhoods, tenure_labels, "All")
    return jsonify(barchart_data)

if __name__ == "__main__":
    app.run(debug=True)
