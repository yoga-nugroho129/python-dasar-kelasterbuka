### INPUT OUTPUT FILE

### MEMBUAT FILE DENGAN MENGGUNAKAN PYTHON

"""
ATURAN/MODE DALAM MANIPULASI FILE DENGAN PYTHON
    1) w = WRITE MODE/CREATE FILE : akan menulis dengan menimpa isi dari file lama/membuat             file baru jika file belum ada
    2) r = READ ONLY MODE : hanya membaca isi dari file
    3) a = APPEDNDING MODE :menambahkan data di akhir baris
    4) r+ = READ + WRITE MODE
"""

### CONTOH PENGGUNAAN UNTUK FILE DENGAN NAMA "data.txt"

### Fungsi "w"
file = open("data.txt","w") # pembuatan variabel dengan nama "file" khusus aktivitas "w"

file.write("ini adalah file txt yang dibuat dengan Python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close() #wajib close file.. setelah di Run maka akan muncul file txt dalam folder

################################################
################################################


### Funfsi "r"
bacaFile = open("data.txt", "r")

### cara baca file
baca = bacaFile.read() # pembacaan isi file, jika dalam () diisi angka maka jumlah karakter sesuai angka tersebut yang akan ditampilkan
print(baca)

print(25 * "-")

bacaFile.close()

################################################
################################################

### Fungsi "a"
cobaAppend = open("data.txt","a")

cobaAppend.write("\nbaris ini ditambahkan dengan mode append")

cobaAppend.close()