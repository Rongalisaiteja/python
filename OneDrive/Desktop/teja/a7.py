mat=int(input("enter mat marks"))
tel=int(input("enter tel marks"))
eng=int(input("enter eng marks"))
total=mat+tel+eng
print("total=",total)
per=(total/300)*100
print("per=",per)
if(per>60):
    print("frist class")
elif(per>40):
    print("second class")
else:
    print("fail")

