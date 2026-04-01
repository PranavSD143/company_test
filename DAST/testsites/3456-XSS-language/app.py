# Flask application demonstrating SQL injection vulnerability
# Type: application
# Language: python

from flask import Flask, request, render_template
import pymysql
import os

app = Flask(__name__)

# Database connection configuration using environment variables
def get_db_connection():
    try:
        conn = pymysql.connect(
            host=os.environ.get('DATABASE_HOST', 'db'),
            user=os.environ.get('DATABASE_USER', 'root'),
            password=os.environ.get('DATABASE_PASSWORD', 'password'),
            database=os.environ.get('DATABASE_NAME', 'vulnerable_db'),
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        query = f"SELECT * FROM users WHERE username = '{username}'"
        
        conn = get_db_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return render_template('index.html', results=results)
            except Exception as e:
                return render_template('index.html', error=str(e))
            finally:
                conn.close()
        else:
            return render_template('index.html', error="Database connection failed")
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)