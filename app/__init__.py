"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaapnrhp8u791gvqorg-a.oregon-postgres.render.com",
        database="todo_8dtn",
        user="root",
        password="sD1ARyd8yLueHhz50l1ez22qBJhTa3BP")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

