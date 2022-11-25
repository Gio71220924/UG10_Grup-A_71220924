no1 = int(input("masukan nilai soal 1 :"))
no2 = int(input("masukan nilai soal 2 :"))
no3 = int(input("masukan nilai soal 3 :"))
umur = int(input("masukan umur anda:"))
           
point1 = (no1*50/100)
point2 = (no2*30/100)
point3 = (no3*20/100)

ratarata = (point1+point2+point3)
print("Rata-rata nilai anda:",ratarata)
if (umur<=25):
    if ratarata>=80:
        print("selamat anda lulus")
    else :
        print("Coba lagi tahun depan!")

else:
    if ratarata>=90:
        print("Selamat anda lulus")
    else:
        print("coba lagi tahun depan!")
        

    
