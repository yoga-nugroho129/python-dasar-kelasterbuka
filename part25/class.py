### Class dalam python (bisa disebut template/blue-print)
### berfungsi dalam program dengan teknik object oriented (OOP)
### sehingga fungsi-fungsi dapat dengan mudah di tempelkan pada object-object
### tanpa perlu mengulang untuk membuat fungsi-fungsi secara berulang-ulang
### class bisa disebut juga sebagai instance
### di dalam class ada instance-instance (instances)
### di dalam 1 class bisa terdiri dari banyak instance yang memiliki template sesuai class-nya

################### BARIS CLASS ###################
class mahasiswa():
    pass ### untuk membuat class/template yang kosong dapat diisi dengan "pass"

### object dalam class diatas
cici = mahasiswa() ### object pertama dengan instance "cici" dalam class "mahasiswa"
yoga = mahasiswa() ### instance dalam class mahasiswa dapat sebanyak banyaknya

print(cici)

print(100 * "=")

### contoh class kedua
class mobil():
    tipe = "city car" ### bisa disebut atribut

    ###>part26 penambahan function di dalam class bisa disebut sebagai method
    def klakson(self):
        print("mobil berbunyi")

    ### method kedua dengan identifier pelaku/instance
    def maju(self):
        print(self.tipe, "bergerak maju")

    ### method ketiga dengan tambahan aksi tambahan
    def mundur(self,aksi):
        print(self.tipe,"bergerak mundur",aksi)

honda = mobil() ### merupakan instanciate
toyota = mobil()

print(toyota.tipe) ### ketika di print maka menghasilkan isian pada tipe

honda.tipe = "Honda cr-v" ### jika dirubah maka
print(honda.tipe) ### ketika di print akan menghasilkan isian sesuai perubahan diatas

print(100*"=")

###>part26... memanggil hasil dari fungsi/method yang telaha disisipkan diatas
honda.klakson() ### cara ini akan menghasilkan aksi dari fungsi yang dibuat
toyota.klakson() ### namun cara hasil dari teknik ini tidak akan diketahui instance mana
                  ### yang melakukan tindakan didalam fungsi maka
                   ### peran self dapat digunakan sesuai di mthod kedua (diatas)
print(100*"=")

### contoh pemanggilan fungsi kedua dengan identifier instance
honda.maju()
toyota.maju()

print(100*"=")

### contoh pemanggilan fungsi ketiga dengan adanya pendambahan aksi dalam fungsinya
honda.mundur("perlahan")
toyota.mundur("pelan-pelan")

print(100*"=")


