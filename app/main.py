from flask import Flask
from blueprints.user import blueprint_signup,blueprint_login,blueprint_getuserlst
from blueprints.notes import upload_file
from db.database import db
from admin.setup import SECRET_KEY, SQLALCHEMY_DATABASE_URI


app=Flask(__name__)
UPLOAD_FOLDER = r'D:\knowshare\my repo\test-flask-app\app\db\notes'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "d55cc5e7c5c840b29eac8831d43203da"
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://ecelilmw:Eb9eNRBLa1rQeA1O6eSAZjRC9BUJwDBm@tiny.db.elephantsql.com/ecelilmw"
app.config['SQLALCHEMY_TRACK_MODIFICATINOS'] = True
db.init_app(app)


app.register_blueprint(blueprint_signup)
app.register_blueprint(blueprint_login)
app.register_blueprint(blueprint_getuserlst)
app.register_blueprint(upload_file)


@app.route("/")
def test():
    return 'this is working'

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
