def cekKarakter(kalimat):
    kalimat_bersih = kalimat.lower()
    no_space = ''
    for i in kalimat_bersih:
        if i.isalpha():
            no_space = no_space + i
    set_huruf = set()
    for karakter in no_space:
        set_huruf.add(karakter)
    list_huruf = list(set_huruf)
    if len(list_huruf) == 26:
        print('Kalimat tersebut memiliki semua huruf')
    else:
        print('Kalimat tersebut tidak memiliki semua huruf')

kalimat = "the quick brown fox jumps over the lazy cat"
cekKarakter(kalimat)