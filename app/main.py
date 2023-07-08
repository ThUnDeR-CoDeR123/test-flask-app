from flask import Flask,Response,request,jsonify,send_file,flash,redirect,url_for,session,make_response
from werkzeug.utils import secure_filename
import os
import jwt
import sys
sys.path.append("db")
from db.database import search_user,add_user,get_userlist
from functools import wraps


app=Flask(__name__)
UPLOAD_FOLDER = './db'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'd55cc5e7c5c840b29eac8831d43203da'



#ALLOWED FILE EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def token_required(func):
    #@wraps(func)
    def decorated(*args, **kwargs):
        token=request.args.get('token')
        
        if not token:
            return jsonify({'Alert!': 'Token is missing!'})
        try:
            payload=jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            # if payload['username'] and  payload['password']:
            #     return jsonify('verified payload : ',payload)
            payload=func()

            return str(payload)
        except Exception as e:
            return str(e)
    return decorated

@app.route('/auth',methods=['POST'])
@token_required
def auth():
    return 'JWT is valid'


@app.route('/getdata',methods=['GET'])
def getdata():
    return get_userlist()


@app.route('/login',methods=['POST'])
def login():
    # searches and storedpassword for corresponding username
    request_json_object = request.get_json()

    pwrd=search_user(request_json_object['username'])


    if not pwrd:
        return request_json_object
    if pwrd == request_json_object['password']:
        session['logged_in'] = True
        token=jwt.encode({
            'username':request_json_object['username'],
            'password':request_json_object['password']
        },
        app.config['SECRET_KEY'])

        # ,'token-data':jwt.decode(jwt=token,key=app.config['SECRET_KEY'],algorithms=["HS256"]) to decoded_jwt
        return jsonify({'token':token})
    else:
        return make_response('unable to verify ',403,{'WWW-Authenticate':'Basic realm="Authentication failed'})


@app.route("/")
def test():
    return {"message":"works"} 



@app.route("/signup",methods=['POST'])
def signup():
    data=request.get_json()

    success=add_user(data['username'],data['password'])

    if(success):
        return make_response('success',201)
    else :
        return make_response('failure',401)


'''
@app.route("/user-details")
def test_abc():
    return jsonify({"user-details" : user_id})

@app.route("/files-list")
def sendfilelist():
    return jsonify(files)

@app.route("/downloads/<string:name>")
def download_file(name):
    return send_file(f'.\db\\{name}.pdf')


@app.route("/signup",methods=['POST'])
def signup():
    data=request.get_json()
    userid=len(user_id)+1
    userno=f'user{userid}'
    user_id[userno]=data
    return jsonify({"user-details" : user_id})


@app.route('/upload-files', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            d={}
            d['filename']=filename
            d['url']=f'http://127.0.0.1:8080/downloads/{filename}.pdf'
            entry='entry'+str(len(files)+1)
            files[entry]=d
            return redirect(url_for('download_file', name=filename))
    return 
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    
@app.route("/login",methods=['POST'])
def login():
    data=request.get_json()
    print(data)
    list_user=[i for i in user_id.values() if i['username']==data['username']]
    if len(list_user)!=0:
        return jsonify(list_user)
    else:
        return {'error':'Invalid username'}
'''


if __name__ == "__main__":
    app.run(debug=True, port=8080,host='0.0.0.0')