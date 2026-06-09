RESERVASI BIOSKOP 
--------------------------------------------
Program ini berfungsi sebagai manajemen reservasi biskop untuk mengelola data pemesanan kursi. Melalui sistem yang telah dibuat user dapat melakukan pengecekan status kursi secara cepat, melihat daftar pemesanan yang terdaftar di baris yang sudah terisi serta melakukan pembatalan atau melakukan pemesanan dengan cepat. Sistem ini sangat berguna untuk menangani alur data yang dinamis seperti kursi sering kali dipesan dan dibatalakan dalam waktu yang bersamaan. 

Algoritma yang diterapkan adalah struktur data hash table dengan metode Separate Chaining. Metode ini untuk mengatasi collision dengan menggunakan linked list di setiap bucket tabel. Dengan ini pemesan yang mempunyai nilai hash yang sama pada nomor kursi tertentu dapat disimpan secara berurutan dalam satu data, sehingga  operasi pencarian dan penghapusan data tetap berjalan dengan waktu akses yang optimal.

Source Code:
<img width="1051" height="907" alt="image" src="https://github.com/user-attachments/assets/b3c5766c-9c31-4764-9e48-deacccaa78f7" />

<img width="1027" height="827" alt="image" src="https://github.com/user-attachments/assets/46a83686-ac75-4fcf-81d3-789b133b0d25" />

<img width="1053" height="851" alt="image" src="https://github.com/user-attachments/assets/11cf62f8-5d9a-49d4-8248-ee2464063a2e" />

Baris 1–5: Mendefinisikan unit terkecil data. Setiap Node menyimpan key (nomor kursi), value (nama penumpang), dan next (penunjuk ke node berikutnya jika terjadi collision).

Baris 7–10: Inisialisasi hash table dengan ukuran (SIZE=10). self.table adalah list yang berisi None, yang nantinya akan menyimpan node pertama dari linked list.

Baris 12–13: Menentukan posisi indeks dalam tabel menggunakan sisa bagi. Operasi ini memastikan nomor kursi berapa pun akan selalu masuk ke dalam rentang indeks 0–9.

Baris 15–25: Logika utama untuk memesan kursi dan Mencari indeks berdasarkan kunci.

Baris 18-22: memeriksa apakah kursi sudah dipesan. Jika sudah, nama penumpang diperbarui. Jika belum, new_node dibuat dan diletakkan di depan list pada indeks tersebut.

Baris 27–34: Mencari data penumpang berdasarkan nomor kursi. Program masuk ke indeks hasil hash, lalu menyusuri linked list (while current is not None) sampai menemukan kunci yang cocok.

Baris 36–49: Menghapus reservasi dan Program mencari node target. prev digunakan untuk menyambungkan kembali node sebelum dan sesudah node yang dihapus, sehingga rantai linked list tidak terputus.

Baris 51–62: Fungsi untuk mencetak sebuah reservasi bioskop. Program melakukan looping ke setiap indeks. Jika indeks berisi linked list, ia akan mencetak semua kursi yang ada di rantai tersebut hingga mencapai NULL.

Baris 64–74: Inisialisasi objek bioskop dan pembuatan loop menu interaktif yang akan terus berjalan sampai pengguna memilih opsi 4 (Keluar).

Baris 75–79: Penanganan kesalahan jika pengguna memasukkan input selain angka untuk menu.

Baris 81–82: Jika pilih 1, fungsi display() dipanggil untuk memperlihatkan kondisi kursi saat ini.

Baris 84–91: Jika pilih 2, program meminta input nomor kursi dan nama, lalu menjalankan insert untuk menyimpan data.

Baris 93–101: Jika pilih 3, program meminta nomor kursi dan menjalankan remove_key. Jika kursi ada, reservasi dibatalkan.

Baris 103–106: Jika pilih 4, program berhenti. Jika input tidak sesuai angka menu, pesan kesalahan ditampilkan.

Baris 108–109: Baris eksekusi utama yang memanggil fungsi main() saat skrip dijalankan.



Output:

<img width="812" height="747" alt="image" src="https://github.com/user-attachments/assets/931636a2-b1ca-4e8b-9cae-1c46a51961cf" />

<img width="812" height="701" alt="image" src="https://github.com/user-attachments/assets/fe3d26a8-bed0-4628-9f27-f850c275071d" />



Link Video 
