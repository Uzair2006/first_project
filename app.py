
from turtle import home
from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)
db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] =db ['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] =db ['mysql_password']
app.config['MYSQL_DB'] =db ['mysql_db']
mysql=MySQL(app)

@app.route("/" ,methods=['POST','GET'])
def index():
    if request.method == 'POST':
        
        userdetails = request.form
        email = userdetails.get('email')
        password = userdetails.get('password')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(email,password) VALUES(%s,%s)",(email,password))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html')
        


    return render_template('index.html') 

@app.route("/user")
def user():
    cur = mysql.connection.cursor()
    resultvalue =cur.execute("SELECT * FROM user")
    if resultvalue > 0:
        userdetails = cur.fetchall()
        return render_template('userlogs.html',userdetails=userdetails) 




if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
