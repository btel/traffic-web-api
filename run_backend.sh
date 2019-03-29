export FLASK_APP=traffic_back
export FLASK_ENV=development
export DATABASE=myDatabase
export DBUSER=bartosz

flask init-db
flask run -p 8080
