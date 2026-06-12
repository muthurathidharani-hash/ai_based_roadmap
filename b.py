from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

LOGIN_PASSWORD = "muthu404"   # Hardcoded password

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        if password == LOGIN_PASSWORD:
            return redirect(url_for("homepage"))
        else:
            return "Invalid Password!"
    return render_template("login.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
