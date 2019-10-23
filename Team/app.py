from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
reason = ""

@app.route("/")
def root():
    #global is a keyword that allows an user to modify a variable outside the current scope
    global reason
    print(url_for("success"))
    #Check to see if user entered username and password
    if ("username" in request.args) & ("password" in request.args):
        usernam = request.args["username"]
        passwor = request.args["password"]
        #If password and username are correct, say so
        if (passwor == "1234") & (usernam == "Peglegs"):
            return redirect(url_for("success"))
        #If password and username are incorrect,
        elif (usernam != "Peglegs") & (passwor != "1234"):
            reason = " Your username and password were both incorrect"
            flash(reason)
            return redirect(url_for("try_again"))
        #If username is incorrect, say so
        elif (usernam != "Peglegs"):
            reason = " Your username was incorrect"
            flash(reason)
            return redirect(url_for("try_again"))
        #If password is incorrect, say so
        else:
            reason = " Your password was incorrect"
            flash(reason)
            return redirect(url_for("try_again"))
    return render_template(
    'login.html'
        )



@app.route("/signup")
def signup():
    return render_template(
        "signup.html"
        )

@app.route("/loggedIn")
def success():
    return render_template(
        "loggedIn.html"
        )


# page for creating a new story

if __name__ == "__main__":
    app.debug = True
    app.run()
