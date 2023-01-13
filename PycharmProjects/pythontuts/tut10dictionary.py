                                 #dictionary----->>>

          #dictionary is nothing but kay value pairs..... in python is a data strucher type...

d1={}
d2={"harry":"burger","rohan":"fish","ayush":"roti"}
print(d2["harry"])
d3={"harry":"burger","rohan":"fish","ayush":"roti","shubham":{"b":"maggie","l":"roti","c":"chawal"}}
print(d3["shubham"] ["b"])

d2["ankit"]="junk food"# to add new element
print(d2)

print(d2.copy())# copy the element

print(d2.get("ayush"))# to get the element

d2.update({"leena":"toffee"})
print(d2)# to update any element

print(d2.keys())# to give all key from dictionary

del d2["rohan"]# to dlt the element
print(d2)

print("all item=",d2.items())
                  #quiz--->>>>
ayush={"apple":"khane ka shamaan","orange":"narangi","banana":"lamba lamba "}
print(ayush["apple"])
