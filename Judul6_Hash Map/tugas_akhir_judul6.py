class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\n RESERVASI KURSI BIOSKOP ")
        for i in range(self.SIZE):
            print(f"Baris {i:2}: ", end="")
            current = self.table[i]
            if current is None:
                print("KOSONG")
            else:
                while current is not None:
                    print(f"[Kursi:{current.key}, Nama:{current.value}] -> ", end="")
                    current = current.next
                print("NULL")

def main():
    bioskop = SeparateChaining(10)
    
    pilih = 0
    while pilih != 4:
        print("\n RESERVASI BIOSKOP ")
        print("1. Lihat Denah Kursi")
        print("2. Pesan/Update Kursi")
        print("3. Batalkan Pesanan")
        print("4. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            bioskop.display()
            
        elif pilih == 2:
            try:
                nomor = int(input("Masukkan nomor kursi: "))
                nama = input("Masukkan nama pemesan: ")
                bioskop.insert(nomor, nama)
                print(f"Kursi {nomor} telah dipesan atas nama {nama}.")
            except ValueError:
                print("Nomor kursi harus angka!")
                
        elif pilih == 3:
            try:
                nomor = int(input("Masukkan nomor kursi yang ingin dibatalkan: "))
                if bioskop.remove_key(nomor):
                    print(f" Pesanan kursi {nomor} telah dibatalkan.")
                else:
                    print(f"Kursi {nomor} tidak ditemukan.")
            except ValueError:
                print("Nomor kursi harus angka!")
                
        elif pilih == 4:
            print("Terima kasih!")
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
