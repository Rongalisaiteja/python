a= int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a<b and a<c):
    if(b<c):
        print("a,b,c=",a,b,c)
    else:
        print("a,c,b=",a,c,b)
elif(b<a and b<c):
    if(a<b):
        print("b,a,c=",c,a,b)
    else:
        print("b,c,a=",b,c,a)
elif(c<a and c<b):
    if(c<a):
        print("c,a,b=",c,a,b)
    else:
        print("b,c,a=",b,c,a)
    
    
