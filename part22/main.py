### cara ke-1 untuk import modul
import modulMatematik

modulMatematik.tambah(2,9)

##########################################

### cara ke-2 untuk import modul dengan pemberian nama menggunakan "as"
import modulMatematik as math

math.tambah(3,7)

##########################################

### cara ke-3 untuk import modul yaitu dengan
### langsung memanggil fungsi spesifik yang diinginkan
from modulMatematik import kurang, tambah

kurang(6,2)
tambah(1,1)

##########################################

### cara ke-4 untuk import modul denganmengambil seluruh fungsi yang ada
from modulMatematik import *
kali(5,5)