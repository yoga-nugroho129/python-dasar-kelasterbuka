print(25 * "=")
print("BASIC INHERITANCE")
print(25 * "=")

### CLASS
class Ojek(): ### penulisan nama class lebih baik diawali huruf kapital untuk memudahkan

    def __init__(self, nama, motor, daerahOperasional):
        self.nama = nama
        self.motor = motor
        self.daerah = daerahOperasional

    def dataDriver(self):
        print("Nama :", self.nama, "\nKendaraan :", self.motor, "\nDaerah Operasional :", self.daerah)

### CLASS CLONE DARI CLASS Ojek menjadi data Gojek
class Gojek(Ojek):
    def dataDriver(self):
        print("Driver atas nama", self.nama, "bisa dilihat di aplikasi")




### instances
ojek1 = Ojek("Paijo", "Mio", "Sleman Selatan")
ojek2 = Ojek("Parjo", "MegaPro", "Bantul")

### data instances untuk class Gojek yang menggunakan inheritance
ojek3 =Gojek("Suparman", "Supra", "aplikasi")

### pemanggilan data driver dengan class ojek
ojek1.dataDriver()
print(25 * "-")
ojek2.dataDriver()
print(25 * "-")

### pemanggiflan data driver Gojek hasil dari class dengan inhertitance dari class Ojek
ojek3.dataDriver()


#############################################################################
### DARI CLASS OJEK, MAKA JIKA DALAM PEMBUATAN CLASS YANG SEJENIS ###
### CONTOH GOJEK, MAKA BISA DILAKUKAN "INHERITANCE" ATAU FUNGSI ###
### UNTUK MEWARISKAN YANG ADA DALAM CLASS SEBELUMNYA ###

