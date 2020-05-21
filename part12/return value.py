### fungsi dengan return value
### berfungsi ketika fungsi yang dibuat akan digunukan sebagai alat penghitung/value
### yang digunakan berkali-kali

def garis():
    print(100*"=")
garis()

### pemanggilan dengan argumen biasa
def kuadrat(n):
    hasil = n**2
    print ("Hasil kuadrat dari", n, "adalah", hasil)

kuadrat(3)
a = kuadrat(3) ### fungsi kuadrat tidak bisa dipanggil dengan menjadikannya sebagai variabel
print(a) ### menghasilkan output None

garis()

### pemanggilan dengan argumen return
def pangkatdua(n):
    output = n**2
    print ("Hasil kuadrat dari", n, "adalah", output)
    return output ### aksi dalam output dipanggil ulang/di return sehingga fungsi
                  ### penugasan pada variabel dibawah dapat dilakukan
                  ### namun dengan hasil display sesuai dengan aksi dalam output saja (n**2)

a = pangkatdua(3)
### cara 1
print(a)

### cara 2
print(pangkatdua(5))
garis()

### fungsi dengan return value dan multiple argumen
### Contoh fungsi penambahan
def tambah(argumen1, argumen2):
    hasil = argumen1 + argumen2
    print("Hasil penjumlahan dari", argumen1, "dan", argumen2, "adalah", hasil)
    return hasil

def kali(argumen1, argumen2):
    hasil = argumen1 * argumen2
    print("Hasil perkalian dari", argumen1, "dan", argumen2, "adalah", hasil)
    return hasil

a = tambah(9,7)
print(a)

b = kali(6,7)
print(b)

c = a + b ### bisa dipanggil kapanpun dimanapun
print(c)








