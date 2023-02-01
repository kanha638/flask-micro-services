import os
import psycopg2
import json
from flask import Flask,jsonify,request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='test_flask',
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))
    return conn

@app.route('/')
def hello():
    conn = get_db_connection()
    curr = conn.cursor()
    curr.execute('select * from books;')
    books = curr.fetchall()
    val1 = []
    for book in books:
        # tmp1 = json.dumps(book)
        tmp = {
            "id":book[0],
            "title":book[1],
            "price":book[3],
            "desc":book[4],
            "date":book[5]
        }
        val1.append(tmp)
        
    curr.close()
    conn.close()
    val = jsonify(val1)
    return val

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)