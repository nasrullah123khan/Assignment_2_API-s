from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL 

app3 = Flask(__name__)
mysql = MySQL(app3)


app3.config['MYSQL_HOST']='localhost'
app3.config['MYSQL_USER']='root'
app3.config['MYSQL_PASSWORD'] = "db"
app3.config['MYSQL_DB']= 'mydb'


@app3.route("/" ,methods=["POST"])
def post_comment():
    if request.method=="POST":
        comm = request.json['comment_texts']


        cur = mysql.connection.cursor()
        
        
        cur.execute("INSERT INTO comments (comment_texts) VALUES (%s)", (comm))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Comment Posted successfully'}),201
#    return render_template("index.html")


if __name__ =="__main__":
    app3.run(debug=True)
