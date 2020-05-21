### Looping dengan cara yang berbeda dari cara looping conventional ####

def garis():
    print(100 * "=")
garis()

### data list untuk di loop
namaHewan = ["kucing", "semut", "ikan", "kelinci"]

### Looping dengan cara standard
print("Looping cara STANDARD")
print(50*"- ")
i = 0
for hewan in namaHewan:
    print("urutan (", i ,") adalah", hewan)
    i +=1

garis()

### Looping dengan cara ENUMERATE
print("Looping dengan cara ENUMERATE")
print(50*"- ")
for i, hewan in enumerate(namaHewan):
    print("peringkat (", i ,") adalah", hewan)

garis()

### menggabungkan list dengan zip

### data list ke 2
warnaHewan = ["putih", "hitam", "kuning", "cokelat"]

### fungsi zip
### isi dari list harus memiliki jumlah yang sama agar bisa dipanggil secara berpasangan
print("Penggabungan isi 2 list dengan ZIP")
print(50*"- ")
for hewan, warna in zip(namaHewan,warnaHewan):
    print("binatang", hewan, "itu berwarna", warna)

garis()

### penerapan pada tipe data set/himpunan bisa ditambahkan syntax sorted agar tidak acak

### penerapan pada tipe data Dictionary
binatang = {"kucing":"putih",
           "semut":"merah",
           "burung":"hijau"}
### menampilkan key-nya saja
for bi in binatang.keys():
    print(bi)
print(50*"-")

### menampilkan value-nya saja
for bi in binatang.values():
    print(bi)
print(50*"-")

### menampilkan sebagai item(lengkap)
for bi in binatang.items():
    print(bi)
print(50*"-")

### menampilkan sebagai item(lengkap) dengan pemisahan isi
for bi,wrn in binatang.items():
    print(bi,"berwarna", wrn)
print(50*"-")


