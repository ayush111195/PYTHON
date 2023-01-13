                    # break and continue statement--->>>
i=0
while(True):
    if i+1<5:
        i=i+1
        continue

    print(i+1)
    if (i==44):
        break
    i=i+1

# quizz--->>
while(True):
    i1=int(input("enter the num="))
    if(i1<100):
        print("grater then 100",i1)
        continue
    else:
        print("you print the right num")
        break