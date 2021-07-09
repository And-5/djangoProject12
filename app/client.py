import requests
from app.models import Person

def client():
    requests.get(
        'http://127.0.0.1:8000/person?id=2')