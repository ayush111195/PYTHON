                                        #tell()--->>>

#tell() function ka use umlog filepointer kidhar h  btane ke leye kiya jata h
f=open("shivam.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
                                       #seek()---->>>

#seek() function ka use hum filepointer ko apne acording movie kaene ke leye karte h
f.seek(32)
print(f.readline())
f.close()