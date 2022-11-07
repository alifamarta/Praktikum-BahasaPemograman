x = 100000000

for a in range(1,9):
    if(a>=1 and a<=2):
        b = x * 0
        print("Laba bulan ke-",a," : ",b)
    if(a>=3 and a<=4 ):
        c = x * 0.1
        print("Laba bulan ke-",a," : ",c)
    if(a>=5 and a<=7):
        d = x * 0.5
        print("Laba bulan ke-",a," : ",d)
    if(a==8):
        e = x*0.2
        print("Laba bulan ke-",a," : ",e)
total=b+b+c+c+d+d+d+e
print("\nTotal laba adalah : ",total)