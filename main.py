from flask import Flask
from flask import render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="Yamaha@8763",database="flaskdata")
cuser=conn.cursor()
app=Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///firstdb.db"
# db=SQLAlchemy(app)
# class Contactus(db.Model):
#     myid=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     mytitle=db.Column(db.String(120))
#     mymessage=db.Column(db.Text)
# with app.app_context():    
#    db.create_all()    
# @app.route("/")
# def basefile():
#     return render_template("base.html")
@app.route("/")
def homepage():
    return render_template("home.html")
@app.route("/about")
def aboutuss():
    return render_template("myap/aboutus.html")
@app.route("/services")
def myservices():
    cuser.execute("select * from flasksave")
    data=cuser.fetchall()
    return render_template("myap/services.html",mydata=data)
@app.route("/contact")
def contactus():
    return render_template("contact.html")
@app.route("/savethis",methods=["POST"])
def savethisdata():
    if request.method=="POST":
        titles=request.form.get("title")
        message=request.form.get("msg")
        cuser.execute(f"insert into flasksave values('{titles}','{message}')")
        conn.commit()
        # data=Contactus(mytitle=titles,mymessage=message)
        # db.session.add(data)
        # db.session.commit()
        return redirect("/contact")
@app.route("/deletethisdata/<a>",methods=["POST"])
def deletedata(a):
    cuser.execute(f" delete from flasksave where title='{a}'")
    return redirect("/services")


if __name__ =="__main__":
    app.run(debug=True)
