                                         #strings---->>>

mystr="ayush is a good boy"

print(mystr[0:4])# ismain ye 4 no wala ko nhi leta only (0,1,2,3)  ko hi lega...

print(mystr[0:5])
print(len(mystr))
print(mystr[0:5:2])# ismain ye 0 se start karega aur har dusre char ko lega ...

print(mystr[ :5])# khali jgh pr khud se "0" le lega ..

print(mystr[0: ])#khali jgh pr khus se string ke length le lega ...

print(mystr[ : ])#dono jgh khali chodne par wo puri string ko print karwa dega pehle wale ko "0" aur dusre wale ko
# legnth ke brabar manta h

print(mystr[ : : ])# teno kko khali chodne par bhi ye puri string ko print karwa dega ...

#  teshre wale ka use jgh ko chodne ke leye kiya jata h
print(mystr[ : :3])# yhan teshre wale main value 3 h to ye teshre char ko skip kar deti  h ....

print(mystr.isalnum())#ye humko flase return karegga agr ismain spaces hue to warna true karega

print(mystr.count("b"))#ye humko kise bhi char ki counting dega

print(mystr.capitalize())# pehle latter ko capital kar dega

print(mystr.find("is"))# ye humko is ka place batayega

print(mystr.upper())# puri string ko upper case main convert kar dega

print(mystr.lower())# puri string ko lower main convert kar dega


