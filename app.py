from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager,login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager()

db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userId):
  return User.query.get(userId)

@app.route("/login", methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
      login_user(user)
      print(f"current user: {current_user}")
      return jsonify({"message": "Authentication successfully done!"}), 200

  return jsonify({"message": "Invalid credentials!"}), 400


@app.route("/logout", methods=["GET"])
@login_required
def logout():
  logout_user()

  return jsonify({"message": "Logout successfully done!"})
 

@app.route("/user", methods=["POST"])
def create_user():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created sucessfully!"}), 200
    
  return jsonify({"message": "Invalid credentials!"}), 400


@app.route("/", methods=["GET"])
def hello_world():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True)