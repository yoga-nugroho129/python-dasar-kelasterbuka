def garis():
    print(100*"=")
garis()

### list tingkat lanjutan
makanan = ["roti", "kue", "sate", "jeruk"]
print(makanan)
garis()

### cara menambah data dalam list
makanan.append("puding")
print(makanan)
garis()

### sting dalam python adalah data yg iterabel contoh
data = "coba"
for i in data:
    print(i)
garis()

### dapat juga di extend
makanan.extend("saus")
print(makanan)
garis()

### cara menambah data dalam list dengan urutan/posisi tertentu
makanan.insert(1,"botol")
print(makanan)
garis()

 ### cara untuk menghitung data dalam list dengan kriteria nama
jumlahBotol = makanan.count("botol")
print(jumlahBotol)
garis()

### me-remove data
makanan.remove("botol")
print(makanan)
garis()

### mengubah urutan
makanan.reverse()
print(makanan)

garis()
### membuat copy/clone dari list agar tidak mengubah data asli
food = makanan.copy()
food.append("potato")
print(food)
print(makanan)
