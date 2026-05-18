-------------------------------------------------------------------
SISTEM ANTREAN BANK MANDIRI  
-------------------------------------------------------------------
Program ini dirancang untuk mensimulasikan sistem pemanggilan nomor antrean di Bank Mandiri secara digital. Konsepnya dibuat mirip dengan operasional dunia nyata, di mana admin atau mesin cetak bisa memasukkan nama nasabah baru ke dalam barisan waiting list (enqueue). Ketika teller sudah kosong, nasabah di urutan paling depan akan langsung dipanggil (dequeue). Selain itu, program ini juga menyediakan fitur praktis untuk mengintip siapa nasabah berikutnya yang harus bersiap-siap (peek) serta memantau seluruh barisan nasabah yang masih mengantre secara keseluruhan (display). Tujuannya, yaitu untuk memastikan proses pelayanan nasabah berjalan adil, rapi, dan meminimalkan kesalahan manusia saat pemanggilan. Program ini mengandalkan konsep Queue (Antrean) dengan metode FIFO (First-In, First-Out). Artinya, siapa pun nasabah yang datang dan mencatatkan namanya duluan, dia pula yang akan dilayani pertama kali oleh teller. Agar ukurannya bisa fleksibel, Queue di sini tidak memakai array biasa, melainkan menggunakan Linked List dinamis melalui objek bernama Node. Dengan memanfaatkan dua penunjuk utama front_ptr untuk menandai pintu keluar di depan dan rear_ptr untuk mendeteksi ekor antrean di belakang program dapat menambah atau menghapus data nasabah kapan saja tanpa perlu khawatir memorinya penuh atau terbatas seperti pada array statis.

source code




output dari source code

Link Presentasi 
