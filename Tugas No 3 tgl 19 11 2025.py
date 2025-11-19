# Menerima input 5 angka dari user dan menyimpan ke dalam list
angka_list = []
for i in range(5):
    print("Masukkan angka ke-", i+1, ": ", end="")
    angka = int(input())
    angka_list.append(angka)

# Menghitung jumlah angka genap dan ganjil menggunakan percabangan
jumlah_genap = 0
jumlah_ganjil = 0

for angka in angka_list:
    if angka % 2 == 0:
        jumlah_genap += 1
    else:
        jumlah_ganjil += 1

# Menampilkan hasil
print("Jumlah angka genap:", jumlah_genap)
print("Jumlah angka ganjil:", jumlah_ganjil)
