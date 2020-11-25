from flask import request, redirect 
from app import app 

@app.route('/')
def index():
  return redirect('/index.html')


@app.route('/pets', methods=['GET', 'POST'])
def pets(): 
    return 'Pets' 



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


@app.route('/pets/<name> methods=['DELETE'])
def deletePet(id):
    try:
        print(id)
        connection = mainConnection
        cursor = connection.cursor()
        postgres_insert_query=""" DELETE FROM "pets" WHERE "id" = %s """
        record_to_insert = [id]
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        return 'PUT'
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to DELETE in db: ", error)
            return 'failed'
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            # connection.close()
            print("PostgreSQL cursor is closed")
            return 'finally'

