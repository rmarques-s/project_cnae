import pandas as pd
from flask import Flask, render_template
import psycopg2 #pip install psycopg2
import psycopg2.extras

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

@app.route('/')
def getCNAE():
    cur = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM public.template_estabelecimentos.descricao"
    cur.execute(s)
    list_CNAE = cur.fetchall()
    return render_template('main.html', list_CNAE=list_CNAE)

if __name__ == "__main__":
    app.run(debug=True)

#dataframe = pd.read_csv('/home/rafaelamarques/project_cnae/estabelecimentos_RN.csv')

#print(dataframe.head())  # Exibe as primeiras linhas do DataFrame
