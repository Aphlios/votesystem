from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import datetime
import logging

app = Flask(__name__)

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='database', dbname='votingdb', user='postgres', password='123456')
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form['option']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE votes SET vote_number = vote_number + 1, last_vote = %s WHERE option_name = %s",
                (datetime.datetime.now(), option))
    conn.commit()
    cur.close()
    conn.close()
    # 记录日志
    logger.info(f'Button clicked: {option}')
    # 重定向到投票成功页面
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)