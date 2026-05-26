----------------------------------------
SISTEM JADWAL HARIAN 
----------------------------------------
Program ini dibuat untuk jadi asisten jadwal harian digital. Fungsinya, bisa nambahin agenda baru, nyari kegiatan di jam tertentu, ngitung total aktivitas, sampai ngeliat semua rencana dari pagi sampai malam biar gak ada yang kelewat. Sistem otomatis mendeteksi bentrokan waktu. Jadi, kalau masukin kegiatan baru di jam yang udah ada isinya, program bakal langsung menimpa agenda lama dengan yang paling baru. Bisa tahu dengan cepat apa kegiatan pembuka hari paling pagi dan penutup hari paling malam.

program ini pakai struktur data Binary Search Tree (BST) atau Pohon Pencarian Biner. Setiap jadwal disimpan dalam bentuk node, di mana jam dan menit dikonversi jadi angka biasa (misal jam 07:30 jadi angka 730) sebagai kuncinya. Karena pakai konsep BST, pencarian jadwal jadi efisien. Program tinggal belok ke kiri kalau mau nyari jadwal yang lebih pagi, atau belok ke kanan buat nyari jadwal yang lebih malam. Buat nampilin semua agenda secara berurutan dari terbit matahari sampai tengah malam, program pakai metode In-order Traversal, ngelewatin pohon data dari angka terkecil ke terbesar secara otomatis.

Source Code
<img width="1331" height="903" alt="image" src="https://github.com/user-attachments/assets/1af9dd70-92f0-4019-84d2-46efec0df4dc" />
<img width="1328" height="857" alt="image" src="https://github.com/user-attachments/assets/1e39dd80-8e10-432c-90f2-236b0986fd1a" />
<img width="1322" height="873" alt="image" src="https://github.com/user-attachments/assets/c6707c8d-fb3e-43fd-8635-83f33d622063" />
<img width="1316" height="727" alt="image" src="https://github.com/user-attachments/assets/9577602b-e6c4-416b-ac0f-2b5edb595a35" />


Output
<img width="696" height="549" alt="image" src="https://github.com/user-attachments/assets/90878501-3b4e-471a-92b6-e63b1da8f6f6" />
<img width="698" height="722" alt="image" src="https://github.com/user-attachments/assets/2af97702-f934-4ac5-884f-c4a83349fcb3" />
<img width="498" height="208" alt="image" src="https://github.com/user-attachments/assets/e5f711dd-ec2c-437b-8233-fe75050a5d44" />
