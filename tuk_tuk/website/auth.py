from flask import Blueprint, render_template, request, jsonify,redirect,url_for,flash

auth = Blueprint("auth", __name__)

@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method =="POST":
        name = request.form.get("firstName","").strip()
        email = request.form.get("email","").strip()
        password1 = request.form.get("password1","")
        password2 = request.form.get("password2","")

        if not name or email or not password1 or not password2:
            flash("Please fill in all fields.","danger")
        elif password1 != password2:
            flash("Please fill in all fields.","danger")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", "danger")
        else:
            #data base
            flash("Account created.", "succes")
        return redirect(url_for("auth.sign_up"))
    return render_template('signup.html')

@auth.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email","").strip()
        pasword = request.form.get("password","")
        #login verification
        flash("")
        return redirect(url_for("auth.login"))
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('logout.html'))

@auth.route('/about')
def about():
    return render_template('about.html')

