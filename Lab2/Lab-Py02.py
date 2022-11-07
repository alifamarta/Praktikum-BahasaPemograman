a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
c = int(input("masukkan nilai c: "))

if a>b and a>c:
    print(a,"yang terbesar")
elif b>a and b>c:
    print(b,"yang terbesar")
else:
    print(c,"yang terbesar")