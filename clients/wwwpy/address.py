class Address:
    
    def __init__(self, houseno, streetname, city, state, country, pin, label="Home", areacode= None):
        self.mLabel = label
        self.mHouseno = houseno
        self.mStreetname = streetname
        self.mCity = city
        self.mState = state
        self.mCountry = country
        self.mPin = pin
        self.mAreaCode = areacode

