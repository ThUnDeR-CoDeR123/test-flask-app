from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
serect_keys = 'd55cc5e7c5c840b29eac8831d43203da'


# class user(db.Model):
#      __tablename__ = 'userslist'
#      Id=db.Column('user_id',db.Integer, primary_key=True)
#      username = db.Column('username',db.String(50))
#      password = db.Column('password',db.String(50))

#      def __init__(self,username,password):
#           self.username=username
#           self.password=password

#      def __repr__(self):
#         return '<id {}>'.format(self.Id)


# #APPEND DATA TO USERLIST 
# def add_user(username,password):
#     successful=True
#     try:
#        with psycopg2.connect(database=url.path[1:],
#        user=url.username,
#        password=url.password,
#        host=url.hostname,
#        port=url.port
#        ) as conn:
#            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
               
#                INSERT_SCRIPT = 'INSERT INTO USERLIST (ID,USERNAME, PASSWORD) VALUES (%s, %s, %s)'
               
#                cur.execute('SELECT user FROM USERLIST')
#                #checks if username and password are not null
#                if username and password:
#                      cur.execute('SELECT ID FROM USERLIST')
#                      #cur.fetchall---> [ [], [] [],, [], [], [], [], [], []] 
#                      curent_id=cur.fetchall()[-1][-1]+1
#                      cur.execute(INSERT_SCRIPT,(curent_id,username,password))

#     except Exception as e:
#        print(e)
#        successful = False
#     finally:
#         conn.close()
#         return successful


# #search for user and returns password
# def search_user(username):
#      pwrd = None
#      try:
#           with psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port) as conn:
#                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#                     SEARCH_SCRIPT ="SELECT * FROM USERLIST WHERE USERNAME = '"+username+"'"
       
#                     cur.execute(SEARCH_SCRIPT)

#                     pwrd=cur.fetchone()[-1]
#                     print("search func : ", pwrd)
#      except Exception as e:
#           print(e)
#      finally:
#           conn.close()
#           return pwrd

# #returns all the data in the list
# def get_userlist():
#     data = "hahahaha"
#     try:
#           with psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port) as conn:
#                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#                     SEARCH_SCRIPT ="SELECT * FROM USERLIST"
#                     cur.execute(SEARCH_SCRIPT)
#                     data=cur.fetchall()
                    
#     except Exception as e:
#           print(e)
#     finally:
#           conn.close()
#           return str(data)