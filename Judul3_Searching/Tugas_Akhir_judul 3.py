def cari_barang_hilang(daftar_barang, n, target):
    i = 0
    hasil = [] 
    target = target.lower()
    
    while i < n:
        if target in daftar_barang[i]['nama'].lower():
            hasil.append(daftar_barang[i])
        i += 1
    return hasil

def main():
    data_barang = [
        {"nama": "Kunci Motor Honda", "lokasi": "Di taman"},
        {"nama": "Kacamata Hitam", "lokasi": "di Jalan Raya"},
        {"nama": "Tumblr Biru", "lokasi": "Kantin"},
        {"nama": "Botol Minum", "lokasi": "Ruang kelas 1.2"},
        {"nama": "Helm", "lokasi": "Parkiran Gedung"},
        {"nama": "Tas", "lokasi": "Ruang Kelas 2.3"}
    ]
    
    n = len(data_barang)
    print("=== SISTEM INFORMASI BARANG Hilang ===")
    print("-----------------------------------------------------")
    
    while True:
        target = input("Masukkan nama barang yang Anda cari: ").strip()
        if target: 
            break
        print("Input tidak boleh kosong!")
    hasil_pencarian = cari_barang_hilang(data_barang, n, target)

    print("\n--- Hasil Pencarian ---")
    if len(hasil_pencarian) > 0:
        print(f"Ditemukan {len(hasil_pencarian)} data yang cocok:")
        for idx, barang in enumerate(hasil_pencarian, 1):
            print(f"{idx}. Barang: {barang['nama']}")
            print(f"   Lokasi Penyimpanan: {barang['lokasi']}")
            print("-" * 30)
    else:
        print(f"Maaf, barang '{target}' tidak ditemukan dalam database temuan.")

if __name__ == "__main__":
    main()
