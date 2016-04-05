from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "/kimlik/17291716060"

@app.route("/kimlik/<int:kimlik_no>")
def query_kimlik(kimlik_no):
    conn = conn = psycopg2.connect("dbname='' user='' password='' host=''")
    stm = "select * from citizen where national_identifier=%(kimlik)s"

    cur = conn.cursor()
    cur.execute(stm, {'kimlik': str(kimlik_no)})
    rows = cur.fetchall()
    if len(rows) == 0:
        conn.close()
        return str(kimlik_no) + " nolu vatandaş, güvendesin :)"
    else:
        conn.close()
        return "Sayın " + str(rows[0][2]) + " " + str(rows[0][3]) + " bilgileriniz sızmış :("


if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
