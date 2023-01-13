f=open("ayush.txt","rt")# open main alga input mode hota h mtlb ki kiss mode main oprn karna h file ko r=read,t=text

#readlines function--->>
print(f.readlines())

#line main pure text ko print karwane ke leye--->>

for ayush in f:
    print(ayush,end="")

#read line function---->>>
print(f.readline()) # ye ek line ko print karta h ek baar main ...
print(f.readline())
print(f.readline())


"""
content=f.read(3)# yhan ye file  ke pehle 3  char ko read karega
print(content)

content=f.read(3)# yhan ye file ke agle 3 char ko read karega
print(content)


content=f.read()#yhan ye bache hue char ko  read karega
print(content)
f.close()
"""