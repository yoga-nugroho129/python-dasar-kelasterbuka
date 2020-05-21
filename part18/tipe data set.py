### set = himpunan.. menggunakan tanda {...}
### himpinan mempunyai sifat acak,
### contoh set

mobil = {"civic", "kijang", "baleno", "xenia", "Expander"}
print("Data awal adalah",mobil)

mobil.add("HR-V")
print("Data baru adalah",mobil)
### data yang masuk akan berubah-ubah posisi karena himpunan bersifat acak

mobil.add("kijang")
print("Data baru adalah",mobil)
### serta data tipe set/himpunan tidak akan menduplikasi data yang sudah ada
### seperti data merk kijang diatas yang sudah ada sebelumnya

print(100*"=")

### penulisan tipe data set dengan cara lain
motor = set()

motor.add("beat")
motor.add("mio")
motor.add("supra x")
motor.add("vario")
motor.add("jupiter mx")
motor.add(567) ### dapat juga berisi data dengan tipe yang berbeda

print(motor) ### data acak
#print(sorted(motor)) ### data dengan diurutkan dengan syarat tipe data sama

print(100*"=")

### dengan tipe Himpunan maka dapat dilakukan operasi khusus himpunan/set
genap = {2,4,6,8}
ganjil = {1,3,5,7,9}
prima = {2,3,5,7,11}
### operasi union/gabungan
print(ganjil.union(prima))
### operasi irisan/intersection
print(prima.intersection(genap))




