class Mahasiswa:
    """Kelas untuk merepresentasikan daftar mahasiswa."""
    
    def __init__(self):
        self.daftar_mahasiswa = []

def tambah(nama, nilai):
    """Fungsi untuk menambah data mahasiswa."""
    mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

def tampilkan():
    """Fungsi untuk menampilkan data mahasiswa dalam format tabel."""
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("+====================+=======+")
    print("|  Nama              | Nilai |")
    print("+====================+=======+")
    for mhs in mahasiswa:
        print(f"|  {mhs['nama']: <17} |  {mhs['nilai']: <4} |")
    print("+====================+=======+")

def hapus(nama):
    """Fungsi untuk menghapus data mahasiswa berdasarkan nama."""
    global mahasiswa
    mahasiswa = [mhs for mhs in mahasiswa if mhs['nama'] != nama]
    print(f"Data mahasiswa {nama} berhasil dihapus.")

def ubah(nama, nilai_baru):
    """Fungsi untuk mengubah data mahasiswa berdasarkan nama."""
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah menjadi nilai {nilai_baru}.")
            return 
    print(f"Data mahasiswa {nama} tidak ditemukan.")

# Contoh penggunaan
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            tambah(nama, nilai)
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
