                         #write mode --->>>
f=open("shivam.txt","w") # agr koi file pehle se hogi to uske andr ka data hhta degi aur nya data jo bhi doge usko rakh degi
f.write("shivam bhai bhut accha admi h \n") # agr  nhi h to nyi file bn jayegi...

# agr nyi line add karni h to mode main "a" rakhte h ...
f=open("shivam.txt","a")# add karne ke leye mode main "a" rakte h
f.write("ayush shivam ka bhai h vo bhut nalayak h\n ")

# agr humko filr ke andr ke char ko dekhna h ki humne kitne char likhe h uske leye --->>>
a=f.write("ayush ka pura naam ayushh gupta h\n ")
print(a)
f.close()

# handle read and write both---->>>
f=open("shivam.txt","r+")
print(f.read())
f.write("shivam ka pura naam shivam sachan h")