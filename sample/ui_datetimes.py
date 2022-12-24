#!/usr/bin/phthon3
'''
making one or several datetime objs.
'''

import datetime


aDay = str()
tmpDays = list()


def ret_datetime( day_str ):
    tmp_datetime1=datetime.datetime.strptime(
                                                    day_str,   "%d/%m/%Y"  )
    return(tmp_datetime1)

def ret_datetimes( days_str ):
    for day in days_str:
        tmpDays.append(
                    ret_datetime( day )
        )
    return( tmpDays )

##
def input_oneDay_str():
    aDay = input('enter a day, day/month/year: ')
    #aDay = '11/01/2013'    #for debugging

    #datetime객체로 변환
    # ret a day
    tmp_datetime1=ret_datetime( aDay )
    ##debug
    print( 
                tmp_datetime1.strftime( '%B, %d, %Y' ),
                                ' is ',
                tmp_datetime1.strftime( ' %A  ' )
                )
##

##
def input_Days_str():
    #making a list() about datetimeS.
    tmpDays_str=[]
    while True:
        tmp= input( "enter a day, day/month/year: \n  ( '0' is closing. )"
        )
        tmpDays_str.append( tmp )
        if tmpDays_str[-1] == "0":
              tmpDays_str.pop()
              ret_datetimes( tmpDays_str )              
              break

    print( tmpDays )
##

if __name__=="__main__":
    input_oneDay_str()
    input_Days_str()