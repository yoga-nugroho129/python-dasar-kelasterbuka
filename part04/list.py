### list/array
### menggunakan tanda []
data = [1,2,3,4,5,6,7]

### mengkases list
subdata1 = data[2] ### mengambil data dalam list/array
subdata2 = data[-1] ### mengambil data dari kiri

### memotong list
subdata3 = data[2:4] ### mengambil data dari data ke 2 sampai data sebelum ke 4
print(subdata3) ### result [3, 4]
subdata4 = data[3:] ### mengambil data dari data ke3 sampai terakhir
subdata5 =data[:4] ### mengambil data dari awal sampai data sebelum ke 4

### menambah/menggabungkan 2 atau lebih list
data2 = [7,6,5,4,3,2,1]
tambah = data + data2

### merubah data dalam list
data2[3] = 69 ### merubah data ke 3 dengan angka 69

### merubah data dalam list dengan cara memotong/slicing
data2[3:5] = 69, 77, 44

### list dalam list/multi-dimensional list
x = [data, data2]
print(x)
### mengakses multi-dimensional list
y = x[0][4] ### mengakses list ke 0 (data) dengan mengambil isi dari data yang ke 4

### method untuk list
data2.append(99) ### menambah member dari data2

### function untuk menghitung panjang data dalam list
hitung = len(data2)
print(data2)
print(hitung)
