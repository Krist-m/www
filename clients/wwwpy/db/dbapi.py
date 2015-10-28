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
        id = None
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO users VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) RETURNING id",(userinfo.mLastName, userinfo.mFirstName, userinfo.mPhoneNo,
                                                                    userinfo.mPassword, psycopg2.Binary(userinfo.mPhoto), userinfo.mIsServiceProvder))
            id = cur.fetchone()[0]
            if userinfo.mIsServiceProvder:
                cur.execute("INSERT INTO serviceprovider VALUES (%s, %s)",(id, userinfo.mServiceName))
            self.conn.commit()
        except Exception as e:
            print "DB ERROR: while inserting user info."
            print e
        finally:
            cur.close()
            self.__close()
        return id
    
    
    def insert_address(self, userid, address):
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO address VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(userid, address.mLabel, address.mHouseno,
                                                                                        address.mStreetname, address.mCity, address.mState, 
                                                                                        address.mCountry, address.mPin, address.mAreaCode))
            self.conn.commit()
        except Exception as e:
            print "DB ERROR: while inserting address info."
            print e
        finally:
            cur.close()
            self.__close()

    def check_for_autorization(self, phoneno, passwd):
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE phone = %s AND password=%s", (phoneno, passwd))
            return cur.fetchone()
        except Exception as e:
            print "DB ERROR: while querying users info."
            print e
        finally:
            cur.close()
            self.__close()

        
    def get_service_list(self):
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM services")
            return cur.fetchall()
        except Exception as e:
            print "DB ERROR: while querying services."
            print e
        finally:
            cur.close()
            self.__close()

    def get_address_list(self, userid):
        self.__connect()
        cur = self.conn.cursor()
        try:
            print userid
            cur.execute("SELECT * FROM address WHERE uid = %s", [userid])
            return cur.fetchall()
        except Exception as e:
            print "DB ERROR: while query address."
            print e
        finally:
            cur.close()
            self.__close()
            
    def insert_order(self, orderinfo):
        self.__connect()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO order VALUES (DEFAULT, %s, %s, %s, %s, %s, )",(orderinfo.mUserId, orderinfo.mServiceid, orderinfo.mWhenFrom,
                                                                                    orderinfo.mAddId, orderinfo.mStatus))
            self.conn.commit()
        except Exception as e:
            print "DB ERROR: while inserting address info."
            print e
        finally:
            cur.close()
            self.__close()
        