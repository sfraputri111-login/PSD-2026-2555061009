class Node:
    def __init__(self, key, kegiatan):
        self.key = key            
        self.kegiatan = kegiatan  
        self.left = None
        self.right = None

class SistemJadwalBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, kegiatan):
        if root is None:
            return Node(key, kegiatan)
        if key < root.key:
            root.left = self.insert_node(root.left, key, kegiatan)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, kegiatan)
        else:
            print(f"\n Jam {self.format_jam(key)} sudah ada agenda. Mengubah menjadi: {kegiatan}")
            root.kegiatan = kegiatan
        return root

    def insert(self, key, kegiatan):
        self.root = self.insert_node(self.root, key, kegiatan)

    def search_node(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def cetak_kronologis(self, root):
        if root is None:
            return
        self.cetak_kronologis(root.left)
        print(f" {self.format_jam(root.key)} -> {root.kegiatan}")
        self.cetak_kronologis(root.right)

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def format_jam(self, key):
        return f"{key // 100:02d}:{key % 100:02d}"

def main():
    bst = SistemJadwalBST()
    pilih = 0
    while pilih != 7:
        print("\n=== SISTEM JADWAL HARIAN (BST) ===")
        print("1. Tambah Jadwal")
        print("2. Cari Jadwal")
        print("3. Lihat Agenda Hari Ini (Urut Waktu)")
        print("4. Agenda Paling Pagi & Paling Malam")
        print("5. Hitung Total Kegiatan")
        print("6. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print(" Input tidak valid! Masukkan angka.")
            continue
            
        if pilih == 1:
            try:
                jam = int(input("Masukkan Jam (0-23)  : "))
                menit = int(input("Masukkan Menit (0-59): "))
                if not (0 <= jam <= 23 and 0 <= menit <= 59):
                    print(" Format waktu salah!")
                    continue
                
                key_waktu = (jam * 100) + menit
                kegiatan = input("Nama Kegiatan/Agenda : ")
                bst.insert(key_waktu, kegiatan)
                print(f" Jadwal disimpan untuk pukul {bst.format_jam(key_waktu)}")
            except ValueError:
                print(" Input harus berupa angka!")
                
        elif pilih == 2:
            try:
                jam = int(input("Cari Jam   : "))
                menit = int(input("Cari Menit : "))
                key_waktu = (jam * 100) + menit
                
                hasil = bst.search(key_waktu)
                if hasil:
                    print(f" Ditemukan! Agenda pukul {bst.format_jam(hasil.key)} adalah: {hasil.kegiatan}")
                else:
                    print(" Tidak ada agenda di jam tersebut.")
            except ValueError:
                print(" Input tidak valid!")
                
        elif pilih == 3:
            print("\n AGENDA HARI INI (KRONOLOGIS):")
            if bst.root is None:
                print("(Belum ada jadwal harian)")
            else:
                bst.cetak_kronologis(bst.root)
            
        elif pilih == 4:
            node_min = bst.find_min(bst.root)
            node_max = bst.find_max(bst.root)
            if node_min:
                print(f" Paling awal : [{bst.format_jam(node_min.key)}] {node_min.kegiatan}")
                print(f" Paling akhir: [{bst.format_jam(node_max.key)}] {node_max.kegiatan}")
            else:
                print(" Belum ada jadwal.")
                
        elif pilih == 5:
            print(f" Total kegiatan hari ini: {bst.count_nodes(bst.root)} agenda")

        elif pilih == 6:
            print("Program selesai. Semoga harimu produktif!")
            break
        else:
            print(" Pilihan tidak valid!")

if __name__ == "__main__":
    main()
