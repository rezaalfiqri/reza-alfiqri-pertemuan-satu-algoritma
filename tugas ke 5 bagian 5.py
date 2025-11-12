nilai=int(input('masukan nilai:'))
usia=int(input('masukan umur:'))
if nilai>= 75:
    if(usia<15):
        print('selamat ya dek, kamu lulus!')
    else:
        print('selamat ya kak, kamu lulus')
else:
    if (usia<15):
        print('maaf ya dek, coba lagi ya!')
    else:
        print('maaf ya kak, coba lagi ya!')