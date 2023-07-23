from db.database import db
class User(db.Model):
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


