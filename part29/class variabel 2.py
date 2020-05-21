### contoh penggunaan class variable ke 2 - COUNTER
### menghitung jumlah mahasiswa yang ada

### CLASS
class mahasiswa():

    jumlahMahasiswa = 0

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        mahasiswa.jumlahMahasiswa += 1 ### berguna sebagai penghitung jumlah
                                        ### instances yang berada dalam class

### MAIN PROGRAM
cici = mahasiswa("Cici Finansia",12660018)
yoga = mahasiswa("Yoga Nugroho", 12660020)

print(mahasiswa.jumlahMahasiswa) ### memanggil hitungan jumlah instance/mahasiswa
                                  ### yang berada dalam class mahasiswa