------------------------------------------------------------------------------
SISTEM VERIFIKASI PESERTA UJIAN 
------------------------------------------------------------------------------
Sistem ini dibuat untuk mempermudah proses verifikasi peserta ujian di kelas secara otomatis. Alih-alih pengawas harus mengecek tumpukan kertas secara manual, mereka cukup memasukkan nomor kursi untuk melihat siapa peserta yang seharusnya duduk di sana. Sistem ini tidak hanya menampilkan nama, tapi juga memberikan informasi posisi duduk seperti indeks data dan pembagian zona baris (depan atau belakang). Tujuannya agar alur masuk ruang ujian lebih tertib dan meminimalisir kesalahan posisi duduk siswa kemudian sistem ini mengandalkan Binary Search  Karena data nomor kursi sudah tersusun rapi, algoritma ini bisa bekerja  dengan cara membelah data menjadi dua bagian terus-menerus sampai posisi kursi ditemukan. Cara ini jauh lebih cepat dibanding harus mengecek satu-satu dari awal. Untuk penyimpanan datanya, saya menggunakan List dan Tuples. List bertugas menjaga agar urutan data tetap konsisten, sementara Tuple digunakan untuk mengunci pasangan nomor kursi dan nama agar datanya aman, efisien, dan tidak mudah berubah secara tidak sengaja.

Source Code
<img width="1112" height="551" alt="image" src="https://github.com/user-attachments/assets/c1a69d61-3faf-4597-94f4-d844a8eb9a89" />

<img width="947" height="417" alt="image" src="https://github.com/user-attachments/assets/7ea13e99-fe63-4369-a44d-be3bcd84f409" />
Pada baris 1 Mendefinisikan fungsi yang menerima dua parameter yaitu data dan target.

Pada baris 2 Inisialisasi indeks terendah atau batas kiri pencarian pada posisi awal (0).

Pada baris 3 Inisialisasi indeks tertinggi atau batas kanan pencarian pada posisi terakhir daftar.

Pada baris 4 Melakukan perulangan selama rentang pencarian masih valid yang dimana Jika nomor tidak ditemukan maka pembatas low akan bergeser ke kanan melewati high atau high bergeser ke kiri melewati low.

Pada baris 5 Mencari indeks tengah dari rentang yang ada dan (//) digunakan agar hasilnya tetap berupa angka indeks yang utuh.

Pada baris 6 dan 7 Mengecek apakah nomor kursi pada indeks tengah sama dengan target dan Jika cocok fungsi langsung selesai dan mengirimkan indeks tersebut dan langsung return mid.

Pada baris 8 dan 9 Jika nomor di tengah ternyata lebih kecil dari yang dicari yang berarti target ada di sisi kanan Maka low digeser maju melewati tengah (mid + 1).

Pada baris 10 dan 11 Jika nomor di tengah lebih besar berarti target ada di sisi kiri Maka high digeser mundur sebelum tengah (mid - 1).

Pada baris 12 Jika perulangan selesai tanpa menemukan kecocokan maka fungsi mengirimkan sinyal -1 (data tidak ditemukan).

Pada baris 14 untuk Mendefinisikan fungsi utama program.

Pada baris 15 untuk Inisialisasi basis data yang dimana beberapa menyimpan dalam bentuk tuple ke dalam sebuah list.

Pada baris 16, 17 Untuk menampilkan sebuah data yang nanti akan menjadi kunci pencarian.

Pada baris 18 untuk menunjukan bahwa selama program berjalan tidak dapat tertukar atau berubah secara tidak sengaja.

Pada baris 20 Untuk menampilkan nama progam ke dalam layar dan output nanti

Pada baris 21 untuk mengantisipasi kesalahan dari input.

Pada baris 22 Meminta input dari pengguna kemudian mengonversinya menjadi bilangan bulat.

Pada baris 23 Memanggil fungsi Binary Search untuk mendapatkan indeks dari nomor kursi yang dimasukkan.

Pada baris 25 Jika indeks ditemukan (bukan -1) maka jalankan perintah di bawahnya.

Pada baris 26 untuk membuka data pada indeks yang ditemukan ke dalam variabel nomor dan nama.

Pada baris 27 Menentukan zonasi area Jika indeks berada di 0-3 maka masuk Baris Depan dan jika tidak maka masuk Baris Belakang.

Pada baris 29, 30, 31, 32 untuk menampilkan sebuah data yang telah ditemukan ke dalam output

Pada baris 33 dan 34 Jika indeks adalah -1 maka tampilkan pesan bahwa data kursi tersebut tidak ditemukan atau kosong.

Pada baris 35 dan 36 Menangkap kesalahan jika pengguna memasukkan karakter selain angka lalu menampilkan pesan peringatan yang sesuai.

Pada baris 38 Memastikan bahwa fungsi main() hanya akan dieksekusi jika file ini dijalankan secara langsung, bukan saat diimpor sebagai modul oleh file lain.

Pada baris 39 Memanggil fungsi utama untuk memulai program.

Output
<img width="685" height="154" alt="image" src="https://github.com/user-attachments/assets/37e9e7d7-3c5b-477d-adc4-116df434d14c" />
Program ini meminta input angka dari User. pengguna memasukkan sebuah angka 5, yang kemudian diproses oleh fungsi pencarian untuk dicocokkan dengan data yang ada di dalam sistem.
karena algoritma pencarian berhasil menemukan angka 5 di dalam daftar dan Jika angka tidak ada dalam daftar, pesan yang muncul adalah "Data tidak ditemukan", setelah data ditemukan Program menampilkan tiga informasi utama hasil dari proses unpacking data pada indeks yang ditemukan yaitu Nama peserta, Nomor Kursi, Posisi Area.

Link Presentasi
