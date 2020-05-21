### fungsi __init__ yang sebelumnya merupakan fungsi
### yang dapat dirubah dengan mudah/tidak private/public
### sehingga dapat dengan mudah untuk sistem yang dirancang diserang hacker
### sehingga diperlukan sebuah atribut private guna memproteksi tindakan-tindakan
### perubahan oleh hacker karena kondisi sistem yang terbuka/public

### PRIVATE ATTRIBUTE ###
def garis2():
    print(100 * "=")

garis2()
print("PRIVATE ATTRIBUTE")
garis2()

### class
class mahasiswa():

    nilai = 0 ### atribut nilai mahasiswa

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama # public
        self.nim = inputNim # public

    def membaca(self, aksi):
        print(self.nama, "dengan NIM", self.nim, "sedang membaca", aksi)

    def nilaiAkhir(self,inputNilai):
        self.__nilai = inputNilai ### fungsi dari karakter "__" adalah sebagai private attribute
        if self.__nilai >=65:
            print(self.nama,"NIM", self.nim, "mendapat nilai", self.__nilai, "dan LULUS")
        else:
            print(self.nama,"NIM", self.nim, "mendapat nilai", self.__nilai, "dan TIDAK LULUS")

### instances & main program
yoga = mahasiswa("Nugroho", 12660020)

cici = mahasiswa("Cici",12660018)
cici.membaca("optimisasi")

### dengan cara dibawah ini maka atribut-atribut pada mahasiswa dapat diganti isinya
cici = mahasiswa("Finansia", 12660081)
cici.membaca("ergonomi")

### sehingga untuk beberapa atribut agar aman diperlukan adanya private attribute
### cek atribut "nilai" diatas |^|^|^|

garis2()

### pemanggilan private attribute
cici.nilaiAkhir(55) ### dengan cara ini maka nilai tidak dapat dirubah secara
yoga.nilaiAkhir(90)







