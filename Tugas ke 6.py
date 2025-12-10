listkota=[
    'jakarta','Surabaya','Depok','Bekasi','Solo','Jogjakarta','Semarang','Makasar'
]
for kota in listkota:
    print(kota)
for i, kota in enumerate(listkota):
    print(i,kota)
for kota in listkota:
    print(kota)
else:
    print('tidak ada lagi item yang tersisa')
kotayangdicari=input('ketik nama kota yang kamu cari:')
for i, kota in enumerate(listkota):
    #kita ubah katanya ke lowercase agar
    #menjadi case insensitive
    if kota.lower()==kotayangdicari.lower():
        print('kota yang anda cari berada pada indeks',i)
        break
    else:
        print('maaf, kota yang anda cari tidak ada')