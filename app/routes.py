from flask import request, redirect 
from app import app 

@app.route('/')
def index():
  return redirect('/index.html')


@app.route('/pets', methods=['GET', 'POST'])
def pets(): 
    return 'Pets' 




