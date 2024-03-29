from flask import Flask
from flask import render_template
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
if __name__ =="__main__":
    app.run(port=1000,debug=True)
