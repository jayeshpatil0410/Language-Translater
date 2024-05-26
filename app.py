from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # MySQL host
app.config['MYSQL_USER'] = 'root'   # MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # MySQL password
app.config['MYSQL_DB'] = 'translater'  # MySQL database name
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        data = request.form['data']
        print(data)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM etom")
        users = cur.fetchall()
        print(type(users))
        for i in users:
            if i[0]==data:
                print(i[1])
        cur.close()
        print(users)
    else:
        return render_template('index.html')
    return render_template('index.html', users=users, data = data)

if __name__ == '__main__':
    app.run(debug=True)