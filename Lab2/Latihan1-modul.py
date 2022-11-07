nama = input ("Masukkan nama: ")
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))
tugas = int(input("Masukkan nilai Tugas: "))

akhir = ( tugas * .2) + (uts * .4) + (uas * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 75.0]

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama       :",nama)
print("Nilai UTS    :",uts)
print("Nilai UAS    :",uas)
print("Nilai Tugas  :",tugas)
print("Nilai akhir  :",akhir)
print("\nNilai Huruf :",huruf)
print("Keterangan   :",keterangan)