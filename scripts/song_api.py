from flask import Flask, jsonify, request,make_response
from functools import wraps
import MySQLdb
import pandas as pd
import logging

app = Flask(__name__)

#configure authorization
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'ferrytm' and auth.password == 'henshin':
            return f(*args, **kwargs)
        
        return make_response ('Login failed', 401, {'WWW-Authenticate': 'Basic realm="Login Required"' })
    
    return decorated

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Define MySQL connection parameters
mysql_host = 'mysql-service'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'henshin'
mysql_db = 'mysql'

# Define API Endpoints
@app.route('/')
def index():
    return '<h1>Welcome to the Music Recommendation API. Go to /topsong to get top 10 most popular songs in Spotify. </h1>'
   

@app.route('/topsong', methods=['GET'])
@auth_required
def get_topsong():
    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db)
        cursor = conn.cursor()
        
        # Query MySQL database to get song topsong
        query = "select artist_names, track_name, source, weeks_on_chart, streams from spotify_top_songs order by weeks_on_chart desc limit 50;"  
        cursor.execute(query)
        data = cursor.fetchall()

        # Convert data to pandas DataFrame
        df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])

        # Convert DataFrame to dictionary format
        topsong = df.to_dict(orient='records')

        # Close MySQL connection
        cursor.close()
        conn.close()

        return jsonify(topsong)
    except Exception as e:
        logging.error('Error retrieving topsong from MySQL database: %s', e)
        return jsonify({'error': 'An error occurred while retrieving topsong'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
