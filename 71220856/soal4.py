def cek_kekurangan(krs1, krs2):
    set1 = set(krs1)
    set2 = set(krs2)
    sama = set1 & set2
    list_sama = list(sama)
    jumlah1 = len(krs1)
    jumlah_sama = len(list_sama)
    hasil = jumlah1 - jumlah_sama
    print(hasil)

krs1 = ['alpro', 'strukdat', 'pbo', 'ppkn', 'toefl', 'prakalpro', 'skripsi', 'kkn', 'statistik', 'ai', 'jarkom', 'tekwan']
krs2 = ['alpro', 'jarkom', 'pbo', 'strukdat', 'statistik', 'hamdem', 'kcp']
cek_kekurangan(krs1, krs2)