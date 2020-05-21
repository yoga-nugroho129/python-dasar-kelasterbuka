### membuat GUI sederhana dengan menggunakan pakcage tkinter

import tkinter

jendelaUtama = tkinter.Tk() ### biasanya nama variabel dengan nama "root"

#### membuat fungsi ketika tombol ditekan
def tombolDitekan():
    hasilTombol = tkinter.Label(jendelaUtama, text = "Tombol ditekan \[^-^]/")
    hasilTombol.pack()


### membuat tulisan dalam GUI
isi = tkinter.Label(jendelaUtama, text = "Ini adalah text didalam \n GUI sederhana")

### membuat tombol/button didalam GUI
tombol = tkinter.Button(jendelaUtama, text = "Ini Tombol!", command = tombolDitekan)


### menampilkan/memanggil tulisan yang telah dibuat diatas ke dalam GUI
isi.pack()
### memanggil tombol kedalam GUI
tombol.pack()

jendelaUtama.mainloop() ### syntax untuk memanggil jendela/window