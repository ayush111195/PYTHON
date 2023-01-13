                                   #list in python--->>

grocery=["harpic","vim bar","deodrant","bhindi","lollypop"]
print(grocery)
print(grocery[4])

grocery.sort()# ye short karta h
print(grocery)

grocery.reverse()# ye reversh karta h
print(grocery)

numbers=[2,3,4,5,6,7]
numbers.append(30)# ye list ke end main nnumber ko add karwata h

numbers1=[8,9,10,11,12,13]
numbers1.extend(numbers) # ye ek list main dusri ko extend karwata h
print(numbers1)

numbers.insert(2,66)# ye kise bhi place pr addb karta h chejo ko
print(numbers)

numbers.remove(2)# btaye gye element ko dlt kar deta h
print(numbers)

numbers.pop()#ye last wale element ko hta deta h
print(numbers)

numbers1.clear()
print(numbers1)

print(numbers.index(66))# kise bhi element ka place btata h

print(numbers.count(3))# inddex main kaunsa element kitni baar h

print(str(grocery).isnumeric())
# hum kise bhi list ke element ko change kar skte h
numbers[1]=44
print(numbers)
#mutable=can change
#ammutable=can not change
#list are mutable
#tuple are ammutable
tp=(1,2,3,4,5)
#tp(1)=33 yhan ye eeror show karega
tp1=(1)
print(tp) # yhan result 1 ayega () nhi ayega
tp2=(1,)
print(tp2)# yhan result (1) ayega
# inter change 2 num --->>
#1. in other lanq=
a=1
b=8
temp=a
a=b
b=temp
print(a,b)
#. in python=
a=1
b=8
a,b=b,a
print(a,b)

# how to change list in to dictionary= use"dict" method

list1=[["harry",1],["larry",2],["carry",3],["marry",4]]
change=dict(list1)
print(change)