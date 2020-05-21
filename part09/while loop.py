
### Struktur While Loop
### while ...argumen...:
###     ...aksi...
###

angka = 1
while angka <= 5 :
    print(angka)
    angka = angka + 1

print("diluar while")
print(150*"-")

### contoh dengan boolean
start = True
angka = 0
while start:
    print("Mencari angka...")
    if angka == 5:
        start = False
        print("Angka ditemukan = 5")
    angka += 1
print("diluar loop")

print(150*"=")
