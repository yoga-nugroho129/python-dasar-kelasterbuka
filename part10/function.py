### fungsi garis pembatas
def garis():
    print(100 * "=")
garis()

### cara mendefinisikan/menyatakan fungsi
def fungsi():
    print("Ini adalah baris fungsi")
### cara memanggil fungsi
fungsi()

garis()

### memanggil fungsi menggunakan fungsi
def merk():
    print("DAIHATSU")

def type():
    merk() ### memanggil fungsi sebelumnya didalam fungsi
    print("Expander")

type()

garis()

### fungsi dengan input-argumen dengan format ... def namafungsi(input_argumen):
def bayar(unit):
    type()
    harga = 150000000
    total = harga*unit
    print("Harga", unit, "unit mobil adalah Rp.", total, ",-")

bayar(4)

garis()

