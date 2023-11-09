from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL 

app1 = Flask(__name__)
mysql = MySQL(app1)


app1.config['MYSQL_HOST']='localhost'
app1.config['MYSQL_USER']='root'
app1.config['MYSQL_PASSWORD'] = "Nasrullah123%"
app1.config['MYSQL_DB']= 'mydb'


@app1.route("/" ,methods=["POST"])
def login():
    if request.method=="POST":
        email = request.json['Email']
        password = request.json['Password']

        cur = mysql.connection.cursor()


        # Check if the email or username is already registered
        cur.execute("SELECT * FROM user_login WHERE Email = %s", (email,))
        existing_email = cur.fetchone()
        if existing_email:
            return jsonify({'message': 'Email already in use'}), 400

        cur.execute("SELECT * FROM user_login WHERE Password = %s", (password,))
        existing_username = cur.fetchone()
        if existing_username:
            return jsonify({'message': 'Username already in use'}), 400

        
        
        cur.execute("INSERT INTO user_login (Email, Password) VALUES (%s, %s)", (email, password))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User login successfully'}),201
#    return render_template("index.html")


if __name__ =="__main__":
    app1.run(debug=True)