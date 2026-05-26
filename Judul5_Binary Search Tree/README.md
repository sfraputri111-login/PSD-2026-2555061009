----------------------------------------
SISTEM JADWAL HARIAN 
----------------------------------------
Program ini dibuat untuk jadi asisten jadwal harian digital. Fungsinya, nambahin agenda baru, nyari kegiatan di jam tertentu, ngitung total aktivitas, sampai ngeliat semua rencana dari pagi sampai malam biar gak ada yang kelewat. Sistem otomatis mendeteksi bentrokan waktu. Jadi, kalau masukin kegiatan baru di jam yang udah ada isinya, program bakal langsung menimpa agenda lama dengan yang paling baru. Bisa tahu dengan cepat apa kegiatan pembuka hari paling pagi dan penutup hari paling malam.

program ini pakai struktur data Binary Search Tree atau Pohon Pencarian Biner. Setiap jadwal disimpan dalam bentuk node, di mana jam dan menit dikonversi jadi angka sebagai kuncinya. Karena pakai konsep BST, pencarian jadwal jadi efisien. Program tinggal belok ke kiri kalau mau nyari jadwal yang lebih pagi, atau belok ke kanan buat nyari jadwal yang lebih malam. Buat nampilin semua agenda secara berurutan dari terbit matahari sampai tengah malam, program pakai metode In-order Traversal, ngelewatin pohon data dari angka terkecil ke terbesar secara otomatis.

Source Code
<img width="1331" height="903" alt="image" src="https://github.com/user-attachments/assets/1af9dd70-92f0-4019-84d2-46efec0df4dc" />
<img width="1328" height="857" alt="image" src="https://github.com/user-attachments/assets/1e39dd80-8e10-432c-90f2-236b0986fd1a" />
<img width="1322" height="873" alt="image" src="https://github.com/user-attachments/assets/c6707c8d-fb3e-43fd-8635-83f33d622063" />
<img width="1319" height="780" alt="image" src="https://github.com/user-attachments/assets/cd8e5819-7139-4129-9f84-3cad7c963049" />

Baris 1: Mendeklarasikan pembuatan kelas bernama Node.

Baris 2: Membuat otomatis jalan saat sebuah node baru dibuat. Fungsi ini menerima input key (waktu angka) dan kegiatan.

Baris 3: Menyimpan input angka waktu ke dalam variabel internal self key.

Baris 4: Menyimpan nama aktivitas ke dalam variabel internal self.kegiatan.

Baris 5: Menyiapkan slot cabang kiri (self.left) dan diisi kosong (None) karena belum punya anak pohon.

Baris 6: Menyiapkan slot cabang kanan (self.right) dan diisi kosong (None). Struktur Utama Pohon (class SistemJadwalBST)Kelas ini mengatur semua logika bagaimana jadwal disimpan, dicari, dan diurutkan menggunakan konsep pohon biner (BST).

Baris 8: Mendeklarasikan kelas utama SistemJadwalBST.

Baris 9-10: Membuat fungsi awal yang mengatur bahwa saat sistem pertama kali dijalankan, titik pusat (self.root) masih kosong (None).Logika Menambah Jadwal (insert_node & insert)

Baris 12: Fungsi internal insert_node untuk meletakkan jadwal secara rekursif (berulang) dari titik root tertentu.

Baris 13-14: Jika posisi titik yang dicek kosong (None), buat objek Node baru di posisi tersebut dengan membawa data key dan kegiatan.

Baris 15-16: Jika jam baru (key) lebih kecil daripada jam di titik saat ini (root.key), sistem akan mencari slot kosong ke arah cabang kiri (root.left).

Baris 17-18: Jika jam baru (key) lebih besar daripada jam di titik saat ini, sistem akan mencari slot kosong ke arah cabang kanan (root.right).

Baris 19-21: Jika jam baru ternyata persis sama dengan jam yang sudah terdaftar, program mencetak teks pemberitahuan, lalu menimpa isi root.kegiatan dengan nama kegiatan yang baru.

Baris 22: Mengembalikan kondisi titik root yang sudah diperbarui posisinya.

Baris 24-25: Fungsi insert agar user dari luar bisa langsung memasukkan jadwal tanpa harus pusing memikirkan posisi root internal pohon. Hasilnya langsung disimpan kembali ke self.root.

Baris 27: Fungsi internal search_node untuk mencari jadwal berdasarkan angka waktu (key).

Baris 28-29: Jika titik tidak ditemukan (None) atau angka jamnya sudah persis sama dengan yang dicari, langsung kembalikan data titik tersebut (return root).

Baris 30-31: Jika jam yang dicari lebih kecil dari titik saat ini, cari ke arah cabang kiri.

Baris 32: Jika jam yang dicari lebih besar, cari ke arah cabang kanan.

Baris 34-35: Fungsi pembungkus search untuk memudahkan pemanggilan dari menu utama dengan otomatis memulai pencarian dari akar pohon paling atas dan Menampilkan Agenda Berurutan.

Baris 37-39: Fungsi untuk mencetak jadwal. Jika posisi titik kosong (None), fungsi langsung berhenti (return).

Baris 40: Sistem secara rekursif masuk dulu ke cabang kiri terdalam (mencari waktu paling pagi yang tersedia).

Baris 41: Setelah mentok di kiri, sistem mencetak jam (yang sudah diubah formatnya) beserta nama kegiatannya.

Baris 42: Setelah mencetak titik tengah, sistem berpindah memeriksa cabang kanan (waktu yang lebih malam). Ini disebut metode In-order Traversal.Mencari Agenda Paling Pagi (find_min).

Baris 44-46: Jika pohon kosong, langsung kembalikan nilai None.

Baris 47: Menandai titik awal penelusuran dari posisi root.

Baris 48-49: Selama cabang sebelah kiri masih ada isinya (is not None), sistem akan terus berjalan ke arah kiri tanpa henti.

Baris 50: Setelah mentok di paling kiri (angka terkecil), data titik tersebut dikembalikan sebagai waktu paling pagi.Mencari Agenda Paling Malam (find_max).

Baris 52-55: Logikanya mirip dengan find_min, diawali dengan validasi kosong dan penandaan titik mulai.

Baris 56-57: Bedanya, sistem ini melakukan perulangan terus menerus bergeser ke arah kanan (current.right) untuk mencari angka terbesar.

Baris 58: Mengembalikan data titik paling kanan sebagai waktu paling malam.Menghitung Total Aktivitas (count_nodes).

Baris 60-61: Jika titik kosong, nilainya adalah 0.

Baris 62-63: Jika ada isinya, sistem menghitung angka 1 (untuk dirinya sendiri) ditambah hasil hitungan total node di cabang kiri dan total node di cabang kanan secara rekursif.Mengubah Format Angka ke Jam (format_jam).

Baris 65-66: Mengubah angka integer (misal 1345) menjadi teks jam standar. key mengambil 2 angka di depan (jam), dan key mengambil 2 angka sisa di belakang (menit). memastikan jika angkanya satuan tetap ditulis dua digit dan Alur Menu Utama (def main()) Bagian ini adalah motor penggerak utama yang berinteraksi langsung dengan ketikan user di terminal.

Baris 68-70: Membuat fungsi utama, mengaktifkan objek SistemJadwalBST(), dan menyetel variabel pilihan menu pilih = 0.

Baris 71: Memulai perulangan menu selama user tidak memilih angka 6 (pilihan keluar).

Baris 72-78: Mencetak teks pilihan menu (1 sampai 6) di layar terminal.

Baris 80-81: Meminta user mengetik angka menu dan mengubahnya langsung menjadi tipe data integer (int).

Baris 82-84: Antisipasi eror (try-except), jika user mengetik huruf, program tidak akan mogok melainkan memunculkan peringatan dan mengulang perulangan lewat perintah continue.

Baris 86-89: Jika memilih 1, sistem meminta input jam dan menit secara terpisah, lalu diubah ke integer.

Baris 90-92: Memvalidasi batas waktu wajar. Jam harus di antara 0-23 dan menit di antara 0-59. Jika ngawur, muncul teks salah dan diulang.

Baris 94: Mengonversi jam dan menit ke bentuk angka kunci tunggal.

Baris 95-97: Meminta input nama kegiatan, memasukkannya ke sistem pohon melalui fungsi bst.insert, lalu memunculkan konfirmasi sukses.

Baris 98-99: Mengamankan eror jika input jam dan menit yang diketik bukan angka.

Baris 101-105: Jika memilih 2, sistem meminta input jam dan menit yang mau dicari, lalu dikonversi dengan rumus yang sama menjadi key_waktu.

Baris 107-111: Menjalankan perintah bst.search. Jika variabel hasil ada standsart datanya, tampilkan nama agendanya. Jika kosong (None), munculkan teks tidak ada agenda.

Baris 112-113: Pengaman dari eror salah ketik huruf pada menu cari.

Baris 115-118: Jika memilih 3, sistem mengecek dulu apakah akar pohon (bst.root) kosong. Jika iya, tampilkan teks belum ada jadwal.

Baris 119-120: Jika ada isinya, panggil fungsi bst.cetak_kronologis untuk menampilkan seluruh agenda terurut dari pagi.

Baris 122-124: Jika memilih 4, sistem memanggil fungsi find_min dan find_max sekaligus, lalu menyimpannya di variabel node_min dan node_max.
Baris 125-129: Jika datanya ditemukan, sistem menampilkan jadwal paling pagi dan paling malam ke layar terminal.

Baris 131-132: Jika memilih 5, sistem memanggil fungsi bst.count_nodes dan langsung mencetak jumlah angka total agenda harian saat itu.

Baris 134-136: Jika memilih 6, sistem menampilkan salam perpisahan dan memotong paksa perulangan menggunakan perintah break sehingga program berhenti teratur.

Baris 137-138: Menghandle jika user mengetik angka di luar pilihan 1-6.

Baris 140-141: Baris standar Python untuk memastikan bahwa fungsi main() hanya akan berjalan otomatis jika file script ini dieksekusi secara langsung, bukan karena diimport oleh file lain.

Output

<img width="696" height="549" alt="image" src="https://github.com/user-attachments/assets/90878501-3b4e-471a-92b6-e63b1da8f6f6" />
<img width="698" height="722" alt="image" src="https://github.com/user-attachments/assets/2af97702-f934-4ac5-884f-c4a83349fcb3" />
<img width="498" height="208" alt="image" src="https://github.com/user-attachments/assets/e5f711dd-ec2c-437b-8233-fe75050a5d44" />

user memilih nomor 1 dan user memasukan jam 1 dan menit 32 dengan nama kegiatan Belajar. Program sukses mengubah input tersebut menjadi format waktu 01:32 dan menyimpannya ke dalam sistem.
User memilih nomor 2 dan User mencoba mencari tahu ada agenda apa di jam 1 lewat 32 menit. Karena tadi sudah disimpan, program langsung berhasil menemukan dan menampilkan yang telah disimpan tadi.
User memilih nomor 3 dan program menampilkan seluruh jadwal yang ada secara berurutan karena user baru input satu jadwal yang muncul dilayar cuman satu jadwal tersebut.
User memilih nomor 4 dan Fitur ini otomatis mencari kegiatan paling awal dan paling akhir.
User memilih nomor 5 dan Program menghitung ada berapa banyak aktivitas yang sudah dicatat.
User memilih nomor 6 dan sistem menutup program dengan menampilkan salam penutupnya.


Link Presentasi
https://youtu.be/IS_dthYAf-c?si=fyIkvhVSbISwpydk
