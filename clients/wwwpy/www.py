import os
from signinui import *
from signupui import *
from home import *
from orderui import *
from calenderui import *

'''
Created on Aug 20, 2015

@author: kristapher
'''           
def main():

    #ui = SigninUI()
    #ui = SignupUI()
    ui = HomeUI()
    #ui = OrderUI()
    #ui = CalendarUI()
    ui.main()

if  __name__ =='__main__':
    main()





