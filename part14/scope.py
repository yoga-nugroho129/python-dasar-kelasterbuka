### scope local dan scope global

### mendefinisikan sebuah variabel
namaDesa = "Gempol"

def rubahDesa(namaBaru):
    global namaDesa #agar fungsi dapat mengakses data variabel diluar fungsi(def)
    namaDesa = namaBaru
    print("Alamat desa pindah ke", namaBaru)

rubahDesa("Bareng")
print("Alamat sekarang di", namaDesa) ### jika tidak ada global diatas maka namaDesa
                                      ### akan tetap menjadi Gempol