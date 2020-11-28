from flask import Flask, redirect, g, request, jsonify 
from app import app
import psycopg2.pool

app.config['postgreSQL_pool'] = psycopg2.pool.SimpleConnectionPool(
    1,  # min number of connections
    10,  # max number of connections
    host='127.0.0.1',
    port='5432',
    database='pet_hotel'  # Database name - this changes per project
)


def get_db_conn():
    if 'db' not in g:
        g.db = app.config['postgreSQL_pool'].getconn()
        print('Got a connection')
    return g.db

# Close the database connection when done with a query
@app.route('/')
def index():
    return redirect('/index.html')

@app.teardown_appcontext
def close_db_conn(taco):
    db = g.pop('db', None)
    if db is not None:
        app.config['postgreSQL_pool'].putconn(db)
        print('Closing connection')


@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'GET':
        return  getAllPets()
    elif request.method == 'POST':
        return addPet(request.form.to_dict())


def addPet(pet):
    pet = request.get_json()
    print('Checking in a new pet to the hotel!', pet)
    cursor = None
    response = None

    try:
        connection = get_db_conn()
        cursor = connection.cursor()
        print(pet)
        sql = "INSERT INTO pets (name, breed, color, notes) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (pet['name'], pet['breed'], pet['color'], pet['notes']))

        connection.commit()
        response = {"msg": "Added your pet successfully to the hotel"}, 201
    except psycopg2.Error as e:
        print("Error when checking in your pet", e)
        response = {"msg": "Error checking in your pet, sorry!"}, 500
    else:
        if cursor:
            cursor.close()

    return response


@app.route('/pets/<id>', methods=['DELETE'])
def deletePet(id):
    try:
        print('Deleting pet at id#', id)
        connection = get_db_conn()
        cursor = connection.cursor()
        sql =  """DELETE FROM pets WHERE id = %s;"""
        cursor.execute(sql, (id))
        connection.commit()
        response = {"msg": "Deleted your pet successfully from the hotel"}, 201
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to DELETE in db: ", error)
    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            # connection.close()
            print("PostgreSQL cursor is closed")
    return response

def getAllPets():
    # get a connection to our database, use that to get a cursor
    conn = get_db_conn()
    cursor = conn.cursor()

    # run our select query
    cursor.execute('SELECT * FROM pets ORDER BY id DESC;')
    
    # Get our results
    result = cursor.fetchall()
    print(result)
    # IMPORTANT - CLOSE cursor
    cursor.close()

    # send back results
    return {'pets':result}

@app.route('/pets/<int:id>', methods=['PUT'])
def putPet(id):
    try:
        print(id)
        connection = get_db_conn()
        cursor = connection.cursor()
        postgres_insert_query= 'UPDATE pets SET checked_in = NOT checked_in WHERE id = %s '
        record_to_insert = [id]
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        return 'received PUT'
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to PUT to db", error)
            return 'failed'
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            # connection.close()
            print("PostgreSQL cursor is closed")
            return 'finally'

