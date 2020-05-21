### Packages merupakan kumpulan dari modul-modul yyang dikumpulkan dalam 1 folder
### agar tidak menumpuk banyak didalam 1 main folder

### cara memanggil fungsi dalam package
from sains import matematika

a=matematika.kali(2,9)
print(a)

### cara memanggil lebih dari 1 modul dalam package
from sains import fisika, matematika

b = fisika.kecepatan(180,2)
print(b)

### cara lain untuk memanggil package yaitu dengan membuat file python
### __init__ sehingga semua fungsi dalam folder dapat dipanggil dengan
### cara yang lebih mudah & fleksibel

### cara pemanggilan pertama

import sains
x = sains.kali(2,2)
print(x)


### cara kedua dengan cara yg lebih spesifik
from sains import tambah

z = tambah(2,1)
print(z)

### contoh package yang telah ada secara default
### package math
import math

g = math.cos(45)
print(g)
