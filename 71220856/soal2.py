from math import sqrt

def euclidienCalculation(dict1, dict2):
    list_o1 = []
    for i in o1:
        list_o1.append(o1[i])

    list_o2 = []
    for i in o2:
        list_o2.append(o2[i])

    set_all = set()
    for i in o1:
        set_all.add(i)
    for j in o2:
        set_all.add(j)
    list_all = list(set_all)
    jumlah_total_fitur = len(list_all)

    total_fitur_sama = 0
    for i in list_o1:
        for j in list_o2:
            if j == i:
                total_fitur_sama = total_fitur_sama + 1

    list_selisih = []
    for key1 in o1:
        if key1 in o2:
            selisih = o1[key1]-o2[key1]
            pangkat = selisih**2
            list_selisih.append(pangkat)

    atas = 0
    for i in list_selisih:
        atas = atas + i

    eucrel = (atas**0.5)/jumlah_total_fitur
    return(f'EucRel: {eucrel:.3f}')
    #print(f'{list_o1}\n{list_o2}\n{total_fitur_sama}\n{jumlah_total_fitur}')

o1 = {'a':0.1724,'b':0.648,'c':0.021}
o2 = {'a':0.214,'b':0.048,'d':0.121}
euclidienCalculation(o1, o2)
#print('EucRel: %0.3f'%euclidienCalculation(o1,o2))