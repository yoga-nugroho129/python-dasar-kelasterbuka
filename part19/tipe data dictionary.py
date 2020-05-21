### rekap

list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}

#########################

### tipe data Dictionary
### merupakan struktur data asosiatif/mapping
### dengan format =
### member1 = {keyword1:value1,keyword2:value2,dst..}

member1 = {"ID":101,
          "nama":"Cici",
          "umur":24,
          "pekerjaan":"dosen"
          }
### mencetak dictionary secara keseluruhan
print(member1)

### mencetak dictionary berdasarkan key-nya
print(member1["umur"])

### mencetak key-key yang ada
print(member1.keys())

### mencetak value-value yang ada
print(member1.values())

### mencetak data per item
print(member1.items())

print(100*"=")
### membuat dictionary agar masuk ekdalam list => seperti fungsi database
member2 = {"ID":102,
           "nama":"Yoga",
           "umur":24,
           "pekerjaan":"Karyawan"}

### menyatukan 2 member yang sudah ada
daftarMember = {"Cici":member1,"Yoga":member2}
### memanggil data dalam database-dictionary daftarMember
print(daftarMember["Cici"])