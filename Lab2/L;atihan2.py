a = int(input("Masukkan bilangan a: "))
b = int(input("Masukkan bilangan b: "))
c = int(input("Masukkan bilangan c: "))

if a<b and a<c:
    if b<c:
        print ("urutan bilangan:",a,b,c)
    else:
        print("urutan bilangan:",a,c,b)

elif b<a and b<c:
    if a<c:
        print("urutan bilangan:",b,a,c)
    else:
        print("urutan bilangan:",b,c,a)

else:
    if a<b:
        print("urutan bilangan",c,a,b)
    else:
        print("urutan bilangan:",c,b,a)