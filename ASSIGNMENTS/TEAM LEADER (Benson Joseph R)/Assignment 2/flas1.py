from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello this is my first flask project<h1>HELLO!!</h1>"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__== "__main__":
	app.run()