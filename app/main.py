from flask import Flask
from blueprints.user import blueprint_signup,blueprint_login,blueprint_getuserlst
from db.database import db
from admin.setup import SECRET_KEY, SQLALCHEMY_DATABASE_URI


app=Flask(__name__)
UPLOAD_FOLDER = './db'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATINOS'] = True
db.init_app(app)


app.register_blueprint(blueprint_signup)
app.register_blueprint(blueprint_login)
app.register_blueprint(blueprint_getuserlst)

@app.route("/")
def test():
    return 'this is working'

if __name__ == "__main__":
    app.run(debug=True, port=8080,host='0.0.0.0')
    db.create_all()
