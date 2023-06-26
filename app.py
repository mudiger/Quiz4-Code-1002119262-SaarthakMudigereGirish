from flask import request
from flask import Flask
from flask import render_template
import pyodbc
import os
import redis


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

driver = '{ODBC Driver 17 for SQL Server}'
server = 'sqlserver-1002119262-saarthakmudigeregirish.database.windows.net'
database = 'DataBase-1002119262-SaarthakMudigereGirish'
username = 'saarthakmudigeregirish'
password = 'Hello123'

# Establish the connection
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Create a cursor object
cursor = conn.cursor()

# Redis connection details
redis_host = 'Redis-1002119262-SaarthakMudigereGirish.redis.cache.windows.net'
redis_port = 6379
redis_password = 'l2CPHbqqk4w90H19Tmvm0n2ykWFLefcyBAzCaA1MX8M='

# Redis client
redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
#redis_client.flushall()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page1/", methods=['GET', 'POST'])
def page1():
    paira = []
    pairb = []
    if request.method == "POST":
        letter = request.form['letter']
        amount = request.form['amount']
        letter.split(",")
        amount.split(",")

        for i in letter:
            if i!=",":
                paira.append(i)
        for i in amount:
            if i != ",":
                pairb.append(i)
    return render_template("1)Page.html", paira=paira, pairb=pairb)


@app.route("/page2/", methods=['GET', 'POST'])
def page2():
    paira = []
    pairb = []
    if request.method == "POST":
        letter = request.form['letter']
        amount = request.form['amount']
        letter.split(",")
        amount.split(",")

        for i in range(30):
            if i!=",":
                paira.append(i)
        print(paira)
        for i in amount:
            if i != ",":
                pairb.append(i)
    return render_template("2)Page.html", paira=paira, pairb=pairb)


@app.route("/page3/", methods=['GET', 'POST'])
def page3():
    paira = []
    pairb = []
    z = []
    if request.method == "POST":
        letter = request.form['letter']
        amount = request.form['amount']
        b = request.form['z']

        letter.split(",")
        amount.split(",")
        b.split(",")
        for i in letter:
            if i!=",":
                paira.append(i)
        for i in amount:
            if i != ",":
                pairb.append(i)
        for i in b:
            if i != ",":
                z.append(i)
    return render_template("3)Page.html", paira=paira, pairb=pairb, z=z)


if __name__ == "__main__":
    app.run(debug=True)