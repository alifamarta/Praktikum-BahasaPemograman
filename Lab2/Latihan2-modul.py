gaji = int(input("Masukkan gaji: "))
berkeluarga = (False,True)[input("Sudah berkeluarga ? (Y/T)") == "Y"]
punya_rumah = (False,True)[input("Punya rumah (Y/T)") == "Y"]

if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib mengikuti asuransi dan menabung untuk pensiun ")

    else:
        print("Tidak perlu mengikuti asuransi")

    if punya_rumah:
        print("wajib bayar pajak")
    else:
        print("Tidak wajib bayar pajak")

else:
    print("Gaji belum UMR")