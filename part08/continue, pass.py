for i in range(0,10):
    if i == 6:
        print("angka",i,"ditemukan")
        #break ### untuk menghentikan ketika kondisi tercapai
        #continue ### untuk melanjutkan ke step berikutnya
    print("Sekarang angka",i)

print(150*"-")

for i in range(0,10):
    if i == 6:
        print("angka",i,"ditemukan")
        pass ### hanya akan dilewati saja
        print("Cek",i)
    print("Sekarang angka", i)