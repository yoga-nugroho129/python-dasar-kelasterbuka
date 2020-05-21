### menggunakan eksternal package yaitu numpy
import numpy as np

a = np.array([1,2,3,4])

print(a) ### menghasilkan array dengan format matrix-vector

b = np.array([4,3,2,1])

c = a * b ### sehingga c merupakan perhitungan dengan aturan perhitungan matrix
print(c)

print(30*"=")

######################################################################
######################################################################

### menggunakan eksternal package Pillow untuk pengolahan file gambar

from PIL import Image

gambar = Image.open("Tawheed.jpg")

print("Format gambar :", gambar.format)
print("Ukuran gambar :", str(gambar.size))

gambar.show()

