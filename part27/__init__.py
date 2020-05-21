### __init__ dalam class

### Baris Class
class mobil():
    tipe = "merk" ### atribut dalam class
### method
    def __init__(self):
        print("ini adalah init")

    def maju(self):
        print(self.tipe, "bergerak maju")

### baris instances
honda = mobil() ### dari baris ini,, function/method __init__ akan langsung dieksekusi (berjalan tanpa perlu dieksekusi)
#toyota = mobil() ### ini berguna ketika dibutuhkan atribut yang langsung dirubah ketika instenciate class

honda.tipe = "city car"

### lanjut ke file __init__2