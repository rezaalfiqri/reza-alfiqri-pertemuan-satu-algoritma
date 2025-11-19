# Menerima input jumlah item belanja
jumlah_item = int(input("Masukkan jumlah item belanja: "))

# List untuk menyimpan harga
daftar_harga = []

# Loop untuk setiap item, user memasukkan harga (integer)
for i in range(jumlah_item):
    print("Masukkan harga item ke-", i+1, ": ", end="")
    harga = int(input())
    daftar_harga.append(harga)  # Simpan harga dalam list

# Hitung total belanja
total_belanja = sum(daftar_harga)

# Tentukan diskon
if total_belanja >= 300000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

# Hitung total akhir
total_akhir = total_belanja - diskon

# Tampilkan rincian
print("\n--- Rincian Belanja ---")
print("Daftar harga :", daftar_harga)
print("Total sebelum diskon :", total_belanja)
print("Diskon :", int(diskon))
print("Total akhir :", int(total_akhir))
