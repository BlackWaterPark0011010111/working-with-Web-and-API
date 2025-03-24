from flask import Flask, render_template, request
from dotenv import load_dotenv 
from pathlib import Path 
import os 
import psycopg2 

path = Path(__file__).parent
load_dotenv(f'{path}/.venv/.env')



app = Flask(__name__)
# connect to postgresql
db_params={
    'host': 'localhost', 
    'database':'postgres', 
    'user': 'postgres', 
    'port': '5432', 
    'password': os.getenv('PASSWORD')  
}


conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# displaying the version, proof of conn


    
@app.route('/', methods=['GET'])
def home(): 
    
    sql_display_customers='SELECT * FROM customers;'
    cursor.execute(sql_display_customers)
    records= cursor.fetchall()
    
    return render_template('index.html', records=records)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name= request.form['name']
    email= request.form.get('email')
    print(name, email)
    
    return f'{name} {email}'
    
if __name__== '__main__': 
    app.run(host='0.0.0.0', port=300, debug=True)