-------------------------------------------------------------------
SISTEM ANTREAN BANK MANDIRI  
-------------------------------------------------------------------
Program ini untuk sistem pemanggilan nomor antrean di Bank Mandiri secara digital. di mana admin atau mesin cetak bisa memasukkan nama nasabah baru ke dalam barisan waiting list (enqueue). Ketika teller sudah kosong, nasabah di urutan paling depan akan langsung dipanggil (dequeue). Program ini juga menyediakan fitur untuk mengintip siapa nasabah berikutnya yang harus bersiap-siap (peek) serta memantau seluruh barisan nasabah yang masih mengantre secara keseluruhan (display). 

Tujuannya, yaitu untuk memastikan proses pelayanan nasabah berjalan adil, rapi, dan meminimalkan kesalahan manusia saat pemanggilan. Program ini mengandalkan konsep Queue (Antrean) dengan metode FIFO (First-In, First-Out). Artinya, siapa pun nasabah yang datang dan mencatatkan namanya duluan, dia pula yang akan dilayani pertama kali oleh teller. Agar ukurannya bisa fleksibel, Queue di sini tidak memakai array biasa, melainkan menggunakan Linked List dinamis melalui objek bernama Node. Dengan memanfaatkan dua penunjuk utama front_ptr untuk menandai pintu keluar di depan dan rear_ptr untuk mendeteksi ekor antrean di belakang program dapat menambah atau menghapus data nasabah kapan saja tanpa perlu khawatir memorinya penuh atau terbatas.


source code
<img width="1326" height="502" alt="image" src="https://github.com/user-attachments/assets/fcd3afb1-0eba-4e03-a693-f05b54bfdf0e" />
<img width="1326" height="527" alt="image" src="https://github.com/user-attachments/assets/554dca75-e450-4486-9fdb-feb70a90335a" />
<img width="1321" height="455" alt="image" src="https://github.com/user-attachments/assets/3de0bd5b-bb9d-4fb0-a038-5c12c037f9d2" />
<img width="1322" height="523" alt="image" src="https://github.com/user-attachments/assets/e48c27fb-a01d-429b-b4ea-ad807545e7c5" />
<img width="1322" height="457" alt="image" src="https://github.com/user-attachments/assets/563d2382-503c-45fa-b835-ef806909efd9" />

Pada baris 1 Mendefinisikan sebuah kelas bernama Node. Node adalah komponen dasar pembentuk Linked List.

Pada baris 2 untuk menginisialisasi objek Node baru setiap kali data dimasukkan.

Pada baris 3 Menyimpan nilai data yang dimasukkan ke dalam node tersebut.

Pada baris 4 Mengatur penunjuk ke node berikutnya. Saat pertama kali dibuat, node belum terhubung ke mana pun, sehingga bernilai None.

Pada baris 6 Mendefinisikan kelas untuk mengatur antrean.

Pada baris 7 untuk membuat antrean baru yang masih kosong.

Pada baris 8 dan 9 front_ptr (menunjuk elemen paling depan/yang akan keluar) dan rear_ptr (menunjuk elemen paling belakang/yang baru masuk). Di awal, keduanya bernilai None.

Pada baris 11 dan 12  untuk memeriksa apakah antrean kosong. Mengembalikan nilai True jika front_ptr bernilai None.

Pada baris 13 Menambah Antrean

Pada baris 14 membuat Node baru berisi data nasabah tersebut.

Pada baris 15,16 dan 17 jika bank kosong, front_ptr dan rear_ptr langsung ditugaskan untuk menunjuk nasabah baru ini.

Pada baris 18 rencana cadangan ketika kondisi-kondisi utama yang diuji tidak ada yang terpenuhi.

Pada baris 19 dan 20 Jika sudah ada orang lain, nasabah paling belakang saat ini akan mengarahkan tangan next nya untuk menggandeng nasabah baru tersebut. Setelah itu, status nasabah paling belakang dipindahkan ke orang baru tersebut.

Pada baris 21 mempilkan jika enqueue berhasil 

Pada baris 23 Mengurangi atau Memanggil Antrean

Pada baris 24, 25, 34, 35, 36, 26, 40, 41, 42 Jika  bernilai True, program langsung mencetak Queue kosong dan berhenti (return).

Pada baris 27 Jika ada nasabah, program mencatat data nasabah terdepan ke variabel sementara (temp).

Pada baris 28 jika program berhasil mencatat data di temp maka akan muncul temp pada data berhasil.

Pada baris 29 Penunjuk depan digeser maju ke orang di belakangnya. Secara otomatis, nasabah terdepan yang lama terlepas dari sistem.

Pada baris 30 dan 31 mendeteksi apakah antrean menjadi benar-benar habis Jika kondisi itu terpenuhi, program akan otomatis membersihkan penunjuk belakang.

Pada baris 33 Mengintip Baris Terdepan

Pada baris 37 Hanya melihat siapa nasabah yang berada di urutan pertama saat ini lewat, tanpa menghapus atau mengubah urutan antrean sama sekali.

Pada baris 39 Cetak Seluruh Daftar

Pada baris 43 untuk mencetak teks judul pembuka ke layar komputer.

Pada baris 44 Membuat sebuah variabel posisi saat ini dan meletakkannya di titik awal antrean, yaitu sama dengan posisi yang ditunjuk oleh self.front_ptr.

Pada baris 45 perintah perulangan. Program diinstruksikan untuk terus mengulang kode yang ada di dalam blok while selama variabel current tidak bernilai kosong.

Pada baris 46 Program mengambil data nasabah yang sedang berdiri di posisi current, lalu mencetaknya ke layar.

Pada baris 47 instruksi untuk menggeser posisi agar maju satu langkah ke node di belakangnya.

Pada baris 48 akan dieksekusi setelah perulangan selesai total (ketika current sudah mencapai None).

Pada baris 50 Mendeklarasikan sebuah fungsi 

Pada baris 51 Melakukan pembuatan objek dari kelas yang sudah didefinisikan sebelumnya, kemudian menyimpannya ke dalam variabel lokal bernama queue.

Pada baris 52 Membuat sebuah variabel dengan tipe data bilangan bulat (integer) dan mengisi nilai awalnya dengan angka 0.

Pada baris 53 menyimpan angka menu yang diketik oleh pengguna dan Karena 0 tidak sama dengan 5, maka program diizinkan untuk masuk dan mulai menampilkan pilihan menu bank kepada pengguna.

Pada baris 55, 56, 57, 58, 59, 60, 61, 62, 63 ketika pengguna memiiih 1 sampai dengan 5 maka akan tampil yang telah diinputkan oleh si pengguna.

Pada baris 65 dan 66 Program membuka blok try. Di dalamnya fungsi input() mengambil teks yang diketik pengguna lalu fungsi int() mencoba mengubah teks tersebut menjadi angka bulat. Hasilnya disimpan ke dalam variabel pilih.

Pada baris 67, 68, 69 jika pengguna memasukan selain angka 1-5 akan gagal dan memicu error. Blok except langsung menangkap error tersebut, mencetak pesan peringatan dan continue akan memaksa program melompat kembali ke awal tanpa melanjutkan kode di bawahnya.

Pada baris 71, 72 ika pilih bernilai 1, program meminta pengguna nomor identitas nasabah lalu menyimpannya.

Pada baris 73, 74 dan 75 strip() digunakan untuk menghapus spasi kosong di awal atau akhir input. Jika setelah dihapus hasilnya kosong maka program memberikan peringatan dan continue membatalkan proses lalu melempar pengguna kembali ke menu utama.

Pada baris 77 Jika input valid, nilai variabel ditambah 1 sebagai tanda ada nomor urut baru yang tercipta.

Pada baris 78 Membuat format teks tiket antrean bank resmi. Kode :03d berarti angka di dalamnya wajib ditulis dalam 3 digit.

Pada baris 79 Memanggil metode enqueue pada objek queue untuk membungkus teks data_sistem tadi ke dalam sebuah Node baru dan ke barisan paling belakang antrean.

Pada baris 81, 82 dan 83 Jika pilih bernilai 2 program memeriksa kondisi antrean. Jika fungsi queue.is_empty() mengembalikan nilai True, program langsung memanggil queue.dequeue() yang di dalamnya sudah diprogram untuk mencetak teks Queue kosong.

Pada baris 84, 85, 86,  dan 87 Jika antrean tidak kosong, program mencetak kalimat pembuka, memanggil fungsi queue.dequeue() untuk memproses dan menghapus nasabah yang berada di urutan paling depan lalu mencetak instruksi agar nasabah tersebut pergi ke Teller 1.

Pada baris 89 dan 90 Jika pilih bernilai 3, program memanggil metode queue.peek() untuk melihat dan mencetak data nasabah yang berada di urutan terdepan saat ini tanpa mengubah isi antrean.

Pada baris 91 dan 92 Jika pilih bernilai 4, program memanggil metode queue.display() untuk menelusuri linked list dari depan ke belakang dan mencetak seluruh daftar nasabah yang sedang mengantre.

Pada baris 93 dan 94 ika pilih bernilai 5, program mencetak ucapan terima kasih. Karena nilai pilih sekarang berubah menjadi 5, kondisi pada perulangan utama akan bernilai salah sehingga perulangan berhenti otomatis.

Pada baris 95 dan 96 Jika pengguna memasukkan angka bulat tetapi di luar jangkauan 1–5 (misalnya mengetik angka 9) semua kondisi if dan elif di atas akan bernilai salah, sehingga baris ini dijalankan untuk memberi peringatan.

Pada baris 98 dan 99 Memeriksa apakah sedang dijalankan secara langsung oleh pengguna di terminal dan menjadi pemicu utama roda program berputar dari awal hingga akhir.

output dari source code

<img width="572" height="260" alt="image" src="https://github.com/user-attachments/assets/92ce5de1-9e48-42e1-a8f6-048c2ee2f593" />
<img width="576" height="262" alt="image" src="https://github.com/user-attachments/assets/7b58a49a-ab0a-4331-94bf-4ca076d8338a" />
<img width="558" height="262" alt="image" src="https://github.com/user-attachments/assets/d5e92f7c-f1b4-47ce-b9a4-83f71b87300e" />
<img width="558" height="263" alt="image" src="https://github.com/user-attachments/assets/700abcb1-bd4a-4f81-853d-e45d52821fbc" />
<img width="558" height="227" alt="image" src="https://github.com/user-attachments/assets/3ceb1fd9-4bf2-438e-b44f-58b0e66cd1b0" />
<img width="552" height="220" alt="image" src="https://github.com/user-attachments/assets/3668c803-76da-4fd7-b734-69434c635262" />
<img width="726" height="235" alt="image" src="https://github.com/user-attachments/assets/acaade67-bf46-4bd9-a813-99aad42695f9" />
setelah program dijalankan akan muncul pilihan dari nomor 1-5, ketika milih nomor 1 maka pengguna akan disuruh untuk memasukan nomor nasabah dan jika sudah akan muncul pesan nomor nasabah telah berhasil dan menggunakan prinsip enqueue. Di sini penggun memasukan nomor nasabah dan memilih nomor 1 sebanyak 3 kali. Kemudian pengguna memilih nomor 2 yaitu memanggil nasabah ke teller 1, Pengguna memilih nomor 3 yaitu untuk melihat antrian dengan menggunakan peek dan telah muncul antrean depan nya adalah B-002 dan 6. Pengguna memilih nomor 4 yaitu untuk mencetak seluruh nomor antrean yang ada pada saat ini dan akan muncul output secara depan ke belakang. Kemudian terakhir pengguna memasukan nomor 5 untuk keluar dari program dan program pun telah selesai. 

Link Presentasi 
https://youtu.be/aeBGgi7bwsQ?feature=shared
