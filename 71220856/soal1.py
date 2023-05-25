def hitungHonorAsisten(data,honorPerKelas):
    asdos_gaji = dict()
    for matkul, semua_asdos in data.items():
        for asdos in semua_asdos:
            if asdos in semua_asdos:
                if asdos not in asdos_gaji:
                    asdos_gaji[asdos] = honorPerKelas
                else:
                    asdos_gaji[asdos] += honorPerKelas
    return {k: v for k, v in sorted(asdos_gaji.items(), key= lambda item: item[0])}

data = {
    'Alpro_A':['Rizky', 'Yusak', 'Shalom', 'Tania'],
    'Alpro_B':['Dedi', 'Karen', 'Yusak', 'Tania'],
    'Alpro_C':['Richard', 'Rizky', 'Mikael', 'Yusak'],
    'Alpro_D':['Michelle', 'Tania','Dedi','Karen'],
    'Jarkom_A':['Rizky', 'Vero'],
    'Jarkom_B':['Riel','Natanael'],
    'Jarkom_C':['Yulius','Kevin']
}
print(hitungHonorAsisten(data, 45000))