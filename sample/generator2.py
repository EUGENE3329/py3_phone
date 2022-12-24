import  os,  pickle


f_name = 'xl_columns_iter.pickle'
fd = open( f_name, 'rb' )
obj = pickle.load( fd )

for i in obj:
    print( type(i),  ' : ', i.value )
    
print( len(obj)  )
td = obj[0].value 
print( dir(td)  )
print( td.strftime( '%Y, %A' ), td.year, td.weekday() )

#정리할 거
#datetime, decimal, generator, 
#pickle, 