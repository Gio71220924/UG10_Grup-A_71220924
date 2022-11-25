print("==== Selamat datang di Toko Andi Tersenyum, selamat belanja!====")
a= int(input("Total belanja: Rp"))


       
if a>=100000:
    a= a-(a*2/100)
    print("Tidak ada diskon! Maka yang Anda bayarkan adalah Rp", a)

elif a>=500000:
    a= a-(a*5/100)
    print("Biaya yang harus dibayar setelah diskon adalah Rp", a)

elif a>=1000000:
    a= a-(a*10/100)
    print("Biaya yang harus dibayar setelah diskon adalah Rp", a)

else :
    print("Tidak ada diskon! Maka yang anda bayarkan adalah Rp",a)
    
    


