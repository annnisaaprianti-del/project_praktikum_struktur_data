class Vector:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.data = [None] * self.capacity

    def resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data

    def push_back(self, value):
        if self.length == self.capacity:
            self.resize()
        self.data[self.length] = value
        self.length += 1

    def display(self):
        if self.length == 0:
            print("Belum ada step make up.")
        else:
            for i in range(self.length):
                print(f"Step {i+1}: {self.data[i]}")

    def total_pump(self):
        total = 0
        for i in range(self.length):
            step = self.data[i].split("-")
            if len(step) > 1:
                try:
                    total += int(step[1])
                except:
                    pass
        return total


# program utama
v = Vector()

while True:
    print("\n1. Tambah step make up")
    print("2. Tampilkan step")
    print("3. Total pump")
    print("4. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        produk = input("Nama make up: ")
        jumlah = input("Berapa pump: ")
        step = produk + "-" + jumlah
        v.push_back(step)

    elif pilihan == "2":
        v.display()

    elif pilihan == "3":
        print("Total pump make up:", v.total_pump())

    elif pilihan == "4":
        print("Selesai.")
        break

    else:
        print("Pilihan salah!")