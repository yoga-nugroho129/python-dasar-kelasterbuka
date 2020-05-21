### variable dalam class
def garis():
    print(50*"=")

garis()
print("CONTOH CLASS VARIABEL #1")
garis()

class mahasiswa():

    jurusan = "Teknik Industri" ### baris ini bisa disebut sebagai variabel milik class mahasiswa

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim

yoga = mahasiswa("Yoga Nugroho", 12660020)

cici = mahasiswa("Cici Finansia", 12660018)
print(cici.nama, "- NIM", cici.nim, "- Jurusan", cici.jurusan)

### tanpa adanya self.jurusan di dalam method maka jurusan akan default
### sesuai dengan variable jurusan dalam class
### namun jika dilakukan operasi dibawah maka...

yoga.jurusan = "Teknik Rahasia"
print(yoga.nama, yoga.jurusan) ### ...maka jurusan milik yoga akan ditimpa oleh jurusan
                                ### yang telah ditetapkan secara manual atas nama yoga

