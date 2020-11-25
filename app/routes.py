from flask import Flask, redirect, g, request 
from app import app
import psycopg2
import psycopg2.pool

@app.route('/')
def index():
  return redirect('/index.html')


@app.route('/pets', methods=['GET', 'POST'])
def pets(): 
    return 'Pets' 

app.config['postgreSQL_pool'] = psycopg2.pool.SimpleConnectionPool(
    1, #min number of connections 
    10, #max number of connections 
    host = '127.0.0.1', 
    port = '5432', 
    database = 'pet_hotel' # Database name - this changes per project 
)

def get_db_conn(): 
    if 'db' not in g: 
        g.db = app.config['postgreSQL_pool'].getconn()
        print('Got a connection')
    return g.db

# Close the database connection when done with a query 
@app.teardown_appcontext 
def close_db_conn(taco): 
    db = g.pop('db', None)
    if db is not None: 
        app.config['postgreSQL_pool'].putconn(db)
        print('Closing connection') 
