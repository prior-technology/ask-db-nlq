source activate ask-db-nlq-cpu
export FLASK_APP=api.py
#gunicorn -w 1 -t 120 -b 0.0.0.0:4000 --log-level DEBUG api:app
flask run -h 0.0.0.0 -p 4000
