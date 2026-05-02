def insertion_sort_level_pedas(antrean_level, total_pesanan):
    for i in range(1, total_pesanan):
        level_saat_ini = antrean_level[i]
        j = i - 1
        
        while j >= 0 and antrean_level[j] > level_saat_ini:
            antrean_level[j + 1] = antrean_level[j]
            j -= 1
        antrean_level[j + 1] = level_saat_ini

def main():
    print("=== Sistem  pengurutan Berdasarkan Level Pedas ===")
    try:
        n = int(input("Masukkan jumlah pesanan masuk: "))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
        return

    antrean = []
    print(f"\nMasukkan level pedas untuk {n} pesanan (contoh: 0, 1, 5):")
    for i in range(n):
        while True:
            try:
                level = int(input(f"Pesanan ke-{i+1}: "))
                antrean.append(level)
                break
            except ValueError:
                print("Input tidak valid, masukkan angka level pedas!")

    print(f"Antrean masuk berdasarkan level pedas : {antrean}")
    insertion_sort_level_pedas(antrean, n)

if __name__ == "__main__":
    main()
