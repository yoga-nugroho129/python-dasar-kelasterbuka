def garis():
    print(100*"=")
garis()

### digunakan untuk data yanag sifatnya FIX
### Contoh : data identitas (No. KTP, Tgl Lahir, Dll.)
################################################################################
### data tuple merupakan data yang lebih RINGAN untuk diproses daripada list
### bisa dicek dengan import sys

import sys

dataList = [1,2,3,4,5, "kantong", "sendal", 4, 5, 6, 7, 8, 9, "kresek", "mandi", "odol", 3.14, True]
dataTuple = (1,2,3,4,5, "kantong", "sendal", 4, 5, 6, 7, 8, 9, "kresek", "mandi", "odol", 3.14, True)

besarDataList = sys.getsizeof(dataList)
print("Ukuran data list =",besarDataList)

besarDataTuple = sys.getsizeof(dataTuple)
print("Ukuran data tuple =", besarDataTuple)

### semakin besar data maka semakin signifikan perbedaan ukuran yang ada

garis()

### pengecekan kebutuhan waktu running code
### menggunakan import timeit
import timeit

waktuList = timeit.timeit(stmt="[1,2,3, 'sendok', 'piring',3.14]")
print("Waktu untuk memproses list =", waktuList)

waktuTuple = timeit.timeit(stmt="(1,2,3, 'sendok', 'piring',3.14)")
print("Waktu untuk memproses tuple =",waktuTuple)

### pemrosesan dengan menggunakan tuple kurang lebih 10x LEBIH CEPAT dari pada List