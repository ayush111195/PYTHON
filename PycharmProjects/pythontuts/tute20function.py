                                       #fuctions in python---->>>

#a=5
#b=6
#c=sum((a,b))           # built in function
#print(c)

#koi bhi fuction bnane ke leye uske pehle "def" ka use kiya jata h ...
def function1 ():
    print("you r in function 1 ")
function1()
#print(function1())
    # hum isko direct call karwaye to only jo jo function ke andr h wahi dega
    #print(function1()) # function1 ko print ke sath call karwa rahe h isleye ye none bhi de rha h

# function ke ander hum input bhi le skte h -->>
def function2 (a,b):
    """this is a function which will calculate average of two number""" #--->> this is a doc_string
    # doc_string = jo humko function ka work smjhaye usko bola jata h
    # kise bhi  function ki doc_string ko dekhne ke leye hum log print(function2.__doc__)

    average=(a+b)/2
#   print(average)
    return average  #agr humko isko variable main store karwana h tab ke leye h
v=function2(5,7)
print(v)            # do baar average a rha 1. print(average  )ke wjh se a rha h 2.print(v) ki wjh se a rha
print(function2.__doc__)
