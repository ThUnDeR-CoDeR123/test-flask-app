from flask import Blueprint,request,make_response,jsonify
from db.database import db,serect_keys
from sqlalchemy import select
from models.user import User
import os
import jwt
upload_file = Blueprint('upload_file',__name__)
@upload_file.route('/upload_file', methods = ['PUT','POST'])  
def success():  
    if request.method == 'POST': 
        try:

            f = request.files['file']
            f.save(os.path.join(r'D:\knowshare\my repo\test-flask-app\app\db\notes',f.filename))
            return "Success!"
        except Exception as e:
            return e.message