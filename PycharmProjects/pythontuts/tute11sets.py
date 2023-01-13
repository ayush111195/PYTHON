                                   # sets in python--->>>

s=set()
print(type(s))
s_from_list= set([1,2,3,4,5])
print(type(s_from_list))
print(s_from_list)

s.add(6)# new element add karne ke leye
s.add(7)
s.add(8)
print(s)

s1=s.union({1,2,3,4})#new dis add karne ke leye
print(s,s1)

s2=s.intersection({8,7,3})# s ke all element and s2 ke wo element jo s2 main bhi h wo
print(s,s2)

s.remove(7)# remove karne ke leye
print(s)

s.discard(8)#Remove the specified item
print(s)

