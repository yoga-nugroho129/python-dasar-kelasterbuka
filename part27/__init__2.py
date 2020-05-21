### sehingga dari fungsi __init__ yang sebelumnya,,
### maka untuk atribut tipe dapat dilakukan seperti berikut agar bisa langsung dieksekusi
class mobil():

    def __init__(self, input_tipe):
        self.tipe = input_tipe

### instances
honda = mobil("city car")
toyota = mobil("sport car")

### maka pemanggilan tipenya yaitu
print(honda.tipe)