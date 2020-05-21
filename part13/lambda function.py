def garis():
    print(100*"=")
garis()

### fungsi dengan syntax standard
def jumlah(a,b):
    c = a + b
    return c

hasil = jumlah(4,5)
print(hasil)

garis()

### membuat fungsi dengan lambda
### syntax sederhana =
### namafungsi = lambda argumen: aksi
kali = lambda a, b: a * b
hasil = kali(2,3)
print(hasil)
