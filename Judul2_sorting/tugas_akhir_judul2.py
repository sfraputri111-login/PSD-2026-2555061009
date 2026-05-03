def urutkan_antrean_dapur(antrean_level):
    for i in range(1, len(antrean_level)):
        level_saat_ini = antrean_level[i]
        j = i - 1
        
        while j >= 0 and antrean_level[j] > level_saat_ini:
            antrean_level[j + 1] = antrean_level[j]
            j -= 1
        antrean_level[j + 1] = level_saat_ini

def main():
    print("=== SISTEM MANAJEMEN DAPUR: MIE PEDAS ===")
    print("Membantu Koki memasak berdasarkan urutan level (0 -> Terpedas)\n")
    
    try:
        n = int(input("Masukkan jumlah total pesanan saat ini: "))
    except ValueError:
        print("Input salah! Masukkan jumlah dalam angka.")
        return

    antrean = []
    for i in range(n):
        while True:
            try:
                level = int(input(f"Level pedas pesanan ke-{i+1}: "))
                antrean.append(level)
                break
            except ValueError:
                print("Masukkan angka level yang valid!")

    print(f"\n Pesanan masuk (berdasarkan waktu): {antrean}")
    urutkan_antrean_dapur(antrean)
    
    print("Rekomendasi urutan masak untuk koki:")
    for idx, level in enumerate(antrean):
        print(f"{idx + 1}. Masak Mie Level: {level}")
    print("Catatan: Urutan ini meminimalkan kontaminasi rasa cabai di wajan.")

if __name__ == "__main__":
    main()
