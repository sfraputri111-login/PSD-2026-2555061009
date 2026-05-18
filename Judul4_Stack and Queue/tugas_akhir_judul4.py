class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"Enqueue {x} berhasil")

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return
        temp = self.front_ptr
        print(f"Dequeue {temp.data} berhasil")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print(f"Elemen depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print("Isi queue (depan ke belakang): ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    queue = QueueLinkedList()
    counter_antrean = 0 
    pilih = 0
    
    while pilih != 5:
        print("\n====================================")
        print("     SISTEM ANTREAN BANK MANDIRI    ")
        print("====================================")
        print("1. Ambil Nomor Antrean (Enqueue)")
        print("2. Panggil Nasabah ke Teller (Dequeue)")
        print("3. Lihat Antrean Terdepan (Peek)")
        print("4. Cetak Seluruh Daftar Antrean (Display)")
        print("5. Tutup Bank & Keluar Program")
        print("------------------------------------")
        
        try:
            pilih = int(input("Pilih Menu (1-5): "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue
            
        if pilih == 1:
            nama_nasabah = input("Masukkan Nama Nasabah: ")
            if nama_nasabah.strip() == "":
                print("Nama tidak boleh kosong!")
                continue
                
            counter_antrean += 1
            data_sistem = f"[B-{counter_antrean:03d} | {nama_nasabah}]"
            print("\n[PROSES ENQUEUE]")
            queue.enqueue(data_sistem)
            
        elif pilih == 2:
            print("\n[PROSES DEQUEUE]")
            if queue.is_empty():
                queue.dequeue() 
            else:
                print(">>> PANGGILAN KEPADA NASAHAB: <<<")
                queue.dequeue()
                print("Silakan menuju ke Teller 1.")
                
        elif pilih == 3:
            print("\n[PROSES PEEK]")
            queue.peek()  
        elif pilih == 4:
            print("\n[PROSES DISPLAY]")
            queue.display()
        elif pilih == 5:
            print("\n[SISTEM DIKOSONGKAN SEBELUM KELUAR]")
            while not queue.is_empty():
                queue.dequeue()
            print("Sistem dimatikan. Terima kasih.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
