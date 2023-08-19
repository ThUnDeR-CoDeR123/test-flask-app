from flask import Blueprint,request,make_response,jsonify
from db.database import db,serect_keys
from sqlalchemy import select
from models.user import User
import jwt

blueprint_signup = Blueprint('blueprint_signup',__name__)
blueprint_login = Blueprint('blueprint_login',__name__)
blueprint_getuserlst = Blueprint('blueprint_getuserlst',__name__)



def token_required(func):
    #@wraps(func)
    def decorated(*args, **kwargs):
        token=request.args.get('token')
        
        if not token:
            return jsonify({'Alert!': 'Token is missing!'})
        try:
            payload=jwt.decode(token,serect_keys,algorithms=["HS256"])
            # if payload['username'] and  payload['password']:
            #     return jsonify('verified payload : ',payload)
            payload=func()

            return str(payload)
        except Exception as e:
            return str(e)
    return decorated


@blueprint_signup.route('/user-signup',methods=['POST'])
def signup():
    data=request.get_json()
    success=True
    errstr=''
    try:
        TempUser=User(data['username'],data['password'])
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

@blueprint_getuserlst.route('/get_user',methods=['POST'])
@token_required
def get_user():
    data=User.query.all()
    result=[{"ID":item.Id,"username" : item.username,"password":item.password} for item in data]
    return result


@blueprint_login.route('/login',methods=['POST','GET','PUT'])
def login():
    data=request.get_json()
    db_statement=select(User.password).where(User.username==data["username"])
    try:
        l=db.session.execute(db_statement).first()[0]
        if l==data["password"]:
            token=jwt.encode({
            'username':data['username'],
            'password':data['password']
            },
        serect_keys)
            return jsonify(token=token)
        else:
            return 'Invalid Password or Password'
    except Exception as e:
        return str(e)