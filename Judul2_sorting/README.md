-----------------------------------------------------
Sistem Pengurutan level mie pedas berdasarkan pesanan
-----------------------------------------------------
Program ini fungsinya sebagai sistem optimalisasi produksi mie yang bertugas mengatur urutan masak berdasarkan tingkat kepedasan pesanan pelanggan. Dengan mengurutkan pesanan dari level pedas terendah hingga tertinggi, program ini membantu meminimalkan risiko kontaminasi antar pesanan dan meningkatkan efisiensi proses memasak karena koki tidak perlu sering membersihkan peralatan memasak akibat bekas kepedasan cabe yang lebih tinggi dibandingkan pesanan selanjutnya. Algoritma yang diterapkan dalam program ini adalah insertion sort yang dimana sebuah metode pengurutan berbasis Perbandingan yang bekerja dengan cara membangun deretan data terurut satu demi satu melalui mekanisme penyisipan elemen. Struktur data utama yang digunakan list atau antrean yang dimana setiap elemen baru dibandingkan dengan elemen yang sudah terurut sebelumnya dan digeser ke posisi yang tepat hingga seluruh antrean pesanan tersusun dengan rapi dan tidak acak.

Codingan
<img width="762" height="95" alt="image" src="https://github.com/user-attachments/assets/de30d887-ddb5-44f4-8401-2a89c647196c" />
Pada baris 1 merupakan Mendefinisikan fungsi pengurutan dengan parameter antrean_level (daftar angka level pedas).
pada baris 2 merupakan Loop luar yang dimulai dari data kedua (indeks 1). Data pertama (indeks 0) dianggap sebagai titik awal yang sudah benar.
Pada baris 3 merupakan Mengambil pesanan yang sedang diproses dan menyimpannya di variabel sementara agar posisinya bisa digeser-geser.
pada baris 4 merupakan Menentukan indeks elemen tepat di sebelah kiri pesanan yang sedang diproses untuk mulai dibandingkan.
<img width="800" height="105" alt="image" src="https://github.com/user-attachments/assets/e41821d6-e99a-458c-8159-4a4e61315ef4" />
Pada baris 6 merupakan sebuah perbandingan yang dimana Selama belum sampai ujung kiri daftar (j >= 0) dan elemen di kiri lebih pedas (>) daripada pesanan saat ini.
Pada baris 7 merupakan Jika elemen di kiri lebih pedas, pindahkan elemen tersebut satu posisi ke kanan untuk memberi ruang.
Pada baris 8 yang dimana Pindah ke elemen berikutnya di sisi kiri untuk terus dibandingkan.
Pada baris 9 yang dimana jika Setelah menemukan posisi yang tepat (di mana elemen di kiri sudah tidak lebih besar lagi), selipkan pesanan tadi ke posisi tersebut.
<img width="932" height="221" alt="image" src="https://github.com/user-attachments/assets/52174d1f-8116-4b9c-8732-b5da34485e35" />
Pada baris 11 Pada bagian ini merupakan yang mengatur kapan meminta input, kapan menyuruh algoritma bekerja, dan bagaimana menampilkan hasil akhirnya ke layar.
Pada baris 12 dan 13 Menampilkan judul program agar pengguna tahu tujuan aplikasi ini.
Pada baris 15 dan 17 untuk Menjaga agar program tidak error jika pengguna salah memasukkan huruf saat diminta angka.
Pada baris 16 untuk Meminta input jumlah total pesanan yang masuk ke dapur.
Pada baris 18 dan 19 untuk Memberi tahu pengguna (kasir atau koki) bahwa mereka baru saja melakukan kesalahan dan Mengakhiri fungsi saat itu juga.
<img width="895" height="216" alt="image" src="https://github.com/user-attachments/assets/22a6b547-8672-4f74-8c77-07b69fde0115" />
Pada baris 21 merupakan Wadah kosong untuk menyimpan semua data level pedas yang akan dimasukkan.
Pada baris 22 Melakukan perulangan sebanyak n kali untuk mengambil input level pedas satu per satu.
Pada baris 23 dan 24 untuk memberikan data yang valid sebelum program boleh lanjut ke tahap berikutnya.
Pada baris 25 untuk Mengambil data level pedas yang telah di inputkan oleh si user.
Pada baris 26 untuk Memasukkan nilai level yang baru saja diketik ke dalam daftar antrean.
Pada baris 27 dan 28 untuk menghentikan paksa perulangan (loop) yang sedang berjalan dan menangkap kesalahan.
Pada baris 29 untuk jika pengguna memasukan huruf bukan angka sebagai petnda level pedas tersebut maka akan muncul masukan angka level yang valid
<img width="915" height="146" alt="image" src="https://github.com/user-attachments/assets/5591e782-6433-4bd5-a01d-4996112c0b43" />
Pada baris 31 menampilkan urutan asli pesanan tepat sebelum diurutkan.
Pada baris 32 memiliki fungsi untuk memanggil insertion sort yang dimana daftar antrean yang tadinya berantakan atau ssecara acak langsung diproses dengan logika perbandingan dan pergeseran lalu kembali dalam keadaan yang sudah terurut.
Pada baris 33 untuk menampilkan rekomendasi urutan memasak untuk koki.
Pada baris 34 untuk mengambil nilai level yang telah di inputkan oleh si user dan kemudian memberikan nomor urut atau indeks yang disimpan.
Pada baris 35 karena komputer menghitung mulai dari 0 maka tambah 1 untuk koki melihat urutan yang sistematis.
Pada baris 36 untuk menampilkan sebuah catatan yang ada di dalam codingan tersebut
<img width="414" height="93" alt="image" src="https://github.com/user-attachments/assets/74d3255b-3b8f-41d9-a31e-42892f7dd365" />
dan yang terakhir adalah untuk memastikan bahwa program menjalankan langsung saat file phyton dibuka.

Outputnya 
<img width="669" height="60" alt="image" src="https://github.com/user-attachments/assets/93d75b37-1d10-4acc-9d83-8b36280f62a7" />
karena pada baris 12 dan 13 karena disitu perintah hanya untuk menampilkan sebuah judul dari sistem program tersebut dan outputnya seperti ini.
<img width="664" height="242" alt="image" src="https://github.com/user-attachments/assets/dc5d7857-1eed-4cd4-8651-388ea0458c7a" />
Pada codingan baris 16 yang meminta inputkan jumlah total pesanan saat ini maka si user menginputkan total nya 7, user disuruh untuk memasukan level pedas yang masuk saat ini, yang dimana karena ada totalnya 7 maka user harus memasukan level pedas sebanyak 7 dan pada codingan baris ke 18 disitu jika inputnya selain angka maka akan akan muncul output masukan angka yang valid
<img width="751" height="225" alt="image" src="https://github.com/user-attachments/assets/5b59fcc1-e544-421b-b28a-6a881d582e41" />
Pada codingan baris 31 dan 33 yang dimana akan muncul output inputan yang si user telah masukan tadi dan menampilkan nya ke layar atas inputan tersebut. Pada output yang terakhir yang dimana setelah inputan ditampilkan ke layar maka akan muncul catatan terkait fungsi dari program ini.

Link Video Presentasi 
https://youtu.be/L3jUpt6sZao?si=ezEljLc6NizDAYkF
