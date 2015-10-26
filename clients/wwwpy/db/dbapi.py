import psycopg2

class DBAPI:
    conn = psycopg2.connect("dbname='wwwdb' user='postgres' host='localhost' password='harry1joey'")
    
    def __init__(self):
        pass
            
    def __connect(self):
        try:
            self.conn = psycopg2.connect("dbname='wwwdb' user='postgres' host='localhost' password='harry1joey'")
        except:
            print "Unable to connect to the database"
            return None
    
    def __close(self):
        self.conn.close()
    
    def insert_user_info(self, userinfo):
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO users VALUES (DEFAULT, %s, %s, %s, %s)",(userinfo.mLastName, userinfo.mFirstName, userinfo.mPhoneNo,
                                                                    "xxx"))
            self.conn.commit()
        except Exception as e:
            print "DB ERROR: while inserting user info."
            print e
        finally:
            cur.close()
            self.__close()
        
        
        