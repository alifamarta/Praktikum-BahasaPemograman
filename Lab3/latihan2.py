import random
n = int(input("Masukkan nilai N: "))

for i in range (n):
    a = random.uniform(0.0,0.5)
    print("Data ke :",i+1,"=> ",a)
