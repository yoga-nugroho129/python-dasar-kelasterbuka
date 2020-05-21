### syntax stack berfungsi untuk kasus seperti tumpukan (FILO)
### syntax queue berfungsi untuk kasus antrian kasir (FIFO)

def garis():
    print(100*"=")

garis()

### contoh penggunaan stack
print("CONTOH STACK")
garis()
dataStack = [1,2,3,4,5]
print("data awal yaitu", dataStack)

dataStack.append(6)
print("tambahan data masuk menjadi", dataStack)

dataStack.append(7)
print("tambahan data masuk menjadi", dataStack)
print(100*"-")

### fungsi pop berfungsi untuk menghilangkan data yang apling baru masuk

dataStack.pop()
print("data setelah di-pop menjadi", dataStack)

dataStack.pop()
print("data setelah di-pop menjadi", dataStack)

garis()

### contoh penggunaan queue
### penggunaan queue harus menggunakan module (import fungsi dari library luar yaitu deque)
from collections import deque
print("CONTOH QUEUE")

def garis():
    print(100*"=")

dataQueue = deque([1,2,3,4,5])

garis()

print("Data awal yaitu ", dataQueue)

dataQueue.append(6)
print("Data baru masuk",6,"sehingga data menjadi", dataQueue)

dataQueue.append(7)
print("Data baru masuk",7,"sehingga data menjadi", dataQueue)

dataQueue.append(8)
print("Data baru masuk",8,"sehingga data menjadi", dataQueue)

print(100*"-")
### fungsi untuk menghilangkan data yang paling kiri yaitu dengan
### fungsi dari deque berupa .popleft

dataQueue.popleft()
print("Data telah di-popleft,",1,"sehingga menjadi", dataQueue)

dataQueue.popleft()
print("Data telah di-popleft,",2,"sehingga menjadi", dataQueue)

dataQueue.popleft()
print("Data telah di-popleft,",3,"sehingga menjadi", dataQueue)
