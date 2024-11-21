from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='database', dbname='votingdb', user='postgres', password='123456')
    return conn

@app.route('/')
def results():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT option_name, vote_number, last_vote FROM votes')
    votes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', votes=votes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)