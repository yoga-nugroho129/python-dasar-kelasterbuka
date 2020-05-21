### PERULANGAN -FOR LOOPS-

### mengambil/display data dalam list/array dengan cara iterasi
menu = ["sate", "tongseng", "rendang", "tengkleng", "soto", "es teh"]
for n in menu: ### n adalah variabel baru untuk memeriksa setiap data dalam list
    print(n)
    print(len(n))
print(150*"-")

### cara diatas/iterasi tapi digunakan untuk non list/non array
sayur = "bayem"
for n in sayur:
    print(n) ### maka string dalam "n" akan dieja

print(150*"-")

### penerapan dalam list multi-dimensional
    ### list dasar
buah = ["jeruk", "pisang", "salak", "alpukat"]
sayur = ["bayem", "sawi", "kangkung", "kubis"]
rempah = ["jahe", "kencur", "kunyit", "laos"]
    ### list dalam list/multi-dimensional
komposisi = [buah, sayur, rempah]
    ### looping
for subkomposisi in komposisi:
    print(subkomposisi) ### mencetak/meng-iterasi data dalam masing-masing list komposisi
    for isi in subkomposisi:
        print(isi) ### mencetak/mengiterasi data dalam masing-masing list (list buah, list sayur, list rempah)
