### PENGKONDISIAN/PENGKONDISIAN

nilai = 80

### syntax if dalam python :
### if ..kondisi.. :
### ..aksi..

### cara 1) dengan 'sama dengan' (==)
if nilai == 75:
    print("Nilai anda", nilai)

### cara 2) dengan 'is'
if nilai is 75:
    print("Nilai anda", nilai)

### NEGASI bisa dengan menggunakan '!=' atau 'is not'
if nilai != 75:
    print("Nilai anda bukan 75")

if 80 <= nilai <=100:
    print("Nilai anda A")
elif 70 <= nilai <80:
    print("Nilai anda B")
elif 60 <= nilai <70:
    print("Nilai anda C")
elif 50 <= nilai <60:
    print("Nilai anda D")
else:
    print("Anda Tidak Lulus, Nilai anda E")

print(100*"-")
### pengkondisian dalam logika list/array
### cara 1
menu = ["pecel", "semur", "sate", "gule", "rendang"]
beli = "soto"
if beli in menu:
    print("Baik,", beli ,"akan segera kami antar")
else:
    print("Maaf,",beli,"tidak ada pada menu")

### cara 2
beli2 = "sate"
if beli2 not in menu:
    print("Maaf,",beli2,"tidak ada pada menu")
else:
    print("Baik,", beli2, "akan segera kami proses")
### pengkondisian diatas bisa juga untuk memeriksa karakter dalam string maupun tipe data lain