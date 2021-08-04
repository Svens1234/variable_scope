#pi = 'outer pi variable'


#def print_pi():
    #pi = 'inner pi variable'
    #print(pi)


#print_pi()
#print(pi)


#Local Scope

#pi = 'global pi variable'
#def inner():
    #pi = 'inner pi variable'
    #print(pi)


#inner()


#pi = 'global pi variable'
#def inner():
    #pi = 'inner pi variable'
    #print(pi)


#inner()


#pi = 'global pi variable'
#def inner():
    #pi = 'inner pi variable'
    #print(pi)

#inner()
#print(pi)


#pi = 'global pi variable'
#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #nonlocal pi
        #print(pi)
    #inner()

#outer()
#print(pi)



#pi = 'global pi variable'
#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #nonlocal pi
        #print(pi)
    #inner()

#outer()
#print(pi)



#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #pi
        #print(pi)
    #inner()

#outer()
#print(pi)



#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #pi = 'new value'
        #print(pi)
    #inner()

#outer()
#print(pi)




#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #nonlocal pi
        #pi = 'new value'
        #print(pi)
    #inner()

#outer()
#print(pi)




#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #nonlocal pi
        #pi = 'new value'
        #print(pi)
    #inner()
    #print(pi)

#outer()
#print(pi)




#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #global pi
        #pi = 'new value'
        #print(pi)
    #inner()
    #print(pi)

#outer()
#print(pi)




#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #pi = 'inner pi variable'
        #global pi
        #print(pi)
    #inner()
    #print(pi)

#outer()
#print(pi)



#from math import pi

#def outer():
    #def inner():
        #print(pi)
    #inner()

#outer()


#from math import pi

#pi = 'global pi variable'

#def outer():
    #def inner():
        #print(pi)
    #inner()

#outer()



#from math import pi

#pi = 'global pi variable'

#def outer():
    #pi = 'outer pi variable'
    #def inner():
        #print(pi)
    #inner()

#outer()




from math import pi

pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        pi = 'inner pi variable'
        print(pi)
    inner()

outer()
