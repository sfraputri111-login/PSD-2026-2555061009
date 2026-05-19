-------------------------------------------------------------------
SISTEM ANTREAN BANK MANDIRI  
-------------------------------------------------------------------
Program ini untuk sistem pemanggilan nomor antrean di Bank Mandiri secara digital. di mana admin atau mesin cetak bisa memasukkan nama nasabah baru ke dalam barisan waiting list (enqueue). Ketika teller sudah kosong, nasabah di urutan paling depan akan langsung dipanggil (dequeue). Program ini juga menyediakan fitur untuk mengintip siapa nasabah berikutnya yang harus bersiap-siap (peek) serta memantau seluruh barisan nasabah yang masih mengantre secara keseluruhan (display). 
Tujuannya, yaitu untuk memastikan proses pelayanan nasabah berjalan adil, rapi, dan meminimalkan kesalahan manusia saat pemanggilan. Program ini mengandalkan konsep Queue (Antrean) dengan metode FIFO (First-In, First-Out). Artinya, siapa pun nasabah yang datang dan mencatatkan namanya duluan, dia pula yang akan dilayani pertama kali oleh teller. Agar ukurannya bisa fleksibel, Queue di sini tidak memakai array biasa, melainkan menggunakan Linked List dinamis melalui objek bernama Node. Dengan memanfaatkan dua penunjuk utama front_ptr untuk menandai pintu keluar di depan dan rear_ptr untuk mendeteksi ekor antrean di belakang program dapat menambah atau menghapus data nasabah kapan saja tanpa perlu khawatir memorinya penuh atau terbatas.

source code
<img width="735" height="520" alt="image" src="https://github.com/user-attachments/assets/34114a85-9da1-419b-a123-06565898818a" />
<img width="756" height="530" alt="image" src="https://github.com/user-attachments/assets/319a35e7-1e2b-4bbf-9d81-cb3f0346910c" />
<img width="755" height="452" alt="image" src="https://github.com/user-attachments/assets/411942cd-e520-4bd9-832d-d40ff9e413c3" />
<img width="822" height="518" alt="image" src="https://github.com/user-attachments/assets/25aba8f9-3756-4498-9e02-74d5e0a495a4" />
<img width="767" height="491" alt="image" src="https://github.com/user-attachments/assets/b18be8d0-7881-4495-8959-a41c1c106f0b" />



output dari source code
<img width="467" height="222" alt="image" src="https://github.com/user-attachments/assets/58fb8e29-93c0-4f5e-acec-6079efe3a74c" />
<img width="386" height="122" alt="image" src="https://github.com/user-attachments/assets/1bf0f9b1-bb1d-4d0d-908d-208fe878cce9" />
<img width="457" height="227" alt="image" src="https://github.com/user-attachments/assets/4a78b343-6b7e-4955-87a2-42da085d0873" />
<img width="366" height="73" alt="image" src="https://github.com/user-attachments/assets/0c9e0121-a5b6-4cfa-8f0b-ef4637b27568" />
<img width="447" height="227" alt="image" src="https://github.com/user-attachments/assets/34d05918-ee0b-4e7b-bccd-c5268ef85e00" />
<img width="342" height="86" alt="image" src="https://github.com/user-attachments/assets/fc8f59e3-8ad7-4d50-97ac-8ac136b36c0e" />
<img width="435" height="197" alt="image" src="https://github.com/user-attachments/assets/de585d83-aef4-469b-a3e7-8eca9b6da001" />
<img width="372" height="110" alt="image" src="https://github.com/user-attachments/assets/3b140947-7918-4df9-b3f4-539dab6bcc15" />
<img width="493" height="262" alt="image" src="https://github.com/user-attachments/assets/12b9817c-5f97-4b35-8ccb-af2c5ebdb18a" />
<img width="617" height="275" alt="image" src="https://github.com/user-attachments/assets/92999d29-102a-4dfb-8724-123c82fa97c2" />
<img width="595" height="257" alt="image" src="https://github.com/user-attachments/assets/2d6bc924-580d-450f-a943-0e3083708fc9" />
