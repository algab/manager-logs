# Manager Logs

Development

````
pip install -r requirements.txt
python server.py
````

Production

````
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:4000 server:app
````