### garis
def garis():
    print(100*"=")

garis()

### fungsi menggunakan argumen sederhana
def siswa(nama):
    print("Nama siswa berikut adalah", nama)
siswa("Cici")

garis()

### fungsi dengan argumen menggunakan keyword
def datasiswa(nama,asal):
    print("Siswa bernama",nama,"berasal dari",asal)

datasiswa(nama = "Cici", asal="Batam") ### pemanggilan harus dengan keywordnya
datasiswa(asal="Klaten", nama="Yoga" ) ### pemanggilan boleh tidak urut asal sesuai keyword

garis()

### fungsi dengan argumen DEFAULT
def datamhs(nama, asal, jurusan="Teknik Industri", kampus="UGM"): ### jurusan dengan isian default
    print("Mahasiswa atas nama", nama,"Berasal dari", asal)
    print("merupakan mahasiswa Program Studi", jurusan, "di Kampus", kampus)

### CATATAN = dalam pendefinisian argumen-input, yg memiliki nilai default
###           harus berada di akhir argumen seperti fungsi datamhs diatas

datamhs(nama="Cici", asal="Batam") ### memanggil dengan default
garis()
datamhs(asal="Klaten", nama="Yoga", kampus="UPN") ### memanggil dengan default yg dirubah

