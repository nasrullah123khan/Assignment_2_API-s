from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL 

app2 = Flask(__name__)
mysql = MySQL(app2)


app2.config['MYSQL_HOST']='localhost'
app2.config['MYSQL_USER']='root'
app2.config['MYSQL_PASSWORD'] = "db"
app2.config['MYSQL_DB']= 'mydb'


@app2.route("/" ,methods=["POST"])
def create_blog():
    if request.method=="POST":
        title = request.json['Title']
        blog = request.json['Blog']

        cur = mysql.connection.cursor()
        
        
        cur.execute("INSERT INTO blog (Title, Blog) VALUES (%s, %s)", (title, blog))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Create a blog successfully'}),201
#    return render_template("index.html")


if __name__ =="__main__":
    app2.run(debug=True)
