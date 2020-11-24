from flask import Flask, request, redirect 
app = Flask(__name__, static_folder='public', static_url_path='')

from app import routes

