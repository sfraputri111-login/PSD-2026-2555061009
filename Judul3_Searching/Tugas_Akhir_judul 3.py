def sequential_search(daftar, target):
    hasil = []
    target = target.lower()
    for barang in daftar:
        if target in barang['nama'].lower():
            hasil.append(barang)
    return hasil

def main():
    data_barang = [
        {"nama": "Tas", "lokasi": "Ruang Tunggu"},
        {"nama": "Kacamata Hitam", "lokasi": "Jalan Raya"},
        {"nama": "Botol Minum", "lokasi": "Ruang Kelas"}
    ]
    
    print("=== SISTEM PENCARIAN BARANG ===")
    target = input("Cari barang apa? ").strip()
    
    if not target:
        print("Input tidak boleh kosong!")
        return
    hasil = sequential_search(data_barang, target)
    
    print("\n--- Hasil ---")
    if hasil:
        for b in hasil:
            print(f"- {b['nama']} (Lokasi: {b['lokasi']})")
    else:
        print("Barang tidak ditemukan.")

if __name__ == "__main__":
    main()
