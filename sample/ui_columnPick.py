#!/usr/bin/python3
'''
p176
'''

import os

tmpstr="fgghf"
f_name='p176.py'        # file name
os.chdir("../data_mgm_intro/")    # path changing

#os.execl( f_name, tmpstr )
os.execl( f_name,
                  tmpstr,        # execl requested, must-have arg
                  
                  )