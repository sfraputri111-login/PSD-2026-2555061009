RESERVASI BIOSKOP 
--------------------------------------------
Program ini berfungsi sebagai manajemen reservasi biskop untuk mengelola data pemesanan kursi. Melalui sistem yang telah dibuat user dapat melakukan pengecekan status kursi secara cepat, melihat daftar pemesanan yang terdaftar di baris yang sudah terisi serta melakukan pembatalan atau melakukan pemesanan dengan cepat. Sistem ini sangat berguna untuk menangani alur data yang dinamis seperti kursi sering kali dipesan dan dibatalakan dalam waktu yang bersamaan. 

Algoritma yang diterapkan adalah struktur data hash table dengan metode Separate Chaining. Metode ini untuk mengatasi collision dengan menggunakan linked list di setiap bucket tabel. Dengan ini pemesan yang mempunyai nilai hash yang sama pada nomor kursi tertentu dapat disimpan secara berurutan dalam satu data, sehingga  operasi pencarian dan penghapusan data tetap berjalan dengan waktu akses yang optimal.

Source Code:
<img width="1051" height="907" alt="image" src="https://github.com/user-attachments/assets/b3c5766c-9c31-4764-9e48-deacccaa78f7" />

<img width="1027" height="827" alt="image" src="https://github.com/user-attachments/assets/46a83686-ac75-4fcf-81d3-789b133b0d25" />

<img width="1053" height="851" alt="image" src="https://github.com/user-attachments/assets/11cf62f8-5d9a-49d4-8248-ee2464063a2e" />






Output:

<img width="812" height="747" alt="image" src="https://github.com/user-attachments/assets/931636a2-b1ca-4e8b-9cae-1c46a51961cf" />

<img width="812" height="701" alt="image" src="https://github.com/user-attachments/assets/fe3d26a8-bed0-4628-9f27-f850c275071d" />



Link Video 
