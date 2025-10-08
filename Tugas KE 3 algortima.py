# list kosong
list_kosong = []
# list yang berisi kum'pulan string
list_buah = ['pisang','nanas','melon','durian']
# list berupa kumpulan integer
list_nilai = [80,70,100,90]
# list campuran
list_jawaban = [150,33.33, 'presiden soekarno',False]
print('list_kosong:', list_kosong)
print('list_buah:', list_buah)
print('list_nilai:', list_nilai)
print('list_jawaban:', list_jawaban)
print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])
# ubah data pertama
list_buah[0]='jeruk'
# ubah data terkahir
list_buah[-1]='mangga'
print(list_buah)
# ubah data dalam range
list_buah[1:3]= ['naga','papaya']
print(list_buah)
# tambah data di belakang list
list_buah.append('sirsak')
print(list_buah)
# tambah data di awal list
list_buah.insert(0, 'jambu')
print(list_buah)
# tambah data di index mana pun dalam list
list_buah.insert(2, 'manggis')
print(list_buah)
list_angka=[1,2,3,4,5]
print(list_angka)
# hapus satu angka di belakang
angka_yang_terhapus=list_angka.pop()
print('angka yang terhapus:', angka_yang_terhapus)
print(list_angka)