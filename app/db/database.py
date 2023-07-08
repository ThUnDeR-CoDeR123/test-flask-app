
import urllib.parse as up
import psycopg2, psycopg2.extras
up.uses_netloc.append("postgres")
url = up.urlparse("postgres://ecelilmw:Eb9eNRBLa1rQeA1O6eSAZjRC9BUJwDBm@tiny.db.elephantsql.com/ecelilmw")
CREATE_SCRIPT = '''CREATE TABLE IF NOT EXISTS USERLIST (
                     ID INT PRIMARY KEY,
                     USERNAME VARCHAR(50) NOT NULL,
                     PASSWORD VARCHAR(50) NOT NULL
)'''
'''
################################ --------------------------------DEMO TEMPLATE--------------------------------
# with psycopg2.connect(database=url.path[1:],
#        user=url.username,
#        password=url.password,
#        host=url.hostname,
#        port=url.port
#        ) as conn:
#            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#                   cur.execute(CREATE_SCRIPT,None)
#                   #cur.execute("INSERT INTO USERLIST (ID,USERNAME,PASSWORD) VALUES (2,'anushka@gmail.com','2023')")
#                   cur.execute('SELECT * FROM USERLIST')
#                   print(cur.fetchall())

# conn.close()
'''

#APPEND DATA TO USERLIST 
def add_user(username,password):
    successful=True
    try:
       with psycopg2.connect(database=url.path[1:],
       user=url.username,
       password=url.password,
       host=url.hostname,
       port=url.port
       ) as conn:
           with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
               
               INSERT_SCRIPT = 'INSERT INTO USERLIST (ID,USERNAME, PASSWORD) VALUES (%s, %s, %s)'
               
               cur.execute('SELECT user FROM USERLIST')
               #checks if username and password are not null
               if username and password:
                     cur.execute('SELECT ID FROM USERLIST')
                     #cur.fetchall---> [ [], [] [],, [], [], [], [], [], []] 
                     curent_id=cur.fetchall()[-1][-1]+1
                     cur.execute(INSERT_SCRIPT,(curent_id,username,password))

    except Exception as e:
       print(e)
       successful = False
    finally:
        conn.close()
        return successful


#search for user and returns password
def search_user(username):
     pwrd = None
     try:
          with psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port) as conn:
               with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    SEARCH_SCRIPT ="SELECT * FROM USERLIST WHERE USERNAME = '"+username+"'"
       
                    cur.execute(SEARCH_SCRIPT)

                    pwrd=cur.fetchone()[-1]
                    print("search func : ", pwrd)
     except Exception as e:
          print(e)
     finally:
          conn.close()
          return pwrd

#returns all the data in the list
def get_userlist():
    data = "hahahaha"
    try:
          with psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port) as conn:
               with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    SEARCH_SCRIPT ="SELECT * FROM USERLIST"
                    cur.execute(SEARCH_SCRIPT)
                    data=cur.fetchall()
                    
    except Exception as e:
          print(e)
    finally:
          conn.close()
          return str(data)