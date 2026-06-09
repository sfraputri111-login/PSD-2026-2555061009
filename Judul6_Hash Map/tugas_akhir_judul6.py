class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
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
        print("\n KURSI BIOSKOP ")
        for i in range(self.SIZE):
            print(f"Baris/Indeks {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("KOSONG")
            while current is not None:
                print(f"[Kursi: {current.key}, Nama: {current.value}] -> ", end="")
                current = current.next
            print("NULL")
            
def main():
    bioskop = HashMapSeparateChaining(10)

    bioskop.insert(1, "Ibnu")
    bioskop.insert(11, "Maryam")   
    bioskop.insert(21, "Andi")   
    bioskop.insert(2, "Siska")

    pilih = 0
    while pilih != 2:
        print("\n MENU RESERVASI BIOSKOP ")
        print("1. Cek & Kelola Reservasi")
        print("2. Keluar")
        
        try:
            pilih = int(input("Masukkan pilihan Anda: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            bioskop.display()
            try:
                nomor_kursi = int(input("\nMasukkan nomor kursi yang ingin dikelola: "))
                hasil = bioskop.search(nomor_kursi)
                
                if hasil:
                    print(f"\n[INFO] Kursi {nomor_kursi} dipesan oleh: {hasil.value}")
                    konfirmasi = input("Apakah ingin membatalkan pesanan ini? (ya/tidak): ")
                    if konfirmasi.lower() == 'ya':
                        bioskop.remove_key(nomor_kursi)
                        print(f"[ACTION] Pesanan {nomor_kursi} dibatalkan.")
                        bioskop.display() 
                else:
                    print(f"\n[INFO] Kursi {nomor_kursi} kosong.")
            except ValueError:
                print("Input harus angka!")
                
        elif pilih == 2:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
