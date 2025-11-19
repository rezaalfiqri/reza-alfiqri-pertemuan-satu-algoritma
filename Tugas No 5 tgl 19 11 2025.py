daftar_nama = []
while True:
    # Menampilkan menu
    print("\n===== MENU =====")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")
    print("================")
    # Meminta input dari pengguna
    pilihan = input("Pilih menu (1-4): ")
    # Percabangan untuk navigasi menu
    if pilihan == '1':
        nama = input("Masukkan nama yang ingin ditambahkan: ")
        daftar_nama.append(nama)
        print("Nama", nama, "berhasil ditambahkan.")
    elif pilihan == '2':
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in daftar_nama:
            daftar_nama.remove(nama)
            print("Nama", nama, "berhasil dihapus.")
        else:
            print("Nama", nama, "tidak ditemukan dalam daftar.")  
    elif pilihan == '3':
        print("\n--- Daftar Nama ---")
        if not daftar_nama:
            print("Daftar nama kosong.")
        else:
            for i, nama in enumerate(daftar_nama, 1):
                print(i, ".", nama)  
    elif pilihan == '4':
        print("Program selesai. Sampai jumpa!")
        break  # Keluar dari loop
    else:
        print("Pilihan tidak valid. Mohon masukkan angka 1-4.")
