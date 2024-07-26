from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL 

app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD'] = "db"
app.config['MYSQL_DB']= 'mydb'


@app.route("/" ,methods=["POST"])
def user_regitration_email():
    if request.method=="POST":
        email = request.json['Email']
        password = request.json['Password']
        username = request.json['Name']

        cur = mysql.connection.cursor()


        # Check if the email or username is already registered
        cur.execute("SELECT * FROM user WHERE Email = %s", (email,))
        existing_email = cur.fetchone()
        if existing_email:
            return jsonify({'message': 'Email already in use'}), 400

        cur.execute("SELECT * FROM user WHERE Name = %s", (username,))
        existing_username = cur.fetchone()
        if existing_username:
            return jsonify({'message': 'Username already in use'}), 400

        
        
        cur.execute("INSERT INTO user (Email, Password, Name) VALUES (%s, %s, %s)", (email, password, username))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User registered successfully'}),201
#    return render_template("index.html")


if __name__ =="__main__":
    app.run(debug=True)
