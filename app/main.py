from flask import Flask,Response,request,jsonify,send_file,flash,redirect,url_for,make_response
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select



app=Flask(__name__)
UPLOAD_FOLDER = './db'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'd55cc5e7c5c840b29eac8831d43203da'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://ecelilmw:Eb9eNRBLa1rQeA1O6eSAZjRC9BUJwDBm@tiny.db.elephantsql.com/ecelilmw"
app.config['SQLALCHEMY_TRACK_MODIFICATINOS'] = True
db = SQLAlchemy(app)

class user(db.Model):
     __tablename__ = 'userslist'
     Id=db.Column('user_id',db.Integer, primary_key=True)
     username = db.Column('username',db.String(50))
     password = db.Column('password',db.String(50))

     def __init__(self,username,password):
          self.username=username
          self.password=password
        #   db.session.create_all()

     def __repr__(self):
        return '<id {}>'.format(self.Id)
@app.route("/")
def test():
    return 'this is working'


@app.route("/signup",methods=['POST'])
def signup():
    data=request.get_json()
    success=True
    errstr=''
    try:
        TempUser=user(data['username'],data['password'])
        db.session.add(TempUser)
        db.session.commit()
    except Exception as e:
        success=False
        errstr=e.message
    finally:
        if(success):
            return make_response('success',201)
        else :
            return make_response('failure',401,errstr)

@app.route('/get_user',methods=['GET'])
def get_user():
    data=user.query.all()
    result=[{"ID":item.Id,"username" : item.username, "password" : item.password} for item in data]
    return result

@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    db_statement=select(user.password).where(user.username==data["username"])
    try:
        l=db.session.execute(db_statement).first()[0]
        if l==data["password"]:
            return 'login successful'
        else:
            return 'login failed'
    except Exception as e:
        return e.message
    
    return str(l)
if __name__ == "__main__":
    app.run(debug=True, port=8080,host='0.0.0.0')
    db.create_all()
