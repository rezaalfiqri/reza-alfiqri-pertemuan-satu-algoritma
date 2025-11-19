nilai_input = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")

list_nilai = [int(nilai.strip()) for nilai in nilai_input.split(',')]

for nilai in list_nilai:
    if nilai >= 85:
        kategori = 'A'
    elif nilai >= 70:
        kategori = 'B'
    elif nilai >= 55:
        kategori = 'C'
    else:
        kategori = 'D'

    print("Nilai:", nilai, "-", kategori)