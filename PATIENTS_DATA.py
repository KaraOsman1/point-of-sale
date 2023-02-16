from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
#import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'hospital'

mysql = MySQL(app)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients(name, age, gender, address, phone) VALUES(%s, %s, %s, %s, %s)", (name, age, gender, address, phone))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
