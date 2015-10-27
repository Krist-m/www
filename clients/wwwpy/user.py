class User:
    
    def __init__(self, fn, ln, pwd, phoneno, photo, sp = False, servicename = None):
        self.id = None
        self.mFirstName = fn
        self.mLastName = ln
        self.mPassword = pwd
        self.mPhoneNo = phoneno
        self.mPhoto = photo
        self.mIsServiceProvder = sp
        self.mServiceName = servicename
        
    @staticmethod
    def create_from_list(list):
        return User(list[1],list[2],list[3],list[4],list[5])

