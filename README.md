# praktikum8
Nama :Rizqi febrian arrahman <P>
Nim  :312410544 <p>
Kelas:TI 24 A5 <p>
# DIAGRAM CLASS
![DIAGRAM CLASS](https://github.com/user-attachments/assets/70bebafc-6539-4dd2-8376-bb65a465b38c)


# FLOWCHART 
![py8](https://github.com/user-attachments/assets/30dbadc1-dfee-49a1-8925-9595499161d1)
Penjelasan Flowchart
(Mulai Program): Titik awal dari program.

(Tampilkan Menu): Menampilkan pilihan menu kepada pengguna.

(Pilih Menu): Pengguna memilih salah satu opsi dari menu.

(Tambah Data Mahasiswa): Jika pengguna memilih untuk menambah data, proses ini akan dijalankan, dan setelah selesai, kembali ke menu.

(Tampilkan Data Mahasiswa): Jika pengguna memilih untuk menampilkan data, proses ini akan dijalankan, dan setelah selesai, kembali ke menu.

(Hapus Data Mahasiswa): Jika pengguna memilih untuk menghapus data, proses ini akan dijalankan, dan setelah selesai, kembali ke menu.

(Ubah Data Mahasiswa): Jika pengguna memilih untuk mengubah data, proses ini akan dijalankan, dan setelah selesai, kembali ke menu.

(Keluar dari Program): Jika pengguna memilih untuk keluar, program akan berhenti.

(Tidak Valid): Jika pilihan tidak valid, program akan kembali ke langkah untuk menampilkan menu.

# PENJELASAN PROGRAM
1. fungsi class

![py8(1)](https://github.com/user-attachments/assets/d1935586-a957-4caa-a6fa-a953fea44e11)


Kelas ini memiliki atribut daftar_mahasiswa, yang merupakan daftar untuk menyimpan data mahasiswa.
Metode tambah, tampilkan, hapus, dan ubah digunakan untuk mengelola data mahasiswa.

2. fungsi __init__

![py8(2)](https://github.com/user-attachments/assets/adb5ddd2-96e2-4e4f-9d3f-92b42246364b)



Konstruktor: Metode __init__ adalah konstruktor yang dipanggil saat objek dari kelas Mahasiswa dibuat.
Atribut daftar_mahasiswa: Atribut ini adalah list kosong yang akan digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary, di mana setiap dictionary berisi nama dan nilai.

3. Fungsi tambah(nama, nilai):

![py8(3)](https://github.com/user-attachments/assets/d578f615-cc56-46b7-ba9e-d3552490bf17)



Fungsi ini digunakan untuk menambahkan data mahasiswa ke dalam list mahasiswa. Data yang ditambahkan adalah nama dan nilai mahasiswa.
Setelah menambahkan data, fungsi ini akan mencetak pesan konfirmasi.

4. Fungsi tampilkan():
![py8(4)](https://github.com/user-attachments/assets/928e4508-e345-4c18-841c-5572fa020f74)




Fungsi ini menampilkan semua data mahasiswa dalam format tabel.
Jika tidak ada data mahasiswa, fungsi ini akan mencetak pesan bahwa tidak ada data yang tersedia.
Jika ada data, fungsi ini mencetak tabel dengan nama dan nilai mahasiswa.

5. Fungsi hapus(nama):

![py8(5)](https://github.com/user-attachments/assets/23fedb27-14ae-412c-8127-1963d5dcb829)



Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan nama.
Fungsi ini akan menyaring list mahasiswa untuk menghapus entri yang memiliki nama yang sesuai.
Setelah menghapus data, fungsi ini mencetak pesan konfirmasi.

6. Fungsi ubah(nama, nilai_baru):

![py8(6)](https://github.com/user-attachments/assets/a1d28438-79b9-47b9-b35a-da03331beed8)



Fungsi ini digunakan untuk mengubah nilai mahasiswa berdasarkan nama.
Fungsi ini mencari mahasiswa dengan nama yang diberikan dan mengubah nilai mereka jika ditemukan.
Jika nama tidak ditemukan, fungsi ini akan mencetak pesan bahwa data mahasiswa tidak ditemukan.

7. Bagian if __name__ == "__main__"::

![py8(7)](https://github.com/user-attachments/assets/5cf755f7-8f6a-4520-b2ad-c9f28a30ef94)


Bagian ini adalah loop utama yang akan terus berjalan hingga pengguna memilih untuk keluar.
Menampilkan menu pilihan kepada pengguna untuk memilih operasi yang diinginkan.
Mengambil input dari pengguna dan memanggil fungsi yang sesuai berdasarkan pilihan pengguna.
# HASIL PROGRAM
![1](https://github.com/user-attachments/assets/a39ef93e-8ae2-4a71-b968-c584b20b0d6b)

![2](https://github.com/user-attachments/assets/726321f7-1fea-451a-86de-06d4238e3755)

![c](https://github.com/user-attachments/assets/b78bd0a6-6849-41ad-ba8d-5f0751912ac9)

![4](https://github.com/user-attachments/assets/f520d0b6-39d0-4548-8ebc-cedaeaf61cf5)


