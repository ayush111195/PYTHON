                                 #try except exception---->>>>
print("enter your num=")
num=input()
print("enter your 2nd num=")
num1=input()
try:
    print("the sum of these two num=",
          int(num)+int(num1))
except Exception as e:
    print(e)

# maan lo ko koi int ki jgh kuc aur de de input main to erroe show kr dega aur aage kaprogram bhi work nhi karega
#
print("this is very impornant ")