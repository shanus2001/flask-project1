from flask import Flask
from flask import render_template,request
app=Flask(__name__)
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
    return render_template("myap/services.html")
@app.route("/contact")
def contactus():
    return render_template("contact.html")
@app.route("/savethis",methods=["post"])
def savethisdata():
    if request.method=="post":
        titles=request.form.get("title")
        message=request.form.get("msg")
        print(titles,message)
    return "data saved success fully"
if __name__ =="__main__":
    app.run(debug=True)
