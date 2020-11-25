from flask import Flask, redirect, g, request 
from app import app

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

@app.route('/')
def index():
  return redirect('/index.html')
  
@app.route('/pets', methods=['GET', 'POST'])
def pets(): 
  if request.method == 'GET':
      #do stuff
      return #placeHolder 
  elif request.method == 'POST':
      return addPet(request.form)

def addPet(pet): 
  print('Checking in a new pet to the hotel!')
  curse = None
  response = None

  try:
    connection = get_db_conn() 
    cursor = connection.cursor()

    sql = "INSERT INTO pets (name, breed, color) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (pet['name'], pet['breed'], pet['color']))

    connection.commit() 
    response = {"msg": "Added your pet successfully to the hotel"}, 201 
  except psycopg2.Error as e: 
    print("Error when checking in your pet")
    response = {"msg": "Error checking in your pet, sorry!"}, 500 
  else: 
    if cursor: 
      cursor.close() 
  
  return response


