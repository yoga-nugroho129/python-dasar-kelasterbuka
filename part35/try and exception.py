### TRY dan EXCEPTION digunakan sebagai ERROR HANDLING
### jenis error ada 2
### 1) Syntax Error = error yg dapat dideteksi oleh interpreter/program
###                 CONTOH = print("halo..) => error karena kurang karakter (")
### 2) Error Runtime = error yang tidak dapat dideteksi oleh program
###                 CONTOH = error ketika membagi string dengan interger

### dengan TRY & EXCEPTION dapat dilakukan error handling

### CONTOH PENERAPAN =
### [1]
try:
    a = 1
    b = 0
    c = a/b
except:
    print("Tidak bisa membagi angka dengan nol") ### error akan ditangkap oleh except

print("=" * 30)


### [2] Mendeteksi apakah yang diinput angka maupun interger
while True:
    try:
        angka = int(input("Masukan angka :\n"))
        break ### untuk keluar dari infinite-loop ketika kondisi input angka terpenuhi
    except:
        print("masukan data berupa angka saja\n"+20 * "-")

print("Angka anda adalah",angka,"\nProgram #1 telah ditutup")
print("--" * 10)

### [3] Mengatasi error lebih dari 1 jenis dengan bahasa yang kita atur melaui print
while True:
    try:
        pembilang = int(input("Masukan bilangan Pembilang ="))
        penyebut = int(input("Masukan bilangan Penyebut ="))
        hasil = pembilang/penyebut
        break
    except ZeroDivisionError: ### khusus untuk error jika dibagi dengan nol
        print("Bilangan penyebut tidak bisa nol\n",10*"-")
    except ValueError:
        print("Masukan data berupa angka saja\n",10*"-")

print("Hasil pembagian", pembilang,"dan",penyebut," adalah",hasil,"\nProgram #2 telah ditutup")
print("--" * 10)


### [4] Mengatasi banyak error dengan bahasa asli dari python (Cocok untuk Debugging)
while True:
    try:
        pembilang = int(input("Masukan bilangan Pembilang = "))
        penyebut = int(input("Masukan bilangan Penyebut = "))
        hasil = pembilang/penyebut
        break

    except Exception as err: ### pendefinisian "err" sebagai error yang ditampilkan
        print(err)

print(hasil)

"""
Jenis-jenis ERROR dalam Python :
1) IOError = untuk catch error ketika proses input/output
2) ImportError = ketika mengimport package yang tidak/belum dimiliki
3) ValueError
4) Division by Zero
5) KeyboardInterupted
6) EOFError
"""