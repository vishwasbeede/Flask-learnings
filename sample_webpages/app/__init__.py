from flask import Flask


apps = Flask(__name__)

from app import views
from app import admin_views
