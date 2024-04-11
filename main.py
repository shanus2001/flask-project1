from flask import Flask
from flask import render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail, Message
# from sqlalchemy import delete
# import mysql.connector
# conn=mysql.connector.connect(host="localhost",username="root",password="Yamaha@8763",database="flaskdata")
# cuser=conn.cursor()
app=Flask(__name__)
app.secret_key="sdgewfhkgewkgufekggfewkj"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///firstdb.db"
db=SQLAlchemy(app)
class Contactus(db.Model):
    myid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    mytitle=db.Column(db.String(120))
    mymessage=db.Column(db.Text)
    myimage=db.Column(db.String(220))
with app.app_context():    
   db.create_all()  
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shanuchoudharyvikas@gmail.com'
app.config['MAIL_PASSWORD'] = 'efya knqk dsre wmjq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)      
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
    data=Contactus.query.all()
    # print(data, "sdsdsd")
    # data=db.fetchall()
    # cuser.execute("select * from flasksave")
    # data=cuser.fetchall()
    return render_template("myap/services.html",mydata=data)
    # return render_template("myap/services.html")
@app.route("/contact")
def contactus():
    return render_template("contact.html")
@app.route("/savethis",methods=["POST"])
def savethisdata():
    if request.method=="POST":
        titles=request.form.get("title")
        message=request.form.get("msg")
        imageee=request.files.get("img")
        if imageee:
            imageee.save(os.path.join("static/images",imageee.filename))
            path=os.path.join("static/images",imageee.filename)
        # cuser.execute(f"insert into flasksave values('{titles}','{message}')")
        # conn.commit()
        data=Contactus(mytitle=titles,mymessage=message,myimage=path)
        db.session.add(data)
        db.session.commit()
        msg = Message( 'Hello', sender ='shanuchoudharyvikas@gmail.com', recipients = ['shanuchoudharyvikas@gmail.com'] 
               ) 
        msg.body = 'Hello Flask message sent from Flask-Mail'
        mail.send(msg) 
        flash("data added successfully")
        return redirect("/contact")
@app.route("/deletethisdata/<int:myid>",methods=["POST"])
def deletedata(myid):
    user=Contactus.query.get(myid)
    # (same as.... )user=Contactus.query.filter_by(myid).first()
    db.session.delete(user)
    db.session.commit()
#     cuser.execute(f" delete from flasksave where title='{a}'")
    return redirect("/services")
@app.route("/updatethisdata/<int:myid>",methods=["POST"])  
def updatedata(myid):
    thisdata=Contactus.query.get(myid)
    return render_template("update.html",yourdata=thisdata)

@app.route("/nowupdatedata/<int:myid>",methods=["POST"])
def nowupdatedata(myid):
    if request.method=="POST":
        titles=request.form.get("title")
        message=request.form.get("msg")
        data=Contactus.query.get(myid)
        data.mytitle = titles
        data.mymessage = message
        db.session.commit()
        return redirect("/services")
    

if __name__ =="__main__":
    app.run(debug=True)
