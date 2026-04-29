def menu():
    print("\n=== SISTEM TIKET PESAWAT ===")
    print("1. Lihat Rute & Harga")
    print("2. Pilih Rute & Beli Tiket")
    print("3. Keluar")

def main():
    rute = ["Jakarta-Bali", "bandung-Singapura", "inggris-jakarta"]
    harga = [1200000, 2500000, 6000000]
    
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("\n--- Daftar Rute Tersedia ---")
            for i in range(len(rute)):
                print(f"{i+1}. {rute[i]} - Rp{harga[i]}")

        elif choice == 2:
            try:
                pilih = int(input("\nPilih nomor rute (1-3): ")) - 1
                if 0 <= pilih < len(rute):
                    jumlah = int(input(f"Berapa tiket untuk {rute[pilih]}? "))
                    total = jumlah * harga[pilih]
                    print(f"Total yang harus dibayar: Rp{total}")
                else:
                    print("Rute tidak ditemukan!")
            except ValueError:
                print("Input harus berupa angka!")

        elif choice == 3:
            running = False
            print("Program selesai. Sampai jumpa!")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
