
number = 5
for i in range(0,20):
    print(i) ### i adalah variabel untuk pemeriksaan
    if i == number:
        print("angka", number,"ditemukan")
        break ### berfungsi sebagai break/stop ketika aksi dalam if telah dilakukan
else:
    print("angka", number,"tidak ditemukan") ### jika kondisi dalam looping tidak terjadi


